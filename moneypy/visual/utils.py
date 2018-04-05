"""This module contains the utility functions for the plotting module."""
import pandas as pd


def min_max_date(df_list):
    """Return a list of the min and max dates.
    From each dataframe in the list passed to it.
    """
    new_list = []
    for df in df_list:
        new_list.append((df['Date'].min(), df['Date'].max()))
    return new_list


def min_max_date_format(df_list):
    """Return list of formatted min and max dates in each
    dataframe in the list passed to it.
    """
    new_list = []
    for df in df_list:
        new_list.append((df['Date'].min().strftime('%y/%m/%d'),
                         df['Date'].max().strftime('%y/%m/%d')))
    return new_list


def max_date_range(date_tuple_list):
    """Return the min and max date from a list of dates, (in tuples)."""
    min_date = pd.to_datetime('1979-10-12 00:00:00')
    max_date = pd.to_datetime('1979-10-12 00:00:00')
    for t in date_tuple_list:
        for i in t:
            if i < min_date:
                min_date = i
            elif i > max_date:
                max_date = i
    return min_date, max_date


def format_date_to_string(date_tuple, date_format="yymmdd"):
    """Return the formated dates from the input tuple.
    Using the passed date format.
    """
    min_date, max_date = date_tuple[0], date_tuple[1]
    if date_format.lower() == "yymmdd":
        min_date = min_date.strftime('%y/%m/%d')
        max_date = max_date.strftime('%y/%m/%d')
    elif date_format.lower() == "yymm":
        min_date = min_date.strftime('%y/%m')
        max_date = max_date.strftime('%y/%m')
    return min_date, max_date
