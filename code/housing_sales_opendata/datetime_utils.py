# -*- coding: utf-8 -*-
"""
Helper functions for datetime.
"""
import datetime


def roc_date_to_datetime(roc_date):
    year = int(roc_date[0:3]) + 1911
    month = int(roc_date[3:5])
    day = int(roc_date[5:])
    return datetime.datetime(year, month, day)
