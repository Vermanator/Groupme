from collections import OrderedDict

import apiEndpoints
import json
from collector import GroupData
import sys
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
data = GroupData('Pokersters')
messages = data.get_messages()
data.process(False)
favorites_received = data.get_fav_rec()
favorites_given = data.get_fav_giv()
user_count = data.get_user_count()
users = data.get_users()
user_favorites = data.get_user_fav()
user_time_messages = data.get_user_time()
group_data = data.get_raw_data()
name = data.get_name()
sys.stdout.reconfigure(encoding='utf-8')
new_user_times = {}

start_date = datetime(2023,6,5)

start_date_timestamp = start_date.timestamp()
for msg in data.get_raw_data():
    if float(msg['created_at']) > start_date_timestamp:
        if msg['text'] and 'created event' in msg['text'] and 'Zach' in msg['text']:
            print(msg['text'])
        if msg['text'] and 'Wrath' in msg['text'] and 'created event' in msg['text']:
            print(msg['text'])
        # if msg['sender_id'] == 'system':
        #     print(msg)