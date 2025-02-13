import requests
import datetime
import json
from vk_tokens import *

# найти информацию по друзьям
'''
friends = requests.post(f'https://api.vk.com/method/friends.get?user_id={id_me}&count=10&access_token={access_token}&v=5.199') 

print (friends.json()['response']['items'])

for id_friend in friends.json()['response']['items']:
    response = requests.post(f'https://api.vk.com/method/users.get?user_ids={id_friend}&fields=bdate&access_token={access_token_me}&v=5.199') 
    print (response.json())
'''
#вывод инф о друге
#print( requests.post(f'https://api.vk.com/method/friends.get?user_id={id_me}&access_token={access_token_me}&v=5.199') )

#вывод последних бесед
#print( requests.post(f'https://api.vk.com/method/messages.getConversations?offset=0&count=1&extended=1&access_token={access_token_me}&v=5.199').json() )
#print( requests.post(f'https://api.vk.com/method/messages.getConversationsById?peer_ids=485275609&extended=1&access_token={access_token_me}&v=5.199').json() )

#вывод сообщений в диалоге
#print( requests.post(f'https://api.vk.com/method/messages.getHistory?user_id={id_me}&offset=400&count=200&access_token={access_token_me}&v=5.199').json() )

#возврат сообщения
#print( requests.post(f'https://api.vk.com/method/messages.getById?message_ids={1253041}&extended=1&access_token={access_token_me}&v=5.199').json() )
#print( requests.post(f'https://api.vk.com/method/messages.getById?message_ids=1253582,1253581,1253580,1253579,1253578&extended=1&access_token={access_token_me}&v=5.199').json() )

#восстановление и удаление
#print( requests.post(f'https://api.vk.com/method/messages.restore?message_id=543825&access_token={access_token_me}&v=5.199').json() )
'''
print( requests.post(f'https://api.vk.com/method/messages.getById?message_ids=493762&extended=1&access_token={access_token_me}&v=5.199').json() )
print( requests.post(f'https://api.vk.com/method/messages.delete?message_ids=493762&access_token={access_token_me}&v=5.199').json() )
'''



