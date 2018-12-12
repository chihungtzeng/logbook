# -*- coding: utf-8 -*-
"""
Helper functions for datetime.
"""
import datetime


def roc_date_to_datetime(roc_date):
    try:
        year = int(roc_date[0:3]) + 1911
        month = int(roc_date[3:5])
        day = int(roc_date[5:])
    except:
        year = 1911
        month = 1
        day = 1

    try:
        candidate = datetime.datetime(year, month, day)
    except ValueError:
        candidate = datetime.datetime(1911, 1, 1)
    return candidate
