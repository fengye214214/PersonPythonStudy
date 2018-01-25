#! python3
# factorialLog.py

import logging
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s-%(message)s')
#logging.basicConfig(filename = 'myProgramLog.txt', level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s-%(message)s')
logging.debug('开始程序')
#logging.disable(logging.CRITICAL) 禁止用日志

def factorials(n):
    logging.debug('开始factorials(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= (i + 1)
        logging.debug('i is ' + str((i + 1)) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorials(5))
logging.debug('程序结束')