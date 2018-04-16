
import argparse
import sys
import plistlib
from matplotlib import pyplot
import numpy as np

def findCommonTracks(fileNames):
    '''
    寻找多个播放列表的共同音轨，并把他们保存到common.txt
    '''
    #一个设置tracks names的列表集合
    trackNameSets = []
    for fileName in fileNames:
        #创建一个新的set
        tracksNames = set()
        #在playlist中读取
        plist = plistlib.readPlist(fileName)
        #获取track
        tracks = plist['Tracks']
        #迭代tracks
        for trackId, track in tracks.items():
            try:
                #添加名称到set
                tracksNames.add(track['Name'])
            except:
                pass
        #添加到list
        trackNameSets.append(tracksNames)
    #获取共同的tracks set
    commonTracks = set.intersection(*trackNameSets)
    #写入到文件
    if len(commonTracks) > 0:
        with open('common.txt', 'wb') as f:
            for val in commonTracks:
                s = "%s\n" % val
                f.write(s.encode('utf-8'))
            f.close()
            print('%d 共同track已经找到。track名称已经写入common.txt' % len(commonTracks))
    else:
        print('No common tracks!')
        

def findDuplicates(fileName):
    '''
    在给的列表里寻找重复的曲目
    '''
    print('在文件%s中寻找重复的曲目...' % fileName)
    #读取playList
    plist = plistlib.readPlist(fileName)
    #获取tracks
    tracks = plist['Tracks']
    #创建一个tracks名称的dict
    trackName = {}
    #迭代tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            #判断确定存在
            if name in trackName:
                #如果名称和时长匹配，增加计数
                #时长接近秒
                if duration // 1000 == trackName[name][0] // 1000:
                    count = trackName[name][1]
                    trackName[name] = (duration, count + 1)
            else:
                #增加时长和计数
                trackName[name] = (duration, 1)
        except:
            pass
    #存储副本为(name, count) tuples
    dups = []
    for k, v in trackName.items():
        if v[1] > 1:
            dups.append((v[1], k))
    #把dups存到文件
    if len(dups) > 0:
        print('找到副本%s Track名称存到dup.txt' % len(dups))
    else:
        print('没有找到副本！')
    with open('dups.txt', 'w') as f:
        for val in dups:
            f.write('[%s] %s\n' % (val[0], val[1]))
        f.close()

    
def plotStats(fileName):
    '''
    收集统计信息
    '''
    #读取playlist
    plist = plistlib.readPlist(fileName)
    #获取tracks
    tracks = plist['Tracks']
    #创建速率和范围的列表
    ratings = []
    durations = []
    #迭代tracks
    for trackId, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass
    print(ratings)
    print(durations)
    #确保合法的数据被收集
    if ratings == [] or durations == []:
        print('%s 没有合法的数据' % fileName)
        return


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
        #寻找共同的tracks
        findCommonTracks(args.plFiles)
    elif args.plFile:
        print(args.plFile)
        plotStats(args.plFile)
    elif args.plFileD:
        print(args.plFileD)
        #查找重复的曲目
        findDuplicates(args.plFileD)
    else:
        print('没有你输入的命名')
        
if __name__ == '__main__':
    main()