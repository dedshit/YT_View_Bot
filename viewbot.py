#!/usr/bin/python3

import requests as R
import random 

class test:

    def __init__(self, proxy, url):
        self.proxy = proxy
        self.url = url

    def test(self):       
        a = R.get(self.proxy)
        b = a.content.decode('utf-8')
        p = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; Lenovo A7600-F Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'
        ]
        for i in b.split(','):
            try:
                while True:
                    for o in range(1, 10):
                        U = random.choice(p)
                    h = { "User-Agent":U }
                    print ("--------")
                    try:
                        rr = R.get(self.url, headers=h)
                        if rr.status_code == 200:
                            print ("Ok")
                    except R.exceptions.ConnectionError:
                        print ("Retrying...")
            except R.exceptions.Timeout:
                print ('')
            except R.exceptions.ChunkedEncodingError:
                print ('connection error!')
            except KeyboardInterrupt:
                print ('Quitting..')
                
q = input('\n Enter video url : ')
q1 = test("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000&country=all&ssl=yes&anonymity=elite", q)
q1.test()
