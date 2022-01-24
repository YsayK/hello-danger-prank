import time
import random
import os
from colorama import init
from colorama import Fore, Back, Style

init()

loading_pro = random.randint(1, 5)
loading = False

time.sleep(1)
print("Здравствуйте, Как вам обращаться?")
name = input()
time.sleep(1)
print('Прекрасно... ' + name + ', Подождите секунду...')

time.sleep(1)
print('\nStarting PC scan... ')
time.sleep(random.uniform(0.3, 0.7))
loading = True

while loading:
    if loading_pro < 99:
        print('Loading ' + str(loading_pro) + '%...')
        loading_pro += random.randint(13,23)
        time.sleep(random.uniform(0.3, 1.3))
    else:
        loading_pro = 99
        loading = False
        break


print('Loading ' + str(loading_pro) + '%...')
time.sleep(random.uniform(0.7, 1))
print('Updating and checking... \n')


time.sleep(1.5)
print('  info founded:')
time.sleep(1)
print(Fore.WHITE + 'age info:' + Fore.GREEN + ' yes')
time.sleep(0.4)
print(Fore.WHITE + 'surname:' + Fore.GREEN + ' yes')
time.sleep(1.2)
print(Fore.WHITE + 'address info:' + Fore.GREEN + ' yes')
time.sleep(0.4)
print(Fore.WHITE + 'phone number:' + Fore.GREEN + ' yes')
time.sleep(0.9)
print(Fore.WHITE + 'bank card-number info:' + Fore.GREEN + ' yes')
time.sleep(1)
print(Fore.WHITE + 'bank card-ccv info:' + Fore.RED + ' failed.error47588')

time.sleep(0.5)
print(Fore.WHITE + '\nНайдена Информация будет ' + Fore.RED + ' отправлена ' + Fore.WHITE + ' по данному ' + Fore.RED + ' адресу '+ Fore.WHITE + ' : ...D:/MyPc/'+ Fore.RED + 'vadim' + Fore.WHITE + '/hacked_people/' + Fore.GREEN + name + Fore.WHITE + "_pc_info")

time.sleep(random.uniform(0.3, 0.7))
os.startfile('C:\\')
time.sleep(random.uniform(0.3, 0.7))
os.startfile('C:\\Program Files')
time.sleep(random.uniform(0.3, 0.7))
os.startfile('C:\\Program Files (x86)')

time.sleep(9)
print("\nБлокируем ваше устройство...")
time.sleep(2.5)
print('Завершение работы через 5...')
time.sleep(0.7)
print('4...')
time.sleep(0.7)
print('3...')
time.sleep(0.7)
print('2...')
time.sleep(0.7)
print(Fore.RED + '1...')
time.sleep(0.7)
print('''
█████████████████████████████████████████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░█████████████░░░░░░░░░░░░░░██
██░░░░░░░░░░░█████═════════█████░░░░░░░░░░░██
██░░░░░░░░░░███═══════════════███░░░░░░░░░░██
██░░░░░░░░░██═══════════════════██░░░░░░░░░██
██░░░░░░░░██═════════════════════█░░░░░░░░░██
██░░░░░░░░██═█═════════════════█═██░░░░░░░░██
██░░░░░░░░██═██═══════════════██═█░░░░░░░░░██
██░░░░░░░░░██═█══███═════███══█═██░░░░░░░░░██
██░░░░░░░░░░██══█████═══█████═████░░░░░░░░░██
██░░░░░██░░░██═██████═══█████══██░░░██░░░░░██
██░░░░█████░█═══████══█══████══██░░████░░░░██
██░░░██════███═══════███═══════████═══██░░░██
██░░░███████═████═══█████═══███════█████░░░██
██░░░░░░░░░█████═█════════██═██████████░░░░██
██░░░░░░░░░░░░██═███═════███═██░░░░░░░░░░░░██
██░░░░░░░░░░░░██═██████████══██░░░░░░░░░░░░██
██░░░░███████████═══█████═══█████████░░░░░░██
██░░░░██══════█████═══════████═══██████░░░░██
██░░░░░██══████░░░█████████░░████═══██░░░░░██
██░░░░░░████░░░░░░░░░███░░░░░░░░█████░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
█████████████████████████████████████████████
''')

time.sleep(1)
#os.system("shutdown /s /t 1")
