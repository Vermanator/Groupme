import json
from pprint import pprint
import girth_puller
import json
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
for key in obj['response']['members']:
    users[key['user_id']] = key['nickname']
    print(key['user_id'] + " n " + key['nickname'])
    user_id[key['user_id']] = 0
    user_count[key['user_id']] = 0
    favorites_given[key['user_id']] = 0
    favorites_received[key['user_id']] = 0
    user_favorites[key['user_id']] = {}
    user_favorites_given[key['user_id']] = 0

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

with open('group_data.json') as f:
    data = json.load(f)
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
        size = len(key['favorited_by'])
        favorites_received[key['sender_id']] += size
        # print(key)
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
file_name = "data_" + name + ".txt"
with open(file_name, 'a') as outfile:
    outfile.seek(0)
    outfile.truncate()
    outfile.write("\n" + "Favortes Given" + "\n")
    for key in favorites_given:
        outfile.write(str(users[key].encode('utf-8') + " ".encode("utf-8") +
                      str(favorites_given[key]).encode("utf-8") + "\n".encode("utf-8")))
    outfile.write("\n" + "Favorites Received" + "\n")
    for key in favorites_received:
        outfile.write(str(users[key].encode('utf-8') + " ".encode("utf-8") +
                      str(favorites_received[key]).encode("utf-8") + "\n".encode("utf-8")))
    outfile.write("\n" + "Ratio" + "\n")
    for key in favorites_received:
        if not (user_count[key] == 0):
            outfile.write(str(users[key].encode(
                'utf-8') + " ".encode("utf-8") + str(float(favorites_received[key])/float(user_count[key])).encode("utf-8") + "\n".encode("utf-8")))
    outfile.write("\n" + "Messages sent" + "\n")
    for key in user_count:
        outfile.write(str(users[key].encode('utf-8') +
                      " ".encode("utf-8") + str(user_count[key]).encode("utf-8") + "\n".encode("utf-8")))
    outfile.write("\n" + "Favorites by person" + "\n")
    for key in user_favorites:
        outfile.write(str("\n".encode("utf-8") + "USER: ".encode("utf-8") + users[key].encode('utf-8') + "\n".encode("utf-8")))
        for key2 in user_favorites[key]:
            outfile.write(str(users[key2].encode('utf-8') +
                          " ".encode("utf-8") + str(user_favorites[key][key2]).encode("utf-8") + "\n".encode("utf-8")))
