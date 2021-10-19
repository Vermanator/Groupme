from collections import OrderedDict

import girth_puller
import json
from collector import GroupData
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
data = GroupData('Paulie’s on 4th and 14')
#data = GroupData('Pokersters')
messages = data.get_messages()
data.process(False)
print(data.user_count)

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
# last_week = (datetime(2021,8,8) - timedelta(weeks = 1)).timestamp()

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

start_date = datetime(2021, 9, 7)

for j in range(3, 6):
    last_week_user_counts = {}
    user_week_message_count = {}
    user_week_total_likes = {}
    last_week_messages = []
    current_week_start = (start_date + timedelta(weeks=j)).timestamp()
    current_week_end = start_date.timestamp()
    if j < 6:
        current_week_end = (start_date + timedelta(weeks=(j+1))).timestamp()
    for event in group_data:
        if float(event['created_at']) > current_week_start and float(event['created_at']) < current_week_end:

            if not (event['sender_id'] in last_week_user_counts):
                last_week_user_counts[event['sender_id']] = 0
            if not (event['sender_id'] in user_week_message_count):
                user_week_message_count[event['sender_id']] = 0
            if not (event['sender_id'] in user_week_total_likes):
                user_week_total_likes[event['sender_id']] = 0
            last_week_user_counts[event['sender_id']
                                  ] = last_week_user_counts[event['sender_id']] + 1
            user_week_message_count[event['sender_id']
                                    ] = user_week_message_count[event['sender_id']] + 1
            for liker in event['favorited_by']:
                user_week_total_likes[event['sender_id']
                                      ] = user_week_total_likes[event['sender_id']] + 1

    # print([(users[x], last_week_user_counts[x]) for x in last_week_user_counts.keys()])
    user_ranks = {}
    for user in user_week_total_likes:
        # print(data.get_users()[user])
        # print(user_week_total_likes[user])
        # print(user_week_message_count[user])
        # print(user_week_total_likes[user]/user_week_message_count[user])
        user_ranks[data.get_users()[user]] = '{:.2f}'.format(
            round(user_week_total_likes[user]/user_week_message_count[user], 2))
    rankings_sorted = [(x, user_ranks[x]) for x in sorted(
        user_ranks, key=user_ranks.get, reverse=True)]
    # print(rankings_sorted)

    i = 0
    print("-" * 60)
    title = "| Verma Efficieny Index " + "Week " + \
        str(j+1) + " " + str((datetime(2021, 9, 7) + timedelta(weeks=j+1)).date())
    spaces = (60 - len(title)) * " "
    title = title + spaces + "|"
    print(title)
    print("|" + " " * 59 + "|")
    for user in rankings_sorted:
        i = i + 1
        row = "| " + str(i) + ". " + user[0]
        rowLength = len(row)
        sendid = list(data.get_users().keys())[
            list(data.get_users().values()).index(user[0])]
        end_of_row = str(user[1]) + "  " + str(user_week_total_likes[sendid]
                                               ) + " L " + str(user_week_message_count[sendid]) + " M"
        spacesLeft = 40 - rowLength
        spaces = " " * spacesLeft
        row = row + str(spaces) + end_of_row
        endSpacesLeft = 60 - len(row)
        endSpaces = " " * endSpacesLeft
        row = row + str(endSpaces) + "|"
        print(row)
    print("-" * 60)
    print(" ")
    # user_weekdays[users[person]] = {}
    # user_hours[users[person]] = {}
    # user_minutes[users[person]] = {}
    # minutes_in_day = []
    # hours = user_hours[users[person]]
    # minutes = user_minutes[users[person]]
    # weekdays = user_weekdays[users[person]]
    # for mtime in user_time_messages[person]:
    #     if float(mtime) > last_week:
    #         tempTime = time.gmtime(int(mtime))
    #         weekday = tempTime.tm_wday
    #         hour = tempTime.tm_hour
    #         minute = tempTime.tm_hour + (tempTime.tm_min % 61)
    #         if minute not in minutes.keys():
    #             minutes[minute] = 0
    #         if hour not in hours.keys():
    #             hours[hour] = 0
    #         if time_to_weekday[weekday] not in weekdays.keys():
    #             weekdays[time_to_weekday[weekday]] = 0
    #         hours[hour] = hours[hour] + 1
    #         minutes[minute] = minutes[minute] + 1
    #         weekdays[time_to_weekday[weekday]] = weekdays[time_to_weekday[weekday]] + 1

# for uh in user_minutes:
#     orderhours = sorted(user_minutes['Shawn Verma'].items())
#     if len(orderhours) != 0:
#         x, y = zip(*orderhours)
#         #plt.plot(x, y, label=uh)
#         # for i, txt in enumerate(x):
#         #     plt.annotate((x[i], y[i]), (x[i], y[i]))
#         break
# orderhours = sorted(user_hours['Shawn Verma'].items())
# x, y = zip(*orderhours)
# plt.plot(x, y, c='mediumorchid')
# plt.legend()
# plt.show()


# print()
