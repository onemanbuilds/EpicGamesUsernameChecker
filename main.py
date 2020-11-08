from colorama import init,Fore,Style
from os import name,system
from sys import stdout
from random import choice
from threading import Thread,Lock,active_count
from string import ascii_letters,digits
from time import sleep
import requests

class Main:
    def clear(self):
        if name == 'posix':
            system('clear')
        elif name in ('ce', 'nt', 'dos'):
            system('cls')
        else:
            print("\n") * 120

    def SetTitle(self,title_name:str):
        system("title {0}".format(title_name))

    def GetRandomUserAgent(self):
        useragents = self.ReadFile('useragents.txt','r')
        return choice(useragents)

    def PrintText(self,bracket_color:Fore,text_in_bracket_color:Fore,text_in_bracket,text):
        self.lock.acquire()
        stdout.flush()
        text = text.encode('ascii','replace').decode()
        stdout.write(Style.BRIGHT+bracket_color+'['+text_in_bracket_color+text_in_bracket+bracket_color+'] '+bracket_color+text+'\n')
        self.lock.release()

    def ReadFile(self,filename,method):
        with open(filename,method,encoding='utf8') as f:
            content = [line.strip('\n') for line in f]
            return content

    def GetRandomProxy(self):
        proxies_file = self.ReadFile('proxies.txt','r')
        proxies = {}
        if self.proxy_type == 1:
            proxies = {
                "http":"http://{0}".format(choice(proxies_file)),
                "https":"https://{0}".format(choice(proxies_file))
            }
        elif self.proxy_type == 2:
            proxies = {
                "http":"socks4://{0}".format(choice(proxies_file)),
                "https":"socks4://{0}".format(choice(proxies_file))
            }
        else:
            proxies = {
                "http":"socks5://{0}".format(choice(proxies_file)),
                "https":"socks5://{0}".format(choice(proxies_file))
            }
        return proxies

    def TitleUpdate(self):
        while True:
            self.SetTitle('One Man Builds EpicGames Username Checker ^& Generator ^| AVAILABLES: {0} ^| TAKENS: {1} ^| RETRIES: {2} ^| THREADS: {3}'.format(self.availables,self.takens,self.retries,active_count()-1))
            sleep(0.1)

    def __init__(self):
        init(convert=True)
        self.clear()
        self.SetTitle('One Man Builds EpicGames Username Checker ^& Generator')
        self.title = Style.BRIGHT+Fore.RED+"""       
                                  ╔═══════════════════════════════════════════════════╗                                 
                                   ╔═╗╔═╗╦╔═╗╔═╗╔═╗╔╦╗╔═╗╔═╗  ╦ ╦╔═╗╔═╗╦═╗╔╗╔╔═╗╔╦╗╔═╗
                                   ║╣ ╠═╝║║  ║ ╦╠═╣║║║║╣ ╚═╗  ║ ║╚═╗║╣ ╠╦╝║║║╠═╣║║║║╣ 
                                   ╚═╝╩  ╩╚═╝╚═╝╩ ╩╩ ╩╚═╝╚═╝  ╚═╝╚═╝╚═╝╩╚═╝╚╝╩ ╩╩ ╩╚═╝
                                                  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗                              
                                                  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝                              
                                                  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═                  
                                  ╚═══════════════════════════════════════════════════╝
        """
        print(self.title)
        self.availables = 0
        self.takens = 0
        self.retries = 0
        self.lock = Lock()
        self.account_type = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Epic ['+Fore.RED+'2'+Fore.CYAN+']PSN ['+Fore.RED+'3'+Fore.CYAN+']Xbox Live: '))
        self.use_proxy = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Proxy ['+Fore.RED+'0'+Fore.CYAN+']Proxyless: '))
        
        if self.use_proxy == 1:
            self.proxy_type = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Https ['+Fore.RED+'2'+Fore.CYAN+']Socks4 ['+Fore.RED+'3'+Fore.CYAN+']Socks5: '))
        
        self.method = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Brute ['+Fore.RED+'0'+Fore.CYAN+']From usernames.txt: '))
        self.threads_num = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Threads: '))

        print('')

    def Start(self):
        Thread(target=self.TitleUpdate).start()
        if self.method == 1:
            username_length = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Length: '))
            include_digits = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Include Digits ['+Fore.RED+'1'+Fore.CYAN+']yes ['+Fore.RED+'0'+Fore.CYAN+']no: '))
            prefix = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Prefix (leave it blank if you dont want to use): '))
            suffix = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Suffix (leave it blank if you dont want to use): '))
            print('')
            Run = True
            while Run:
                if active_count()<=self.threads_num:
                    name = self.GenName(username_length,include_digits,prefix,suffix)
                    Thread(target=self.UsernameCheck,args=(name,)).start()
        else:
            usernames = self.ReadFile('usernames.txt','r')
            for username in usernames:
                Run = True
                while Run:
                    if active_count()<=self.threads_num:
                        Thread(target=self.UsernameCheck,args=(username,)).start()
                        Run = False

    def GenName(self,length,include_digits,prefix,suffix):
        if include_digits == 1:
            name = prefix+''.join(choice(ascii_letters+digits) for num in range(length))+suffix
        else:
            name = prefix+''.join(choice(ascii_letters) for num in range(length))+suffix
        return name

    def UsernameCheck(self,name):
        try:
            headers = {
                'User-Agent':self.GetRandomUserAgent()
            }

            response = ''
            link = ''

            if self.account_type == 1:
                link = f'https://fortnite-api.com/v1/stats/br/v2?name={name}&accountType=epic'
            elif self.account_type == 2:
                link = f'https://fortnite-api.com/v1/stats/br/v2?name={name}&accountType=psn'
            else:
                link = f'https://fortnite-api.com/v1/stats/br/v2?name={name}&accountType=xbl'

            if self.use_proxy == 1:
                response = requests.get(link,headers=headers,proxies=self.GetRandomProxy())
            else:
                response = requests.get(link,headers=headers)

            if response.json()['status'] == 404:
                if response.json()['error'] == 'the requested account does not exist':
                    self.PrintText(Fore.CYAN,Fore.RED,'AVAILABLE',name)
                    with open('availables.txt','a',encoding='utf8') as f:
                        f.write(name+'\n')
                    self.availables += 1
                elif response.json()['error'] == 'the requested profile didnt play any match yet':
                    with open('takens.txt','a',encoding='utf8') as f:
                        f.write(name+'\n')
                    self.takens += 1
            elif response.json()['status'] == 200:
                self.PrintText(Fore.RED,Fore.CYAN,'TAKEN',name)
                with open('takens.txt','a',encoding='utf8') as f:
                    f.write(name+'\n')
                self.takens += 1
            else:
                self.retries = self.retries+1
                self.UsernameCheck(name)
        except:
            self.retries = self.retries+1
            self.UsernameCheck(name)

if __name__ == '__main__':
    main = Main()
    main.Start()