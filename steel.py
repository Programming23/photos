
import requests
import os
import time

def main(url):
    print(url)
    r = requests.get(f'https://selfi-portfolio.netlify.app/{url}')
    try:
        if url.find('img/') != -1:
            w = open(f'{url}', 'wb')
            w.write(r.content)
        else:
            w = open(f'{url}', 'w', encoding='utf-8')
            w.write(r.text)
    except:
        k = "\\".join(url.replace('/', '\\').split('\\')[:-1])
        os.popen(f'mkdir {k}')
        time.sleep(3)
        print(url, '33')
        if url.find('img/') != -1:
            w = open(f'{url}', 'wb')
            w.write(r.content)
        else:
            w = open(f'{url}', 'w', encoding='utf-8')

            w.write(r.text)
    w.close()

r = requests.get('https://selfi-portfolio.netlify.app')

html = r.text
                 
index = open('index.html', 'w', encoding='utf-8')
index.write(html)
index.close()

s = 0
while True:
    s = html.find('assets', s)
    if s == -1:
        break
    e = html.find('"', s)
    main(html[s:e])
    s = e


