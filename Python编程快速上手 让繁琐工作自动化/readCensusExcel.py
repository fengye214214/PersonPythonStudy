#! python3
# readCensusExcel.py 从excel电子表格中读取数据

import openpyxl, pprint

print('打开工作簿...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countryData = {}
print('读取行...')
for row in range(2, sheet.max_row + 1): #max_column
    #获取数据
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    #确保州这个key存在
    countryData.setdefault(state, {})
    #确保国家这个Key的州是存在的
    countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})
    # Each row represents one census tract, so increment by one.
    countryData[state][country]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countryData[state][country]['pop'] += int(pop)

#写入文件
print('写入结果...')
resFile = open('census2010.py', 'w')
resFile.write('allData = ' + pprint.pformat(countryData))
resFile.close()
print('ok')