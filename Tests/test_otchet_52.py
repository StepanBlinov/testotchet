import os
import pytest
import allure
from base_funks import request_report
from base_funks import report_can_be_opened
from base_funks import check_date
from base_funks import idfn


@pytest.mark.fast
@allure.epic('52 отчет')
@pytest.mark.parametrize('day', ['01'])
@pytest.mark.parametrize('month', [('prev', 'Prediduschii mesyac'), ('curr', 'Tekuschii mesyac')], ids=idfn)
def test_52_report(day, month, url):#url передается из confest.py
    """52 отчет"""
    allure.dynamic.story(month[1])
    year = ''
    filename = '52 Отчет_'+day+'_'+month[0]+'_.xlsx'
    filename = os.path.join('52 Отчет', filename) #Добавляем папку к имени
    #etalon = 'Эталон 52 Отчет.xlsx'
    #output_file = 'Результат 52 Отчет.xlsx'

    #Параметры отчета
    exact_date = check_date(day, month[0], year)

    report_uuid = '67be8918-73f7-41d2-9dd2-c542f41dbca7'
    params = {
        'DT_PERIOD': exact_date.strftime('%d.%m.%Y')
    }
    request_report(url['reportserver_url']+'report-query/'+report_uuid+'/XLSX', params, filename)
    allure.attach.file(os.path.join('tmp', filename), extension="xlsx")
    report_can_be_opened(filename)
