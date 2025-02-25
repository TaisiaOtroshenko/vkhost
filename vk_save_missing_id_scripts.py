import requests
import json
import time
from vk_tokens import *

# сохранение истории сообщений используя vkscripts
# перед запуском проверить, что при первом запуске в файле missing_ids.json лежит '[]' или массив ids
# при повторном запуске уменьшить id_current на 5000. именно столько обрабатывается за раз
id_current = 100000
count = 100 # 100 максимум
command_count = 5 # 5 максимум
missing_ids = []

def get_missing_ids(id_current, count, command_count, missing_ids):

    ids_generate = []
    call_generate = []
    arr_name = ['arr'+str(i) for i in range (0,command_count)]
    for i in range(command_count):
        id_first = id_current-i*count
        id_last = id_first - count
        #добавление команд в список
        ids_generate.append( 'var cur = ' + str(id_first) + '; var ' + arr_name[i] +' = ""; while (cur != ' + str(id_last) + ') { ' + arr_name[i] +' = ' + arr_name[i] +'+cur+","; cur = cur - 1;} ')
        call_generate.append( 'API.messages.getById({"message_ids":' + arr_name[i] +'}).items@.id')
    

    ids_generate = ''.join(ids_generate)
    call_generate = ','.join(call_generate)
    code_generate = f'{ids_generate}return[{call_generate}];' #склеиваем генерацию массивов и запросов
    #print(code_generate) #проверяем что мы спрашиваем
    code_generate = code_generate.replace('+','%2b') #ставим корректные плюсы для интернетной ссылки

    r = requests.post(f'https://api.vk.com/method/execute?code={code_generate}&access_token={access_token_me}&v=5.199').json()
    #print(r)

    #объединение полученных ids в один массив
    response_ids = []
    for i in range(command_count):
        for x in r['response']:
            response_ids = response_ids + x

    #выбор отстутсвующих и добавление их в массив missing
    for i in range(command_count*count):
        if not(id_current-i in response_ids):
            missing_ids.append(id_current-i)

for i in range (10):
    get_missing_ids(id_current, count, command_count, missing_ids)
    id_current = id_current - (command_count*count)
    print (missing_ids, '\n')
    time.sleep(0.35) #слишком часто спрашивать нельзя, так что подождем


#добавление новых ids в файл
print (missing_ids, '\n')
file_ids = json.load(open('missing_ids.json','r', encoding='utf-8'))
file_ids = file_ids + missing_ids
json.dump(file_ids,open('missing_ids.json','w', encoding='utf-8'))
