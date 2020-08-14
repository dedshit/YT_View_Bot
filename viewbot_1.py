#!/usr/bin/python3
import random
import bs4 as pi
import requests as R
import headers as H

class test:
    def __init__(self, url):
        self.url = url
        
    def views(self):
        Z = R.get(self.url)
        X = pi.BeautifulSoup(Z.content.decode('utf-8'), 'html5lib')
        V = X.find_all("script")[13].text
        a2 = []
        for i in V.split(','):
            if "viewCount" in i:
                a2.append(i)
        b5 = a2[0].replace("\\", "")[13:-1]
        print("\n Current Views: ", b5)
        
    def Main(self):
        try:
            while True:
                for o in range(1, 10):
                    U = random.choice(H.head)
                h = {
                    "User-Agent":U,
                    "Accept":"*/*",
                    "Accept-Encoding":"gzip, deflate, br",
                    "Accept-Language":"en-us,en;q=0.5",
                    "Connection":"keep-alive",
                    "Host":"www.youtube.com",
                    "Referer":"https://www.youtube.com/",
                    "TE":"Trailers"
                }
                print("--------")
                rr = R.get(self.url, headers=h, allow_redirects=False)
                if rr.status_code == 200:
                    print("Ok")
                else:
                    print("retrying..")
        except R.exceptions.ChunkedEncodingError:
            print('connection error!')
        except KeyboardInterrupt:
            print('Quitting..')                            
q = input('\n Enter video url : ')
q1 = test(q)
q1.Main()
q1.views()
