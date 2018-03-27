import pandas as pd

def min_max_date(df_list):
    new_list = []
    for df in df_list:
        new_list.append((df['Date'].min(),df['Date'].max()))
    return new_list

def min_max_date_format(df_list):
    new_list = []
    for df in df_list:
        new_list.append((df['Date'].min().strftime('%y/%m/%d'),df['Date'].max().strftime('%y/%m/%d')))
    return new_list

def max_date_range(date_tuple_list):
    min_date, max_date = date_tuple_list[0][0], date_tuple_list[0][0]
    for t in date_tuple_list:
        for i in t:
            if i < min_date:
                min_date = i
            elif i > max_date:
                max_date = i
    return min_date, max_date

def format_date_to_string(date_tuple, date_format="yymmdd")
    min_date, max_date = date_tuple[0], date_tuple[1]
    if date_format.lower() == "yymmdd":
        min_date, max_date = min_date.strftime('%y/%m/%d'), max_date.strftime('%y/%m/%d')
    elif date_format.lower() == "yymm":
        min_date, max_date = min_date.strftime('%y/%m'), max_date.strftime('%y/%m')
    return min_date, max_date


