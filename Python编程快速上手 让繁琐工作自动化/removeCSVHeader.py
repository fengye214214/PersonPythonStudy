# python3
# removeCSVHeader.py 删除CSV的第一行，并合并文件 

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('从 %s 文件删除第一行' % (csvFilename))

    csvRows = []
    csvFileObj = open(csvFilename)
    readObj = csv.reader(csvFileObj)
    for row in readObj:
        if readObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    #输出到csv文件夹中
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()