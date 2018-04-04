# python3.x

import optparse
from socket import *
from threading import *
import subprocess
import re
import nmap


screenLock = Semaphore(value = 1)

def main():
    ''' 
    #linux��������ִ��
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if tgtHost == None or tgtPorts[0] == None:
        print(parser.usage)
        exit(0)
    '''

    '''
    fdout = open("file_out.txt",'w')
    sub = subprocess.Popen('netstat',shell = True, stdout = subprocess.PIPE)
    sub.wait()
    if sub.returncode == 0:
        res = sub.stdout.read()
        fdout.write(str(res))
        fdout.close()
        print('ok1')
    else:
        print('ִ��cmd����ʧ�ܣ�')
        raise
    '''

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect(tgtHost, tgtPort)
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %s/tcp oopen' % tgtPort)
        print('[+]' + str(results))
    except:
        screenLock.acquire()
        print('[-] %s/tcp closed' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve %s: UnKnown host' % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP[0])  

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args = (tgtHost, int(tgtPort)))
        t.start()
    

if __name__ == '__main__':
    
    #����һ
    f = open('file_out.txt', 'r')
    for res in f.readlines():
        portScan(res.strip().split(':')[0], res.strip().split(':')[1])

    #������
    '''
    f = open('file_out.txt', 'r')
    for res in f.readlines():
        nmScan = nmap.portScan()
        nmScan.scan(res.strip().split(':')[0], res.strip().split(':')[1])
        state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
        print("[*] " + tgtHost + " tcp/"+tgtPort +" "+state)
    '''
