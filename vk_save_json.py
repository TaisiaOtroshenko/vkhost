import requests
import json
import time
from vk_tokens import *

#сохранение истории сообщений в полном виде
#сохраняет в порядке убывания id от id_current
# :)    не останавливается

id_current = 544000
count = 100

while True:
    #генерация массива ids
    ids = []
    for j in range(count):
        ids.append(str(id_current-j))
    ids = ','.join(ids)
    print(ids)

    #обращение к API
    r = requests.post(f'https://api.vk.com/method/messages.getById?message_ids={ids}&extended=1&access_token={access_token_me}&v=5.199').json() 
    if ('error' in r):
        print (id_current)
        print (r)
        break
        
    #запись в .json
    json.dump(r['response']['items'],open('history.json','a+', encoding='utf-8'))
    if ('profiles' in r['response']):
        json.dump(r['response']['profiles'],open('authors.json','a+', encoding='utf-8'))
    
    id_current = id_current - 100
    time.sleep(0.35) #слишком часто спрашивать нельзя, так что подождем
    
