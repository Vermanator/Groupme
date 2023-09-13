from collections import OrderedDict

import apiEndpoints
import json
from collector import GroupData
import sys
import matplotlib.pyplot as plt
import time
from cycler import cycler
from datetime import datetime, timedelta
def merge_two_dicts(x, y):
    yks = y.keys()
    for k in yks:
        if k not in x.keys():
            x[k] = y[k]
        else:
            x[k] = x[k] + y[k]
    return x
resp = apiEndpoints.get_groups()
obj = resp.json()
stersGroup = []
count = 0
users = {}
user_time_messages = {}
# for group in obj['response']:
#     if 'sters' in group['name']:
#         count = count + 1
#         # stersGroup.append(group['name'])
#         data = GroupData(group['name'])
#         data.process(False)
#         if data.get_raw_data()[-1]['created_at'] < 1547000000:
#             print(group['name'] + " 2018") 
        
#         user_time_messages = merge_two_dicts(user_time_messages,data.get_user_time() )
# print(len(user_time_messages['30072237']))
#messages = collector.get_messages()
# with open('aggregate_sters.json', 'a') as outfile:
#     outfile.seek(0)
#     outfile.truncate()
#     json.dump(user_time_messages, outfile)
# data = {}
with open('aggregate_sters.json') as f:
    user_time_messages = json.load(f)
data = GroupData('Acquaintancesters')
plt.style.use('dark_background')
data.process(False)
# favorites_received = data.get_fav_rec()
# favorites_given = data.get_fav_giv()
# user_count = data.get_user_count()
users = data.get_users()
user_favorites = data.get_user_fav()
group_data = data.get_raw_data()
name = data.get_name()
sys.stdout.reconfigure(encoding='utf-8')
new_user_times = {}
# 
last_week = (datetime(2022,12,12) - timedelta(weeks = 1)).timestamp()
timezone_adjust = 14400 # 4 hours from gmt

# for user_id in user_time_messages:
#     new_user_times[users[user_id]] = user_time_messages[user_id]

user_weekdays = {}
user_hours = {}
user_minutes = {}
user_days = {}
time_to_weekday = {0: "monday", 1: "tuesday", 2: "Wednesday",
                   3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
my_colors = ['steelblue', 'seagreen','darkviolet','lime','rosybrown','gold','dimgrey','aqua','violet','red','silver','orange','hotpink']
custom_cycler = cycler(color=my_colors)
fig, ax = plt.subplots()
ax.set_prop_cycle(custom_cycler)                   
ax.set_title('Messages per Weekday by person in 2019')
year_count = 0
for person in users.keys():
    user_weekdays[users[person]] = {}
    user_hours[users[person]] = {}
    user_minutes[users[person]] = {}
    user_days[users[person]] = {}
    minutes_in_day = []
    hours = user_hours[users[person]]
    minutes = user_minutes[users[person]]
    weekdays = user_weekdays[users[person]]
    days = user_days[users[person]]
    for i in range (366):  #initialize all buckets
        days[i + 1] = 0
    if person not in user_time_messages.keys():
        continue
    for mtime in user_time_messages[person]:
    # if float(mtime) > last_week:
        tempTime = time.gmtime(int(mtime - timezone_adjust))
        weekday = tempTime.tm_wday
        hour = tempTime.tm_hour
        # print(tempTime.tm_year)
        if tempTime.tm_year not in (2019,1000):
            # print('test')
            continue
        else:
            year_count = year_count + 1
        day = tempTime.tm_yday
        # print(mtime)
        # print(tempTime.tm_hour)
        # print(tempTime.tm_min)
        # print(tempTime.tm_yday)
        # print((tempTime.tm_min % 61))
        # break
        minute = tempTime.tm_hour * 60 + (tempTime.tm_min % 61)
        if minute not in minutes.keys():
            minutes[minute] = 0
        if hour not in hours.keys():
            hours[hour] = 0
        if time_to_weekday[weekday] not in weekdays.keys():
            weekdays[time_to_weekday[weekday]] = 0
        hours[hour] = hours[hour] + 1
        minutes[minute] = minutes[minute] + 1
        days[day] = days[day] + 1
        weekdays[time_to_weekday[weekday]] = weekdays[time_to_weekday[weekday]] + 1
print(year_count)
#last_week_user_counts = {}
# for event in group_data:
#     if float(event['created_at']) > last_week:
        
#         if not (event['sender_id'] in last_week_user_counts):
#             last_week_user_counts[event['sender_id']] = 0
#         last_week_user_counts[event['sender_id']] = last_week_user_counts[event['sender_id']] + 1
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
#print([(users[x], last_week_user_counts[x]) for x in last_week_user_counts.keys()])
# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])# main axes

# ax.set_xlabel('Months')
# ax.set_title('messages per month')
# ax.set_xticks([0,31,59,90,121,152,182,212,243,273,304,334])
# ax.set_xticklabels(['January','February','March','April','May','June','July','August','September','October','November','December'])


for uh in user_days:
    orderhours = sorted(user_weekdays[uh].items(), key = lambda a  : list(time_to_weekday.keys())[list(time_to_weekday.values()).index(a[0])])
    if len(orderhours) != 0:
        x, y = zip(*orderhours)
        sory = sorted(y)
        # orderhours.sort(key = lambda a: a[1])
        # print(orderhours)
        ax.plot(x, y, label=uh)
        
        # for i, txt in enumerate(x):
        #     plt.annotate((x[i], y[i]), (x[i], y[i]))
        
# orderhours = sorted(user_hours['Shawn Verma'].items())
# x, y = zip(*orderhours)
# plt.plot(x, y, c='mediumorchid')
# plt.title('Messages per Weekday by person in 2019')

plt.legend()
plt.show()
print()

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


