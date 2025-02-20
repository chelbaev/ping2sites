import ping3
import pandas as pd

namesSites = ['www.google.com', 'vk.com', 'www.ozon.ru', 'education.yandex.ru', 'xxx.ppp', 'chat.deepseek.com', 
              'docs.google.com', 'calorizator.ru', 'docs.ultralytics.com', 'music.yandex.ru', 'miro.com']
dictionary = {'Domen name': namesSites,
              'ping': []}

for name in namesSites:
    dictionary['ping'].append(round(ping3.ping(name) * 1000))

result = pd.DataFrame(dictionary)
result.to_csv("out.csv")