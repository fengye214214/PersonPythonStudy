#! python3
# backupToZip.py 将一个文件夹本分到一个ZIP文件

import zipfile, os 

'''
把文件夹中的全部内容被分到一个ZIP文件中
'''
def backupToZip(folder):
    #确保文件是绝对路径
    folder = os.path.abspath(folder)
    #压缩文件的序号必须依赖于已经存在的文件
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break;
        number = number + 1

    #创建ZIP文件夹
    print('创建 %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for folername, subfolers, filenames in os.walk(folder):
        print('添加文件夹 %s...' % (folername))
        #添加当前文件夹到ZIP文件
        backupZip.write(folername)
    #添加所有文件夹中的文件到ZIP文件
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        '''
        if filename.startswith(newBase) and filename.endswith('.zip')
            continue
        '''
        print('添加文件 %s...' % (filename))
        backupZip.write(os.path.join(folername, filename))
    backupZip.close()
    print('添加完成...')

#if __name__ == '__main__':

backupToZip(".\TempFiles")

