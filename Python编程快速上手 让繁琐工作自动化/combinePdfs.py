#python 3
# combinePdfs.py 把当前路径下的PDF文件合并为一个文件（除了第一页）

import PyPDF2, os 

#获取所有PDF文件的名字
pdfFiles = []
for fileName in os.listdir('.'):
    if fileName.endswith('.pdf'):
        pdfFiles.append(fileName)
pdfFiles.sort()
pdfWriter = PyPDF2.PdfFileWriter()
#循环所有PDF文件
for fileName in pdfFiles:
    pdfFileObj = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
#保存pdf文件
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()