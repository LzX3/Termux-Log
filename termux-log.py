from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m{-------------V1.0-------------}')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m  786 => ยินดีต้อนรับครับ')")
           print("\033[1;93m")
           print("  <───────[ ฝากช่อง youtube Lz X3 ]───────>")
           print("")
           try:
                x = str(input('\033[1;92mใส่Username \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mใส่Password \033[1;93m: ')
                print ("")
                if x=="Username" and e=="Password":
                   print('ระบบกำลังทำรายการกรุณารอสักครู่ครับ...')
                   time.sleep(5)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")                                                                                            print("\033[1;91m     Wrong Password")                                                               time.sleep(2)
                      print("")                                                                                 except Exception:                                                                                               print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
menu()
