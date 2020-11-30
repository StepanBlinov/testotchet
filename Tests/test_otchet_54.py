import os
import pytest
import allure
from base_funks import request_report
from base_funks import report_can_be_opened
from base_funks import check_date
from base_funks import idfn
from base_funks import idfnorg


@pytest.mark.long
@allure.epic('54 отчет')
@pytest.mark.parametrize('day', (str(i) for i in range(1,32)))
@pytest.mark.parametrize('month', [('prev', 'Prediduschii mesyac'), ('curr', 'Tekuschii mesyac')], ids=idfn)
@pytest.mark.parametrize('org', [(124812, 'Bashkiriya'), (3622, 'Tambov')], ids=idfnorg)
def test_54_report(org, day, month, url):#url передается из confest.py
    """54 отчет"""
    allure.dynamic.story(month[1])
    allure.dynamic.feature(org[1])

    year = ''
    filename = '54 Отчет_'+day+'_'+month[0]+'_.xlsx'
    filename = os.path.join('54 Отчет', filename) #Добавляем папку к имени
    #Нужны только при сравнении с эталоном, а его пока нет
    #etalon = 'Эталон 54 Отчет.xlsx'
    #output_file = 'Результат 54 Отчет.xlsx'

    #Параметры отчета
    exact_date = check_date(day, month[0], year)

    report_uuid = '8464398e-1fe4-4861-b9c5-b8bab42e7f80'
    params = {
        'DT_START': exact_date.strftime('%d.%m.%Y'),
        'DT_END': exact_date.strftime('%d.%m.%Y'),
        'ID_ORG': org[0],
        'ID_PARTNER':-1
    }
    request_report(url['reportserver_url']+'report-query/'+report_uuid+'/XLSX', params, filename)
    allure.attach.file(os.path.join('tmp', filename), extension="xlsx")
    report_can_be_opened(filename)
