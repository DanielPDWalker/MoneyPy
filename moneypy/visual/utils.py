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

def max_date_range(date_tuple_list, date_format=0):
    min_date, max_date = date_tuple_list[0][0], date_tuple_list[0][0]
    for t in date_tuple_list:
        for i in t:
            if i < min_date:
                min_date = i
            elif i > max_date:
                max_date = i
    if date_format == 0:
        min_date, max_date = min_date.strftime('%y/%m/%d'), max_date.strftime('%y/%m/%d')
    elif date_format == 1:
        min_date, max_date = min_date.strftime('%y/%m'), max_date.strftime('%y/%m')
    return min_date, max_date
