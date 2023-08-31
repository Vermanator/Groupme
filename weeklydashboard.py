from collections import OrderedDict

import apiEndpoints
import json
from collector import GroupData
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
"""
Users:
Most Messages sent
    messages per user
Most Likes Received
    likes received per user
Most Likes Given
    likes given per user
Earliest Message sent
Latest Message Sent

Groups:
Most active Sters



"""
data = GroupData('Acquaintancesters')
data.process(False)
favorites_received = data.get_fav_rec()
favorites_given = data.get_fav_giv()
user_count = data.get_user_count()
users = data.get_users()
user_favorites = data.get_user_fav()
group_data = data.get_raw_data()
name = data.get_name()
sys.stdout.reconfigure(encoding='utf-8')
new_user_times = {}
# 
last_week = (datetime(2022,12,12) - timedelta(weeks = 1)).timestamp()
timezone_adjust = 14400 # 4 hours from gmt

user_weekdays = {}
user_hours = {}
user_minutes = {}
user_days = {}
time_to_weekday = {0: "monday", 1: "tuesday", 2: "Wednesday",
                   3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

messages = data.get_user_messages_time()
results = {}
start_date = datetime(2022, 9, 8).timestamp()
current_date = datetime.now().timestamp()
# current_week_start = (start_date + timedelta(weeks=j)).timestamp()
current_week_end = start_date.timestamp()

users_messages = [(messages[msg],msg) for msg in messages]
for um in users_messages:
    user_messages = um[0]
    user_combined_msg = ''

    for msg in user_messages:
        if msg[0] and float(msg[1]) > start_date and float(msg[1]) < current_date:
            user_combined_msg = user_combined_msg + msg


