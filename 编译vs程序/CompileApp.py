
import sys, configparser, time, os, re

class CompileApp:

    def __init__(self):
        #读取配置文件
        global config
        #工程路径
        global project_dir
        #visual studio路径
        global vs_compiler
        #服务器IP
        global server_ip
        #更新IP地址的文件
        global update_file_ip
        #程序集信息文件
        global update_assembly

        config = configparser.ConfigParser()
        config.readfp(open("config.ini", "r", encoding='UTF-8', errors='ignore'))
        project_dir = config.get("Config", "ProjectDir")
        vs_compiler = config.get("Config", "Compiler")
        server_ip = ["123.139.56.178", "122.83.0.138"]
        update_file_ip =  os.path.join(project_dir, "AutoPackageApp\AutoPackageApp\Common\SystemVariable.cs")

    def start_compile(self):
        #选择服务器IP
        new_serverip = self.select_serverip()
        #更改服务器IP
        self.update_app_serverip(new_serverip)
        #更新程序集版本信息
        self.update_assembly_info()


    def select_serverip(self):
        print("请输入:前面的索引选择服务器IP:")
        index = 0
        for s in server_ip:
            print("{0}{1}{2}".format(index,": ",s))
            index += 1
        input_index = int(input())
        if input_index < 0 or input_index >= len(server_ip):
            print("请选择正确的服务器IP地址")
            time.sleep(2)
            exit(1)
        else:
            return server_ip[input_index]

    def update_app_serverip(self, serverip):
        temp_ip = ""
        f = open(update_file_ip, "r", encoding='UTF-8', errors='ignore')
        for line in f.readlines():
            if line.find("SERVER_IP") >= 0:
                reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
                find_ip = reip.findall(line) #替换IP地址
                line = line.replace(find_ip[0], serverip)
            temp_ip += line
        f.close()
        fw = open(update_file_ip, "w", encoding='UTF-8', errors='ignore')
        fw.write(temp_ip)
        fw.close()
        print("改变IP地址成功!")

    def update_assembly_info(self):
        print("ok")
        
    def test_print(self):
        print(project_dir)
        print(vs_compiler)

if __name__ == "__main__":
    comApp = CompileApp()
    comApp.start_compile()
