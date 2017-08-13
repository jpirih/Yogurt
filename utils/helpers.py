import datetime
import json


def str_to_date(string_date):
    """
    :rtype: Converts date string from html form to python date
    format for saving to datastore
    """
    date = datetime.datetime.strptime(string_date, "%m/%d/%Y")
    return date


def slo_date_string(date):
    slo_date = datetime.datetime.strftime(date, "%d.%m.%Y")
    return slo_date


def good_until_calculate(production_date, life_period=7):
    """
    :rtype: This function calculates good life period for yougur
    depending on production date
    """
    good_until = production_date + datetime.timedelta(days=life_period)
    return good_until



