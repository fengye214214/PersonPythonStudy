#! python3
# randomQuizGenerator.py Create quizzes with questions and answers in
# random order, along with the answer key.abs

import random, os

#问卷调查数据. key是省，values是省会
capitals = {'山东' : '济南',
            '河北' : '石家庄',
            '吉林' : '长春',
            '黑龙江' : '哈尔滨',
            '辽宁' : '沈阳',
            '内蒙古' : '呼和浩特',
            '新疆' : '乌鲁木齐',
            '甘肃' : '兰州',
            '宁夏' : '银川',
            '山西' : '太原',
            '陕西' : '西安',
            '河南' : '郑州',
            '安徽' : '合肥',
            '江苏' : '南京',
            '浙江' : '杭州',
            '福建' : '福州',
            '广东' : '广州',
            '江西' : '南昌',
            '海南' : '海口',
            '广西' : '南宁',
            '贵州' : '贵阳',
            '湖南' : '长沙',
            '湖北' : '武汉',
            '四川' : '成都',
            '云南' : '昆明',
            '西藏' : '拉萨',
            '青海' : '西宁',
            '天津' : '天津',
            '上海' : '上海',
            '重庆' : '重庆',
            '北京' : '北京',
            '台湾' : '台北',
            '香港' : '香港',
            '澳门' : '澳门'
            }
quizPath = os.path.join(os.getcwd(), 'QuizFiles')
if os.path.exists(quizPath) == False:
    os.makedirs(quizPath)
#生成问卷文件
for quizNum in range(len(capitals)):
    print('生成%s份问卷中...' % (str(quizNum + 1)))
    #创建问卷和回答的文件
    quizFile = open(os.path.join(quizPath, 'capitalsquiz%s.txt' % (quizNum + 1)), 'w')
    #向问卷中写入头
    quizFile.write('姓名:\n\n日期：\n\n分数:\n\n')
    quizFile.write((' ' * 20) + '省会城市问卷调查 (来自 %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #生成考卷问题
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(len(states)):
        quizFile.write('%s. %s的省会是?\n' % (questionNum + 1, states[questionNum]))
        #获取正确和错误的答案
        correctAnswer = capitals[states[questionNum]]
        #获取错误的答案
        wrongAnswer = list(capitals.values())
        #从错误的答案中删除正确的答案
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        #从错误的答案中随机获取三个答案
        wrongAnswer = random.sample(wrongAnswer, 3)
        #将错误答案和正确答案组个到一起
        answerOptions = wrongAnswer + [correctAnswer]
        #重新打乱答案列表的顺序
        random.shuffle(answerOptions)
        #生成考卷答案
        for i in range(4):
            #写入答案
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
print('\n全部生成成功！\n')
        
        
    
  