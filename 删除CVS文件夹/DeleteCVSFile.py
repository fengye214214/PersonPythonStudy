
import os
import shutil

class DeleteCVSFile:

    def __init__(self):
        pass

    def delete_cvs(self):
        current_dir = os.getcwd()
        print("{0}{1}".format("删除的目录为:", current_dir))
        y_or_N = input  ("确认删除CVS文件 (Y / N)")
        if y_or_N == 'y' or y_or_N == "Y":
            self.list_cvs_file(current_dir)

    def list_cvs_file(self, file_dir):
        file_list = os.listdir(file_dir)
        for f in file_list:
            file_path = os.path.join(file_dir, f)
            if os.path.isdir(file_path):
                if f == "CVS":
                    shutil.rmtree(file_path)
                    print("{0}{1}".format("删除:", file_path))
                else:
                    self.list_cvs_file(file_path)
            else:
                if str(f).startswith(".#"):
                    os.remove(file_path)
                    print("{0}{1}".format("删除:", file_path))



if __name__ == '__main__':
    
    delCVSFile = DeleteCVSFile()
    delCVSFile.delete_cvs()