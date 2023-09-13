import json
import apiEndpoints
import sys
from pprint import pprint


class GroupData:

    def __init__(self, name):  
        self.name = name
        self.favorites_received = {}
        self.favorites_given = {}
        self.user_count = {}
        self.users = {}
        self.user_favorites = {}
        self.user_time_messages = {}
        self.user_messages = {}
        self.messages = []
        self.user_favorites_given = {}
        self.group_data = []
        self.group = {}
    def process(self,pullMessages):
        GROUP = self.name
        resp = apiEndpoints.get_group(GROUP)
        self.group = resp.json()
        if pullMessages:
            apiEndpoints.collect_group_messages_to_file(apiEndpoints.get_group_id(GROUP),GROUP)
        group = resp.json()
        self.users = {}
        user_id = {}
        self.user_count = {}
        self.favorites_given = {}
        self.favorites_received = {}
        self.user_favorites = {}
        self.user_favorites_given = {}
        self.user_time_messages = {}
        self.user_messages = {}
        for key in group['response']['members']:
            self.users[key['user_id']] = key['nickname']
            #print(key['user_id'] + " n " + key['nickname'])
            user_id[key['user_id']] = 0
            self.user_count[key['user_id']] = 0
            self.favorites_given[key['user_id']] = 0
            self.favorites_received[key['user_id']] = 0
            self.user_favorites[key['user_id']] = {}
            self.user_favorites_given[key['user_id']] = 0
            self.user_time_messages[key['user_id']] = []
            self.user_messages[key['user_id']] = []


        self.user_favorites['system'] = {}
        self.user_favorites['663430'] = {}
        self.user_favorites['46185459'] = {}
        self.user_favorites['calendar'] = {}

        self.user_favorites_given['system'] = {}
        self.user_favorites_given['663430'] = {}
        self.user_favorites_given['46185459'] = {}
        self.user_favorites_given['calendar'] = {}

        self.users['system'] = 'system'
        self.users['663430'] = 'temp bot'
        self.users['46185459'] = 'Zo'
        self.users['calendar'] = 'calendar'

        self.user_count['system'] = 0
        self.user_count['663430'] = 0
        self.user_count['46185459'] = 0
        self.user_count['calendar'] = 0

        self.user_time_messages['system'] = []
        self.user_time_messages['663430'] = []
        self.user_time_messages['46185459'] = []
        self.user_time_messages['calendar'] = []

        self.user_messages['system'] = []
        self.user_messages['663430'] = []
        self.user_messages['46185459'] = []
        self.user_messages['calendar'] = []

        self.favorites_given['system'] = 0
        self.favorites_given['663430'] = 0
        self.favorites_given['46185459'] = 0
        self.favorites_given['calendar'] = 0

        self.favorites_received['system'] = 0
        self.favorites_received['calendar'] = 0
        self.favorites_received['46185459'] = 0
        self.favorites_received['663430'] = 0

        for key in self.user_favorites:
            self.user_favorites[key] = self.user_favorites_given.copy()
        #print("hi")
        sys.stdout.reconfigure(encoding='utf-8')
        data = {}
        with open('./group_data/' + self.name + '.json') as f:
            data = json.load(f)
        for obj in data:
            for key in obj['response']['messages']:
                if not (key['sender_id'] in self.favorites_received):
                    self.favorites_received[key['sender_id']] = 0
                if not (key['sender_id'] in self.favorites_given):
                    self.favorites_given[key['sender_id']] = 0
                if not (key['sender_id'] in self.user_count):
                    self.user_count[key['sender_id']] = 0
                if not (key['sender_id'] in self.users):
                    self.users[key['sender_id']] = key['name']
                if not (key['sender_id'] in self.user_favorites):
                    self.user_favorites[key['sender_id']] = {}
                if not (key['sender_id']) in self.user_time_messages:
                    self.user_time_messages[key['sender_id']] = []
                if not (key['sender_id']) in self.user_messages:
                    self.user_messages[key['sender_id']] = []
                size = len(key['favorited_by'])
                self.favorites_received[key['sender_id']] += size
                # print(key['text'])
                self.group_data.append(key)
                if key['system'] == False:
                    self.messages.append(key['text'])
                # print(key['sender_id'])
                for key2 in key['favorited_by']:
                    if not (key2 in self.favorites_received):
                        self.favorites_received[key2] = 0
                    if not (key2 in self.favorites_given):
                        self.favorites_given[key2] = 0
                    if not (key2 in self.user_count):
                        self.user_count[key2] = 0
                    if not (key2 in self.users):
                        self.users[key2] = 'NoName'
                    if key2 in self.favorites_given:
                        self.favorites_given[key2] += 1
                    if not (key2 in self.user_favorites[key['sender_id']]):
                        self.user_favorites[key['sender_id']][key2] = 0
                    self.user_favorites[key['sender_id']][key2] += 1
                self.user_count[key['sender_id']] += 1
                self.user_time_messages[key['sender_id']].append(key['created_at'])
                msg_time = (key['text'],key['created_at'])
                self.user_messages[key['sender_id']].append(msg_time)
    def get_group(self):
        return self.group
    def get_messages(self):
        return self.messages
    def get_fav_rec(self):
        return self.favorites_received
    def get_fav_giv(self):
        return self.favorites_given
    def get_user_count(self):
        return self.user_count
    def get_users(self):
        return self.users
    def get_user_fav(self):
        return self.user_favorites
    def get_user_time(self):
        return self.user_time_messages
    def get_user_messages_time(self):
        return self.user_messages
    def get_name(self):
        return self.name
    def get_raw_data(self):
        return self.group_data
    def get_name_from_id(self,id):
        if id in self.users.keys():
            return self.users[id]
        else:
            return "Noname"
    def get_id_from_name(self,name):
        for id in self.users:
            if name == self.users[id]:
                return id
    def get_names_from_ids(self,ids):
        return [self.users[id] for id in ids]
    def get_ratio(self):
        user_ratios = {}
        for user in self.users:
            user_ratios[user] = self.favorites_received[user]/self.user_count[user]
    # def initialize_dict_with_all_users(user_dict):
    #     for user in self.users:
    #         user_dict = 

