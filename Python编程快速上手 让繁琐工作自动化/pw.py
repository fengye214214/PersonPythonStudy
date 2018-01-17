import sys
import pprint
import pyperclip

#! python3
# pw.py -An insure password locker program.
# 口令保管箱

class PasswordManager:

    def __init__(self):
        
        global PASSWORDS

        PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
                'luggage': '12345'}

    def getPwd(self):
        print(pprint.pformat(PASSWORDS))
        if len(sys.argv) < 2:
            print('Usage:python pw.py [account] - copy account password')
            sys.exit()
        account = sys.argv[1] #first command line arg is the account name
        if account in PASSWORDS:
            pyperclip.copy(PASSWORDS[account])
            print('Password for ' + account + ' copied to clipboard.')
        else:
            print('There is no account named  ' + account)


if __name__ == '__main__':
    pw = PasswordManager()
    pw.getPwd()