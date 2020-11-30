import os
import pytest
import allure
from base_funks import request_report
from base_funks import report_can_be_opened
from base_funks import check_date
from base_funks import idfn


@pytest.mark.fast #метка для запуска быстрых тестов
@allure.epic('18 отчет')
@pytest.mark.parametrize('day', (str(i) for i in range(1,32)))#итератор от 1 до 30
@pytest.mark.parametrize('month', [('prev', 'Prediduschii mesyac'), ('curr', 'Tekuschii mesyac')], ids=idfn)
def test_18_report(day, month, url): #url передается из confest.py
    """18 отчет"""
    allure.dynamic.story(month[1])
    year = ''
    filename = '18 Отчет_'+day+'_'+month[0]+'_.xlsx'
    filename = os.path.join('18 Отчет', filename) #Добавляем папку к имени
    #etalon = 'Эталон 18 Отчет.xlsx'
    #output_file = 'Результат 18 Отчет.xlsx'

    #Параметры отчета
    exact_date = check_date(day, month[0], year)

    report_uuid = 'a549cc34-b7b8-49a5-afcf-ea970ad738f7'
    params = {
        'DT_BEGIN': exact_date.strftime('%d.%m.%Y'),
        'DT_END': exact_date.strftime('%d.%m.%Y'),
        'SCHEMA_OUT':'Все',
        'SCHEMA_IN':'Все',
        'TYPE_PAY':'1, 2, 3'
    }
    request_report(url['reportserver_url']+'report-query/'+report_uuid+'/XLSX', params, filename)
    allure.attach.file(os.path.join('tmp', filename), extension="xlsx")
    report_can_be_opened(filename)


