# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:00:04 2017

@author: marti
"""

import os
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns
import datetime


# os.chdir("C:\\work\\School\\research\\research-2017-2018\\python-practice\\date-table")
os.chdir("C:\\Users\\km6e.ESERVICES\\Documents\\GitHub\\roll-analysis")

_baseYear = 2000
_baseMon = 1
_baseDay = 1
_baseHour = 10
_baseMin = 45
_startTime = datetime.datetime(_baseYear, _baseMon, _baseDay, 10, 45)
_registerDelta = datetime.timedelta(hours = 2.00)

class Student:
    def __init__(self, name, ID):
        self.ID = ID
        self.name = name
        self.entries = []
        self.validEntries = {}
        self.invalidEntries = []

    def validateEntries(self, dates, timeInterval):
        for entry in self.entries:
            pass

def cleanID(rawID):
    cleaned = ""
    if type(rawID) is str:
        cleaned = str.lower(rawID)
    cleaned = str.split(cleaned, '@')[0]
    cleaned = str.strip(cleaned)
    return cleaned

_attDF = {}
_datesList = []
_studentDF = {}


def readData():
    # Read in table
    global _attDF, _datesList, _studentDF
    _attDF = pd.read_excel("attendance-2018.xlsx")
    _attDF['Timestamp'] = pd.to_datetime(_attDF['Timestamp'])
    _attDF['ID'] = _attDF['ID'].apply(cleanID)

    datesDF = pd.read_excel("dates.xlsx")
    datesDF['Dates'] = pd.to_datetime(datesDF['Dates'])
    _datesList = []
    for index, row in datesDF.iterrows():
        td = row['Dates']
        _datesList.append(td.date())

    _studentDF = pd.read_excel("students-2018.xlsx")


def initStudents():
    global _studentDF
    result = []
    for index, row in _studentDF.iterrows():
        name = row['Name']
        ID = row['ID']
        curStu = Student(name, ID)
        result.append(curStu)
    return result

def assignDates(stuList):
    for stu in stuList:
        regRecords = _attDF.loc[_attDF['ID'] == stu.ID]
        regDates = regRecords['Timestamp'].tolist()
        stu.entries = regDates


def dateValid(date):
    global _datesList
    result = (date in _datesList)
    return result

def timeValid(time):
    global _startTime, _registerDelta
    global _baseYear, _baseMon, _baseDay
    dTime = datetime.datetime(_baseYear, _baseMon, _baseDay, time.hour, time.minute)
    delta = dTime - _startTime;
    return (delta <= _registerDelta)


def validateDates(stuList):
    for stu in stuList:
        for entry in stu.entries:
            if dateValid(entry.date()) and timeValid(entry.time()):
                stu.validEntries[entry.date()] = 1
            else:
                stu.invalidEntries.append(entry)


# --- Do the work here.
readData()
stuList = initStudents()
assignDates(stuList)
validateDates(stuList)



#---------------------
f = open("result.csv", 'w')
f.write("Name|ID|Valid|Invalid\n")
for stu in stuList:
    f.write("%s|%s|%d|%d\n" % (stu.name, stu.ID, len(stu.validEntries), len(stu.invalidEntries)))
f.close()

for stu in stuList:
    print("%s" % (stu.name))
    for entry in stu.validEntries:
        print("%s" % (entry))
    if (len(stu.invalidEntries) > 0):
        print("Invalid:")
        for entry in stu.invalidEntries:
            print("%s" % (entry))
    print("\n")


    