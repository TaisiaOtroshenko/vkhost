import requests
import time
import json
from vk_tokens import *


#выбор сообщений

file_ids = json.load(open('missing_ids.json','r', encoding='utf-8'))
command_count = 25 # 25 максимум
call_generate = []

for i in range (len(file_ids)):
    #добавление команд в список
    print(file_ids[i], ',', end='')
    call_generate.append( 'API.messages.restore({"message_id":' + str(file_ids[i]) +'})')
    if (len(call_generate)==command_count):
        call_generate = ','.join(call_generate)
        code = 'return ['+ call_generate +'];'

        r = requests.post(f'https://api.vk.com/method/execute?code={code}&access_token={access_token_me}&v=5.199').json() 
        time.sleep(0.35) #слишком часто спрашивать нельзя, так что подождем
        print('\n', r['response'])
        call_generate = []
    

call_generate = ','.join(call_generate)
code = 'return ['+ call_generate +'];'

r = requests.post(f'https://api.vk.com/method/execute?code={code}&access_token={access_token_me}&v=5.199').json() 
print(r['response'])


