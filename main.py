import calendar, sys, os
from time import sleep
os.system('clear')

log = ('''
    +-----------------------------+
    | SIMPLE SCRIPT | COLLECTION  |
    +-----------------------------+''')

def main():
    try:
        print ('')
        print (log)
        print ('')
        print ('------------------')
        print ('[+] MENU:         ')
        print ('------------------')
        print ('[1] Calendar      ')
        print ('[2] Calculator    ')
        print ('[0] Exit          ')
        print ('------------------')
        print ('[+] Enter Number: ')
        choose = input('=>: ')
        if choose == '1':
            def cal():
                try:
                    print ('')
                    print ('[+] Enter The year and Month: ')
                    print ('-'*29)
                    y = int(input('[+] Year : '))
                    m = int(input('[+] Month: '))
                    os.system('clear')
                    print (calendar.month(y, m))
                    print ('-'*29)
                    quit()
                except ValueError:
                    print ('[!] Please Enter year and Month?')
                except KeyboardInterrupt:
                    print ('[!] Stopped')
            
            def quit():
                cb = input('[?] Try Again (y/t): ')
                if cb[0].upper() == 'T':
                    os.system('clear')
                    main()
                else:
                    os.system('clear')
                    cal()
            if __name__ == '__main__':
                cal()

        elif choose == '2':
            def calc():
                try:
                    print ('')
                    a = int(input('[+] Enter the number to 1: '))
                    b = int(input('[+] Enter the number to 2: '))
                    os.system('clear')
                    print ('')
                    print ('    +---------------------+')
                    print ('    | SIMPLE | CALCULATOR |')
                    print ('    +---------------------+')
                    print ('')
                    print ('------------------')
                    print ('[+] MENU:         ')
                    print ('------------------')
                    print ('[1] Pertambahan   ')
                    print ('[2] Perkalian     ')
                    print ('[3] Pengurangan   ')
                    print ('[4] Pembagian     ')
                    print ('------------------')
                    print ('[+] Enter Number: ')
                    choose = int(input('=>: '))
                    if choose == 1:
                        c = a + b
                    elif choose == 2:
                        c = a * b
                    elif choose == 3:
                        c = a - b
                    elif choose == 4:
                        c = a / b
                    print ('-'*18)
                    print ('[+] Result: %d' %c)
                    print ('')
                    quit()
                except ValueError:
                    print ('[!] Wrong Input')
                except KeyboardInterrupt:
                    print ('[!] Stopped')

            def quit():
                cb = input('[?] Try Again (y/t): ')
                if cb[0].upper() == 'T':
                    os.system('clear')
                    main()
                else:
                    os.system('clear')
                    calc()
            if __name__ == '__main__':
                calc()
        elif choose == '0':
            def ex():
                try:
                    print ('')
                    print ('-'*18)
                    print ('[-] Thank you')
                except KeyboardInterrupt:
                    print ('')
            if __name__ == '__main__':
                ex()
        else:
            print ('[!] Wrong Input')

    except KeyboardInterrupt:
        print ('[!] Stopped')

if __name__ == '__main__':
    main()