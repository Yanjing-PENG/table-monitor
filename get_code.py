# -*- encoding:utf-8 -*-

import calendar
from datetime import datetime

def getCode():
    """
    Acquire all code ID of futures which are listed on
    China Financial Futures Exchange(CFFEX) today
    """
    codes = {}
    today = datetime.today()
    date_list = calendar.monthcalendar(today.year, today.month)

    if date_list[0][4] > 0:
        expire_date = date_list[2][4]
    else:
        expire_date = date_list[3][4]

    if today.day > expire_date:
        if today.month in [1, 2, 3]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            xia_yue = str(today.year)[2:] + '0' + str(today.month + 2)
            first_ji_yue = str(today.year)[2:] + '06'
            second_ji_yue = str(today.year)[2:] + '09'
        elif today.month in [4, 5, 6]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            xia_yue = str(today.year)[2:] + '0' + str(today.month + 2)
            first_ji_yue = str(today.year)[2:] + '09'
            second_ji_yue = str(today.year)[2:] + '12'
        elif today.month in [7]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            xia_yue = str(today.year)[2:] + '0' + str(today.month + 2)
            first_ji_yue = str(today.year)[2:] + '12'
            second_ji_yue = str(today.year+1)[2:] + '03'
        elif today.month in [8]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            xia_yue = str(today.year)[2:] + str(today.month + 2)
            first_ji_yue = str(today.year)[2:] + '12'
            second_ji_yue = str(today.year+1)[2:] + '03'
        elif today.month in [9]:
            dang_yue = str(today.year)[2:] + str(today.month + 1)
            xia_yue = str(today.year)[2:] + str(today.month + 2)
            first_ji_yue = str(today.year)[2:] + '12'
            second_ji_yue = str(today.year+1)[2:] + '03'
        elif today.month in [10]:
            dang_yue = str(today.year)[2:] + str(today.month + 1)
            xia_yue = str(today.year)[2:] + str(today.month + 2)
            first_ji_yue = str(today.year+1)[2:] + '03'
            second_ji_yue = str(today.year+1)[2:] + '06'
        elif today.month in [11]:
            dang_yue = str(today.year)[2:] + str(today.month + 1)
            xia_yue = str(today.year+1)[2:] + '01'
            first_ji_yue = str(today.year+1)[2:] + '03'
            second_ji_yue = str(today.year+1)[2:] + '06'
        elif today.month in [12]:
            dang_yue = str(today.year+1)[2:] + '01'
            xia_yue = str(today.year+1)[2:] + '02'
            first_ji_yue = str(today.year+1)[2:] + '03'
            second_ji_yue = str(today.year+1)[2:] + '06'
        else:
            raise Exception('GET_CODE ERROR!')
    else:
        if today.month in [2, 3, 4]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month)
            xia_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            first_ji_yue = str(today.year)[2:] + '06'
            second_ji_yue = str(today.year)[2:] + '09'
        elif today.month in [5, 6, 7]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month)
            xia_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            first_ji_yue = str(today.year)[2:] + '09'
            second_ji_yue = str(today.year)[2:] + '12'
        elif today.month in [8]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month)
            xia_yue = str(today.year)[2:] + '0' + str(today.month + 1)
            first_ji_yue = str(today.year)[2:] + '12'
            second_ji_yue = str(today.year+1)[2:] + '03'
        elif today.month in [9]:
            dang_yue = str(today.year)[2:] + '0' + str(today.month)
            xia_yue = str(today.year)[2:] + str(today.month + 1)
            first_ji_yue = str(today.year)[2:] + '12'
            second_ji_yue = str(today.year+1)[2:] + '03'
        elif today.month in [10]:
            dang_yue = str(today.year)[2:] + str(today.month)
            xia_yue = str(today.year)[2:] + str(today.month + 1)
            first_ji_yue = str(today.year)[2:] + '12'
            second_ji_yue = str(today.year+1)[2:] + '03'
        elif today.month in [11]:
            dang_yue = str(today.year)[2:] + str(today.month)
            xia_yue = str(today.year)[2:] + str(today.month + 1)
            first_ji_yue = str(today.year+1)[2:] + '03'
            second_ji_yue = str(today.year+1)[2:] + '06'
        elif today.month in [12]:
            dang_yue = str(today.year)[2:] + str(today.month)
            xia_yue = str(today.year+1)[2:] + '01'
            first_ji_yue = str(today.year+1)[2:] + '03'
            second_ji_yue = str(today.year+1)[2:] + '06'
        elif today.month in [1]:
            dang_yue = str(today.year)[2:] + '01'
            xia_yue = str(today.year)[2:] + '02'
            first_ji_yue = str(today.year)[2:] + '03'
            second_ji_yue = str(today.year)[2:] + '06'
        else:
            raise Exception('GET_CODE ERROR!')

    codes['IF'] = ['IF' + dang_yue + '.CFE', 'IF' + xia_yue + '.CFE', 'IF' + first_ji_yue + '.CFE', 'IF' + second_ji_yue + '.CFE']
    codes['IH'] = ['IH' + dang_yue + '.CFE', 'IH' + xia_yue + '.CFE', 'IH' + first_ji_yue + '.CFE', 'IH' + second_ji_yue + '.CFE']
    codes['IC'] = ['IC' + dang_yue + '.CFE', 'IC' + xia_yue + '.CFE', 'IC' + first_ji_yue + '.CFE', 'IC' + second_ji_yue + '.CFE']

    return codes

if __name__ == '__main__':
    print(getCode())