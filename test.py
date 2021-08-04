from collections import OrderedDict

import girth_puller
import json
import collector
import sys
import matplotlib.pyplot as plt
import time
#messages = collector.get_messages()
messages = []
with open('group_data.json') as f:
    messages = json.load(f)
favorites_received = collector.get_fav_rec()
favorites_given = collector.get_fav_giv()
user_count = collector.get_user_count()
users = collector.get_users()
user_favorites = collector.get_user_fav()
user_time_messages = collector.get_user_time()
name = collector.get_name()
sys.stdout.reconfigure(encoding='utf-8')
new_user_times = {}
for user_id in user_time_messages:
    new_user_times[users[user_id]] = user_time_messages[user_id]
# with open("times.txt", "w") as f:
#     for user_id in user_time_messages:
#         new_user_times[users[user_id]] = user_time_messages[user_id]
#     f.write(str(new_user_times))
user_weekdays = {}
user_hours = {}
user_minutes = {}
time_to_weekday = {0: "monday", 1: "tuesday", 2: "Wednesday",
                   3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
for person in user_time_messages:
    user_weekdays[users[person]] = {}
    user_hours[users[person]] = {}
    user_minutes[users[person]] = {}
    minutes_in_day = []
    hours = user_hours[users[person]]
    minutes = user_minutes[users[person]]
    weekdays = user_weekdays[users[person]]
    for mtime in user_time_messages[person]:
        tempTime = time.gmtime(int(mtime))
        weekday = tempTime.tm_wday
        hour = tempTime.tm_hour
        print()
        minute = tempTime.tm_hour + (tempTime.tm_min % 61)
        if minute not in minutes.keys():
            minutes[minute] = 0
        if hour not in hours.keys():
            hours[hour] = 0
        if time_to_weekday[weekday] not in weekdays.keys():
            weekdays[time_to_weekday[weekday]] = 0
        hours[hour] = hours[hour] + 1
        minutes[minute] = minutes[minute] + 1
        weekdays[time_to_weekday[weekday]
                 ] = weekdays[time_to_weekday[weekday]] + 1
print(user_weekdays['Shawn Verma'])
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
