import os
import pytest
import allure
from base_funks import request_report
from base_funks import report_can_be_opened
from base_funks import check_date
from base_funks import idfn


@pytest.mark.fast
@allure.epic('801 отчет')
@pytest.mark.parametrize('day', ['01'])
@pytest.mark.parametrize('month', [('prev', 'Prediduschii mesyac'), ('curr', 'Tekuschii mesyac')], ids=idfn)
def test_801_report(day, month, url):#url передается из confest.py
    """801 отчет"""
    allure.dynamic.story(month[1])
    year = ''
    filename = '801 Отчет_'+day+'_'+month[0]+'_.xlsx'
    filename = os.path.join('801 Отчет', filename) #Добавляем папку к имени
    #etalon = 'Эталон 801 Отчет.xlsx'
    #output_file = 'Результат 801 Отчет.xlsx'

    #Параметры отчета
    exact_date = check_date(day, month[0], year)

    report_uuid = '8a1b2505-7652-4837-8fd9-3005b663bcbb'
    params = {
        'DT_Start': exact_date.strftime('%d.%m.%Y'),
        'DT_End': exact_date.strftime('%d.%m.%Y'),
        'id_acc': '-1'
    }
    request_report(url['reportserver_url']+'report-query/'+report_uuid+'/XLSX', params, filename)
    allure.attach.file(os.path.join('tmp', filename), extension="xlsx")
    report_can_be_opened(filename)

