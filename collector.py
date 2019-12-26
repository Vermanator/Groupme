import json
import girth_puller
from pprint import pprint
resp = girth_puller.get_group()

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

