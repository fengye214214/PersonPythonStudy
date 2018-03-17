# python2.7
# autoCompileCSharpProgram.py 自动化编译C#解决方案
#                             @TDO1: 修改程序集版本
#                             @TDO2: 修改服务器IP
#                             @TDO3: 编译程序集
#                             @TDO4: 修改.suf的版本信息（也就是安装exe的版本信息）
#                             @TDO5: 调用stepFactory打包
#                             @TDO6: 复制exe文件到发布文件夹

import os
import re
import datetime
import shutil
import tempfile
import subprocess
import traceback

#----------------------此注释片段中的变量的值根据实际需要自行修改----------------------
#.\代表打包文件的当前目录
#..\代表打包文件的上级目录
#使用脚本前程序必须安装Setup Factory 9

#打包程序路径
setupFactoryPath = r'D:\Program Files (x86)\Setup Factory 9 Trial\SUFDesign.exe'
#VS编译器地址
VSCompilePath = r'C:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE\devenv'
#要修改的AssemblyInfo.cs文件的路径, .代表相对路径(即使当前updateAssemblyInfo.py的当前路径)
assemblyInfoFilePath = r'..\ConsoleNewSH\Properties\AssemblyInfo.cs' 
exeName = '网格化管理信息系统' #程序集名称，根据实际需要修改
exeCompany = '北京捷思锐科技股份有限公司' #程序集公司名称，根据实际需要修改

#修改APPConfig里appSettings里的应用服务器的IP地址
#元组的第一个值为App.config的路径，第二个值为key,第三个值为value(value必须放在列表里)
serverIPInfo = (r'..\ConsoleNewSH\App.config', 'ApplicationServerIP', ['123.139.56.178', '222.44.126.237'])
#工程sln目录
compileSlnPath = r'..\ConsoleNewSH.sln'
#程序打包文件夹目录路径
stepFile = r'.\Setup\File'
#程序打包程序可执行文件路径
setupFactoryFilePath = r'.\Setup\ConsoleNewSH.suf'

#----------------------此注释片段中的变量的值根据实际需要自行修改----------------------

class autoCompileCSharpProgram:

    allFileVersion = '1.0.0.0'
    serverIP = '0.0.0.0'
    currentPythonPath = os.getcwd() #python脚本所在的位置

    def __init__(self):
        pass

    def updateAssemblyInfos(self):
        '''
        修改程序集的版本信息
        修改程序集名称，程序集描述，程序集公司名称，程序集文件版本
        '''
        f = open(assemblyInfoFilePath, 'r') #打开保存程序集信息的文件
        rnew = open('AssemblyInfoBackup.cs', 'w') #创建备份文件
        fileCurrentVersion = '' #文件当前版本号
        #修改程序集名称，描述，公司，公司版权
        for l in f.readlines():
            m = re.search(r'(Assembly.*)(\(.*\))', str(l)) #匹配括号内的内容  #匹配问号内的内容 r'".*"' 
            if m is not None:
                reStr = r'\(.*\)'
                if 'AssemblyTitle' == m.group(1) or 'AssemblyDescription' == m.group(1): #替换程序集体名称和程序集体描述
                    l = re.sub(reStr, '("' + exeName + '")', l)
                if 'AssemblyCompany' == m.group(1): #替换公司名称
                    l = re.sub(reStr, '("' + exeCompany + '")', l)
                if 'AssemblyCopyright' == m.group(1): #替换公司版权
                    l = re.sub(reStr, '("Copyright ©  ' + str(datetime.datetime.now().year) + '")', l)
                if 'AssemblyVersion' == m.group(1): #程序集版本号
                    autoCompileCSharpProgram.allFileVersion = re.search( r'".*"', m.group(2)).group().replace('"','') #去掉双引号
                    print('当前文件版本号为 %s, 是否修改 Y/N ? ' % (m.group(2)))
                    yOrn = raw_input()
                    if yOrn == 'Y' or yOrn == 'y':
                        print('请输入主版本号:')
                        v1 = raw_input()
                        fileCurrentVersion += v1 + '.'
                        print('请输入次版本号:')
                        v2 = raw_input()
                        fileCurrentVersion += v2 + '.'
                        print('请输入生成号：')
                        v3 = raw_input()
                        fileCurrentVersion += v3 + '.'
                        print('请输入修订号：')
                        v4 = raw_input()
                        fileCurrentVersion += v4
                        ver =re.search(r'\d+.\d+.\d+.\d+', fileCurrentVersion) #校验版本号是否有非数字字符
                        if ver is None:
                            print('文件版本号只能为数字, 程序已退出！')
                            exit()
                        else:
                            autoCompileCSharpProgram.allFileVersion = fileCurrentVersion
                            l = re.sub(reStr, '("' + fileCurrentVersion + '")', l) #程序集版本号
                if 'AssemblyFileVersion' == m.group(1): #文件版本号
                    l = re.sub(reStr, '("' + autoCompileCSharpProgram.allFileVersion + '")', l) #文件版本号
            #把修改的内容写入备份文件
            rnew.write(l)   
        f.close() #关闭打开的AssemblyInfo文件
        rnew.close() #关闭打开的AssemblyInfoBackup文件
        shutil.move('AssemblyInfoBackup.cs', assemblyInfoFilePath)#把AssemblyInfoBackup.cs.cs重命名为AssemblyInfo文件
        print('修改程序版本完成！')

    def updateServiceIP(self):
        '''
        修改服务器IP
        '''
        with open(serverIPInfo[0], 'r') as f : #打开文件
            bfile = 'backReplaceFile.' + serverIPInfo[0].split('.')[-1] #备份文件名称
            fback = open(bfile, 'w') #创建备份文件
            #在文件中寻找和要替换的字符串相等的行
            for l in f.readlines():
                if serverIPInfo[1] in l: #serverIPInfo[1]表示要替换的字符串关键字，也是元组的第二个元素
                    print('请输入相应序号，选择服务器IP：')
                    L = []
                    for i in range(len(serverIPInfo[2])):
                        L.append(str(i + 1))
                        print('%s: %s' % (str(i + 1), serverIPInfo[2][i]))
                    li = raw_input() #输入序号
                    if li not in L:
                        print('没有选择正确的服务器IP，程序已经退出！')
                        exit()
                    resStr = '(?<=\<add key="%s" value=")' % (serverIPInfo[1])
                    reStr = r'%s(.*)(?=")' % (resStr) #拼接正则表达式
                    l = re.sub(reStr, serverIPInfo[2][int(li) - 1], l)
                    autoCompileCSharpProgram.serverIP = serverIPInfo[2][int(li) - 1]
                fback.write(l) #把修改的内容写入备份文件
            f.close()
            fback.close()
            shutil.move(bfile, serverIPInfo[0])#把备份文件重命名为原来的文件
            print('修改服务器IP完成！')

    def RunCMD(self, strinput):
        out_temp = tempfile.TemporaryFile(mode='w+')
        fileno = out_temp.fileno()
        p = subprocess.Popen(strinput, shell=True, stdout=fileno, stderr=fileno)
        p.wait()
        if p.returncode != 0:
            return -1
        else:
            return 0
        if out_temp:
            out_temp.close()

    def compileDLL(self):
        '''
        编译程序集
        '''
        print('开始编译程序集...')
        logFile = 'C#_SDK.log'
        logFilePath = os.path.join(os.getcwd(), logFile)
        if os.path.exists(logFilePath) == True:
            os.unlink(logFilePath) #如果日志文件存在则删除日志文件
        print('开始编译...' + os.path.abspath(compileSlnPath))
        compilecmdPath = '"%s" "%s" /REBUILD  "Release|x86" /OUT %s' % (os.path.normpath(VSCompilePath), os.path.abspath(compileSlnPath), logFile)
        ret = self.RunCMD(compilecmdPath)
        if ret != 0:
            print('编译失败，请查看%s，程序已经退出！' % (logFile))
            subprocess.Popen(['start', logFilePath], shell=True) #打开日志完档
            exit()
        else:
            print('编译成功。')        

    def updateSteupFactoryFile(self):
        '''
        修改.suf的版本信息（也就是安装exe的版本信息）
        返回一个列表，列表第一个元素是安装文件名，第二个元素是输出文件名
        '''
        print('开始修改exe版本信息...')
        count = 0
        fbackFile = 'backAutoPackage.suf'
        #打开f1文件是获取%ProductVer%的Value所在的行
        f1 = open(setupFactoryFilePath, 'r')
        for l in f1.readlines():
            count = count + 1
            if '<Name>%ProductVer%</Name>' in l:
                count = count + 1 #此处在加1是获取<Value></Value> 所在的行
                break
        f1.close()

        #修改文件信息
        f = open(setupFactoryFilePath, 'r') 
        fback = open(fbackFile, 'w') 
        tempL = []
        outputFolder = '' #发布>设置>安装文件>输出文件
        countNew = 0
        for l in f.readlines():
            countNew = countNew + 1
            lex = l 
            res = re.search(r'(?<=\<Filename\>).*?(?=\<\/Filename\>)', lex)
            if res is not None:
                tempL.append(res.group()) #获取 发布>设置>安装文件>安装文件名
            res1 = re.search(r'(?<=\<OutputFolder\>).*?(?=\<\/OutputFolder\>)', lex)
            if res1 is not None:
                outputFolder = res1.group() #获取发布>设置>安装文件>输出文件
            #更新 发布>设置>资源>文件版本
            if 'ResourceFileVersion' in lex:
                l = re.sub(r'(?<=\<ResourceFileVersion\>).*?(?=\<\/ResourceFileVersion\>)', autoCompileCSharpProgram.allFileVersion, lex)
            #更新 发布>设置>资源>产品版本
            if 'ResourceProductVersion' in lex:
                l = re.sub(r'(?<=\<ResourceProductVersion\>).*?(?=\<\/ResourceProductVersion\>)', autoCompileCSharpProgram.allFileVersion, lex)
            #更新 设置>会话变量>%ProductVer%
            if countNew == count:
                l = re.sub(r'(?<=\<Value\>).*?(?=\<\/Value\>)', autoCompileCSharpProgram.allFileVersion, lex)
            fback.write(l)  
        f.close()
        fback.close()
        shutil.move(fbackFile, setupFactoryFilePath)#把备份文件重命名为原来的文件
        resL = []
        resL.append(tempL[1]) #发布>设置>安装文件>安装文件名
        resL.append(outputFolder) #发布>设置>安装文件>输出文件
        print('修改exe版本信息完成！')
        return resL

    def applicationPack(self):
        '''
        程序打包
        '''
        print('开始打包...')
        #复制release程序到打包目录
        #程序的Release目录下的文件已经在ConsoleNewSH的生成事件中复制到AutoPackage\Setup\File目录下了
        #所以此处就直接打包
        #使用Setup Factory 9 Trial编译程序
        sfCmd = '"%s" /BUILD "%s"' % (setupFactoryPath, setupFactoryFilePath.split('\\')[-1])
        #将系统的当前路径切换到setupFactoryFilePath文件夹下
        #因为命令行执行Setup Factory 9 Trial,cmd的当前路径必须在.suf所在的路径
        os.chdir(setupFactoryFilePath.split('\\')[-2])
        #执行命令行调用Setup Factory 9 Trial
        ret = subprocess.Popen(sfCmd, shell=True)
        ret.wait()
        if ret.returncode != 0:
            print('打包失败,请检查 %s 的配置是否正确！' % (setupFactoryFilePath.split('\\')[-1]))
        else:
            print('打包成功！')
        os.chdir(autoCompileCSharpProgram.currentPythonPath) #系统当前路径重新切换回去

    def copyInstallexe(self, exeFilePath):
        '''
        把exe复制到指定文件夹
        '''
        print('开始复制发布exe...')
        p = os.path.basename(os.path.abspath(stepFile))
        p1 = os.path.abspath(stepFile).replace(p, '') #替换为空字符串
        newPath = os.path.join(p1, datetime.datetime.now().strftime('%Y-%m-%d')) #创建发布exe的文件夹
        newPath = os.path.join(newPath, autoCompileCSharpProgram.allFileVersion)
        if os.path.exists(newPath) == False:
            os.makedirs(newPath) #创建存放exe的路径
        shutil.copy(exeFilePath, newPath) #将Setup Factory生成的exe复制到发布文件夹
        pubexepath = os.path.join(newPath, exeFilePath.split('\\')[-1]) #获取复制到发布文件夹的exe的绝对路径
        os.chdir(newPath) #将系统目录切换到发布文件夹下
        oldexeName = exeFilePath.split('\\')[-1]
        newexeName = '%s-%s-%s.exe' % (oldexeName.split('.')[0], autoCompileCSharpProgram.allFileVersion, autoCompileCSharpProgram.serverIP)
        if os.path.exists(newexeName):
            os.remove(newexeName) #删除旧的exe
        os.rename(oldexeName, newexeName) #重命名exe
        print('打包成功！')
        print('打包exe路径: %s' % (os.path.join(newPath, newexeName)))
        os.chdir(autoCompileCSharpProgram.currentPythonPath) #系统当前路径重新切换回去
        ret = subprocess.Popen(['start', newPath], shell=True) #打开发布文件夹
        ret.wait()

if __name__ == '__main__':
    ac = autoCompileCSharpProgram()

    L = []
    #1.修改程序集版本
    try:
        ac.updateAssemblyInfos()
    except Exception as e:
        print('修改程序集版本发生异常!')
        traceback.print_exc()
        raise 
    #2.修改服务器IP'修改程序版本发生异常！'
    try:
        ac.updateServiceIP()
        asd = '33'
    except Exception as e:
        print('修改服务器IP发生异常！')
        traceback.print_exc()
        raise 
    #3.编译程序集
    try:
        ac.compileDLL()
    except Exception as e:
        print('编译程序集发生异常！')
        traceback.print_exc()
        raise
    #4.修改.suf的版本信息（也就是安装exe的版本信息）
    try:
        L = ac.updateSteupFactoryFile()
    except Exception as e:
        print('安装包版本信息修改发生异常！')
        traceback.print_exc()
        raise

    #5.调用stepFactory打包
    try:
        ac.applicationPack()
    except Exception as e:
        print('调用stepFactory打包发生异常！')
        traceback.print_exc()
        raise 
    #6.复制exe文件到发布文件夹
    try: 
        ac.copyInstallexe(os.path.join(L[1], L[0]))
    except Exception as e:
        print('复制exe文件到发布文件夹发生异常！')
        traceback.print_exc()
        raise 



    


