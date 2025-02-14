import requests
from vk_tokens import *

#сохранение истории сообщений в читабельном виде
#предыдущие 100 сообщений начиная с id_current записываются в txt файл в формате id, from, peer, text 
#при повторном запуске уменьшите id_current на 100 и они добавятся в конец файла
#таким образом запись ведется в убывании id
#дополнительно в консоль выводится количество отсутствующих сообщений в истории и помечаются удаленные сообщения 

id_current = 1100000
count = 100
#генерация массива ids
ids = []
for j in range(count):
    ids.append(str(id_current-j))
ids = ','.join(ids)
print(ids)

#обращение к API
r = requests.post(f'https://api.vk.com/method/messages.getById?message_ids={ids}&extended=1&access_token={access_token_me}&v=5.199').json() 
#print(r)

#отмечение количества отсутствующих сообщений
have_deleted = count - r['response']['count']
print(r, have_deleted)

#запись в .txt
f_history = open("history.txt", "a+", encoding="utf8")
for i in range(0,r['response']['count']):
    #отмечение удаленных сообщений
    if ('deleted' in r['response']['items'][i]): 
        f_history.write('DELETED ')
        print('DELETED')
    f_history.write(str(r['response']['items'][i]['id']) +'\t'+ str(r['response']['items'][i]['from_id']) + '\t'+ str(r['response']['items'][i]['peer_id']) + '\t' +str(r['response']['items'][i]['text'])+ '\n')
f_history.close()
