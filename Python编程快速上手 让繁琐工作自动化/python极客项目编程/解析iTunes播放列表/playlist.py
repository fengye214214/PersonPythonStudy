# python2.7
# playlist.py

import argparse
import sys

def main():
    print('文件所在路径: %s' % (sys.argv[0]))

    parser = argparse.ArgumentParser(description='三个命令行，选择不同的命令行，完成不同的功能')
    #给组添加多个独有的参数
    group = parser.add_mutually_exclusive_group()
    #给组添加期望的参数
    group.add_argument('--common', nargs = '*', dest = 'plFiles', required = False, help = '获取列表')
    group.add_argument('--stats', dest = 'plFile', required = False, help = '获取列表1')
    group.add_argument('--dup', dest = 'plFileD', required = False, help = '获取列表2')
    #转换参数
    args = parser.parse_args()
    if args.plFiles:
        print(args.plFiles)
    elif args.plFile:
        print(args.plFile)
    elif args.plFileD:
        print(args.plFileD)
    else:
        print('没有你输入的命名')
        
if __name__ == '__main__':
    main()