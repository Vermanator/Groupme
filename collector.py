import json
import girth_puller
import sys
from pprint import pprint
GROUP = 'Pokersters'
resp = girth_puller.get_group(GROUP)
# girth_puller.collect_group_messages_to_file(girth_puller.get_group_id(GROUP))
obj = resp.json()
name = obj['response']['name']
users = {}
user_id = {}
user_count = {}
favorites_given = {}
favorites_received = {}
user_favorites = {}
user_favorites_given = {}
user_time_messages = {}
for key in obj['response']['members']:
    users[key['user_id']] = key['nickname']
    print(key['user_id'] + " n " + key['nickname'])
    user_id[key['user_id']] = 0
    user_count[key['user_id']] = 0
    favorites_given[key['user_id']] = 0
    favorites_received[key['user_id']] = 0
    user_favorites[key['user_id']] = {}
    user_favorites_given[key['user_id']] = 0
    user_time_messages[key['user_id']] = []


user_favorites['system'] = {}
user_favorites['663430'] = {}
user_favorites['46185459'] = {}
user_favorites['calendar'] = {}

user_favorites_given['system'] = {}
user_favorites_given['663430'] = {}
user_favorites_given['46185459'] = {}
user_favorites_given['calendar'] = {}

users['system'] = 'system'
users['663430'] = 'temp bot'
users['46185459'] = 'Zo'
users['calendar'] = 'calendar'

user_count['system'] = 0
user_count['663430'] = 0
user_count['46185459'] = 0
user_count['calendar'] = 0

user_time_messages['system'] = []
user_time_messages['663430'] = []
user_time_messages['46185459'] = []
user_time_messages['calendar'] = []

favorites_given['system'] = 0
favorites_given['663430'] = 0
favorites_given['46185459'] = 0
favorites_given['calendar'] = 0

favorites_received['system'] = 0
favorites_received['calendar'] = 0
favorites_received['46185459'] = 0
favorites_received['663430'] = 0

for key in user_favorites:
    user_favorites[key] = user_favorites_given.copy()
print("hi")
sys.stdout.reconfigure(encoding='utf-8')

with open('group_data.json') as f:
    data = json.load(f)
messages = []
for obj in data:
    for key in obj['response']['messages']:
        if not (key['sender_id'] in favorites_received):
            favorites_received[key['sender_id']] = 0
        if not (key['sender_id'] in favorites_given):
            favorites_given[key['sender_id']] = 0
        if not (key['sender_id'] in user_count):
            user_count[key['sender_id']] = 0
        if not (key['sender_id'] in users):
            users[key['sender_id']] = key['name']
        if not (key['sender_id'] in user_favorites):
            user_favorites[key['sender_id']] = {}
        if not (key['sender_id']) in user_time_messages:
            user_time_messages[key['sender_id']] = []
        size = len(key['favorited_by'])
        favorites_received[key['sender_id']] += size
        # print(key['text'])
        if key['system'] == False:
            messages.append(key['text'])
        # print(key['sender_id'])
        for key2 in key['favorited_by']:
            if not (key2 in favorites_received):
                favorites_received[key2] = 0
            if not (key2 in favorites_given):
                favorites_given[key2] = 0
            if not (key2 in user_count):
                user_count[key2] = 0
            if not (key2 in users):
                users[key2] = 'NoName'
            if key2 in favorites_given:
                favorites_given[key2] += 1
            if not (key2 in user_favorites[key['sender_id']]):
                user_favorites[key['sender_id']][key2] = 0
            user_favorites[key['sender_id']][key2] += 1
        user_count[key['sender_id']] += 1
        user_time_messages[key['sender_id']].append(key['created_at'])

def get_messages():
    return messages
def get_fav_rec():
    return favorites_received
def get_fav_giv():
    return favorites_given
def get_user_count():
    return user_count
def get_users():
    return users
def get_user_fav():
    return user_favorites
def get_user_time():
    return user_time_messages
def get_name():
    return name

