import requests
import json
from vk_tokens import *


#выбор сообщений
id_current = 1253100
count = 1 # 100 максимум
command_count = 2 # 9 максимум

ids = []
for j in range(count):
    ids.append(str(id_current-j))
    ids = ','.join(ids)

code = 'return {API.messages.getById({"message_ids":"'+ ids +'"}).items@.id};'
print(code)

r = requests.post(f'https://api.vk.com/method/execute?code={code}&access_token={access_token_me}&v=5.199').json() 
print(r)