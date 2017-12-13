import os
import shutil

class GetAllFileExtension:
    
    def __init__(self):
        global L

        L = []

    def file_extension(self):
        file_dir = os.getcwd()
        self.print_all_file_extension(file_dir)
        print(set(L))
        

    def print_all_file_extension(self, file_dir):
        file_list = os.listdir(file_dir)
        for f in file_list:
            file_path = os.path.join(file_dir, f)
            #文件夹
            if os.path.isdir(file_path):
                self.print_all_file_extension(file_path)
            #文件
            if os.path.isfile(file_path):
                ex = str(f).split('.')[-1]
                L.append(ex)
            

if __name__ == '__main__':
    all = GetAllFileExtension()
    all.file_extension()