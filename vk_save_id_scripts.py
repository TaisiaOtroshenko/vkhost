import requests
import json
from vk_tokens import *
# работающая версия параметра "code" из web-редактора 
    # "return[API.messages.getById({"message_ids": "544117,544116","extended":"1"}),API.messages.getById({"message_ids": 544116}).items];"
    # "var cur = '1253100'; var arr = ""; while (cur != '1253000') { arr = arr+cur+","; cur = cur - 1;} return API.messages.getById({"message_ids":arr}).items@.id;"
    # "var cur = 125000; var arr0 = ""; while (cur != 124900) { arr0 = arr0+cur+","; cur = cur - 1;} var cur = 124900; var arr1 = ""; while (cur != 124800) { arr1 = arr1+cur+","; cur = cur - 1;}return[arr0, arr1];"
# сохранение истории сообщений используя vkscripts
id_current = 125000
count = 100 # 100 максимум
command_count = 2 # 9 максимум


ids_generate = []
call_generate = []
arr_name = ['arr'+str(i) for i in range (0,command_count)]
for i in range(command_count):
    id_first = id_current-i*count
    id_last = id_first - count
    #добавление команд в список
    ids_generate.append( 'var cur = ' + str(id_first) + '; var ' + arr_name[i] +' = ""; while (cur != ' + str(id_last) + ') { ' + arr_name[i] +' = ' + arr_name[i] +'+cur+","; cur = cur - 1;}')
    call_generate.append( 'API.messages.getById({"message_ids":' + arr_name[i] +'}).items@.id')
   

ids_generate = ''.join(ids_generate)
call_generate = ','.join(call_generate)

#это теоретически правильный запрос
#r = requests.post(f'https://api.vk.com/method/execute?code={ids_generate}return[{call_generate}];&access_token={access_token_me}&v=5.199').json()

#это я запрос тестовый пытаюсь пытаюсь сделать, а оно ошибку дает
r = requests.post('https://api.vk.com/method/execute?code="var cur = 125000; var arr0 = ""; while (cur != 124900) { arr0 = arr0+cur+","; cur = cur - 1;} var cur = 124900; var arr1 = ""; while (cur != 124800) { arr1 = arr1+cur+","; cur = cur - 1;}return[arr0, arr1];"'+ f'&access_token={access_token_me}&v=5.199').json()
print('\n', r)



#запись в .json

'''
items = []
for i in range(command_count):
    for x in r['response'][i]:
        items.append(x)
            
json.dump(items,open('scrpt_messages.json','w', encoding='utf-8'))
'''
