import requests
import json
from vk_tokens import *
# работающая версия параметра "code" из web-редактора "return[API.messages.getById({"message_ids": "544117,544116","extended":"1"}),API.messages.getById({"message_ids": 544116}).items];"

#сохранение истории сообщений используя vkscripts
id_current = 1253100
count = 100 # 100 максимум
command_count = 10 # 9 максимум
command = []
for i in range(command_count):
    id_first = id_current-i*count
    id_last = id_first - count
    #добавление команд в список
    command.append( 'var cur = ' + id_first + '; var arr = ""; while (cur != ' + id_last + ') { arr = arr+cur+","; cur = cur - 1;} return API.messages.getById({"message_ids":"arr"}).items@.id;')
command = ','.join(command)
print(command)

r = requests.post(f'https://api.vk.com/method/execute?code=return[{command}];&access_token={access_token_me}&v=5.199')
print()


#запись в .json
'''
#в этом варианте либо убрать скобочки, либо добавить между ними запятую
for i in range(command_count):
    json.dump(r['response'][i]['items'],open('scrpt_messages.json','a+', encoding='utf-8'))
    
    if ('profiles' in r['response'][i]):
        json.dump(r['response'][i]['profiles'],open('scrpt_profiles.json','a+', encoding='utf-8'))

'''
'''
items = []
profiles = []
for i in range(command_count):
    if ('items' in r['response'][i]):
        for x in r['response'][i]['items']:
            items.append(x)
    if ('profiles' in r['response'][i]):
        for x in r['response'][i]['profiles']:
            profiles.append(x)
            
json.dump(items,open('scrpt_messages.json','w', encoding='utf-8'))
json.dump(profiles,open('scrpt_profiles.json','w', encoding='utf-8'))
'''
