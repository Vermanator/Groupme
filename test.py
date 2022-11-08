from collections import OrderedDict

import apiEndpoints
import json
from collector import GroupData
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
data = GroupData('Seattlesters')
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
last_week = (datetime(2021,8,8) - timedelta(weeks = 1)).timestamp()

for user_id in user_time_messages:
    new_user_times[users[user_id]] = user_time_messages[user_id]

user_weekdays = {}
user_hours = {}
user_minutes = {}
time_to_weekday = {0: "monday", 1: "tuesday", 2: "Wednesday",
                   3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
# for person in user_time_messages:
#     user_weekdays[users[person]] = {}
#     user_hours[users[person]] = {}
#     user_minutes[users[person]] = {}
#     minutes_in_day = []
#     hours = user_hours[users[person]]
#     minutes = user_minutes[users[person]]
#     weekdays = user_weekdays[users[person]]
#     for mtime in user_time_messages[person]:
#         if float(mtime) > last_week:
#             tempTime = time.gmtime(int(mtime))
#             weekday = tempTime.tm_wday
#             hour = tempTime.tm_hour
#             minute = tempTime.tm_hour + (tempTime.tm_min % 61)
#             if minute not in minutes.keys():
#                 minutes[minute] = 0
#             if hour not in hours.keys():
#                 hours[hour] = 0
#             if time_to_weekday[weekday] not in weekdays.keys():
#                 weekdays[time_to_weekday[weekday]] = 0
#             hours[hour] = hours[hour] + 1
#             minutes[minute] = minutes[minute] + 1
#             weekdays[time_to_weekday[weekday]] = weekdays[time_to_weekday[weekday]] + 1
last_week_user_counts = {}
for event in group_data:
    if float(event['created at']) > last_week:
        if not (key['sender_id'] in last_week_user_counts):
            last_week_user_counts[key['sender_id']] = 0
        last_week_user_counts[key['sender_id']]
    user_weekdays[users[person]] = {}
    user_hours[users[person]] = {}
    user_minutes[users[person]] = {}
    minutes_in_day = []
    hours = user_hours[users[person]]
    minutes = user_minutes[users[person]]
    weekdays = user_weekdays[users[person]]
    for mtime in user_time_messages[person]:
        if float(mtime) > last_week:
            tempTime = time.gmtime(int(mtime))
            weekday = tempTime.tm_wday
            hour = tempTime.tm_hour
            minute = tempTime.tm_hour + (tempTime.tm_min % 61)
            if minute not in minutes.keys():
                minutes[minute] = 0
            if hour not in hours.keys():
                hours[hour] = 0
            if time_to_weekday[weekday] not in weekdays.keys():
                weekdays[time_to_weekday[weekday]] = 0
            hours[hour] = hours[hour] + 1
            minutes[minute] = minutes[minute] + 1
            weekdays[time_to_weekday[weekday]] = weekdays[time_to_weekday[weekday]] + 1

for uh in user_minutes:
    orderhours = sorted(user_minutes['Shawn Verma'].items())
    if len(orderhours) != 0:
        x, y = zip(*orderhours)
        #plt.plot(x, y, label=uh)
        # for i, txt in enumerate(x):
        #     plt.annotate((x[i], y[i]), (x[i], y[i]))
        break
orderhours = sorted(user_hours['Shawn Verma'].items())
x, y = zip(*orderhours)
plt.plot(x, y, c='mediumorchid')
plt.legend()
plt.show()


print()
