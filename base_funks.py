import os
import datetime
import xlrd
import requests as r
import pytest
import allure


#фукция для корректного отображения информации о параметризации (месяц, день)
def idfn(val):
    return " Data: {0}, day".format(str(val[1]))

#фукция для корректного отображения информации о параметризации (город)
def idfnorg(val):
    return " City:{0}".format(str(val[1]))

@allure.step('Запрос в отчетку')
# получат отчет из отчетки (формирует)
def request_report(report_url, params, resultpath):
    res = r.get(report_url, params=params)
    print(res.status_code)
    f = open(os.path.join('tmp', resultpath), 'wb')
    f.write(res.content)
    f.close()

@allure.step('Отчет удалось открыть')
def report_can_be_opened(filename):
    wb1 = xlrd.open_workbook(os.path.join('tmp', filename))
    sheet1 = wb1.sheet_by_index(0)
    print('В сформированном отчете: ')
    print('строк '+str(sheet1.nrows))
    print('столбцов '+str(sheet1.ncols))

@allure.step('Преобразование даты')
# функция для преоброзования даты
def get_data(day_str, month_str, year_str):
    day = int(day_str)
    if month_str == 'prev':
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        month = lastMonth.month
        year = lastMonth.year
    elif month_str == 'curr':
        today = datetime.date.today()
        month = today.month
        year = today.year
    else:
        month = int(month_str)
        year = int(year_str)
    try:
        exact_date = datetime.date(year, month, day)
    except ValueError:
        return None
    else:
        return exact_date

@allure.step('Проверить дату')
def check_date(day, month, year):
    exact_date = get_data(day, month, year)
    if exact_date is None:
        pytest.skip('Дата больше текущей')
        #context.scenario.skip(reason='Некорректная дата')
    if exact_date >= datetime.date.today():
        pytest.skip('Дата больше текущей')
        #context.scenario.skip(reason='Дата больше текущей')
    return exact_date