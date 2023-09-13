import apiEndpoints
import json
from collections import OrderedDict
from time import strftime, localtime
from collector import GroupData
import sys
# import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from spellchecker import SpellChecker

def spell3(wl):
    wordlist=wl.split()
    spell = SpellChecker()
    return len(list(spell.unknown(wordlist)))

stersGroup = []
every_group_data = []
AcqData = {} # acquaintersters


data = GroupData('Paulie’s on 4th and 14')
data.process(False)
AcqData = data
every_group_data.append(data)
user_total_messages_in_season = {}
user_ratios = {}
user_total_favorites_received_in_season = {}
#initialize stuff


# print(user_total_messages_in_season)
start_date = datetime(2022,9,7)
end_date = datetime(2023,1,2)
debate_day_start = datetime(2022,9,11).timestamp()
debate_day_end = datetime(2022,9,12).timestamp()
start_date_timestamp = start_date.timestamp()
end_date_timestamp = end_date.timestamp()
end_day = datetime(2022,9,7) + timedelta(days=1)
# key is the message, value is the # of times said
copy_pastas = {}
potential_pastas = []
# person -> total content
content_kings = {}
max_likes = {}
message_count_per_day = {}
user_all_combined_messages = {}

debate_day=[]
## DD CP AND LM, debate days, liked messages, and content pilled
#initialize loop
test_flag = False
# print(AcqData.get_users())
weekday_buckets = {}
for i in range(0,7):
    weekday_buckets[i] = 0
for id in AcqData.get_users():
    user_total_messages_in_season[AcqData.get_users()[id]] = 0
    user_ratios[AcqData.get_users()[id]] = 0
    user_total_favorites_received_in_season[AcqData.get_users()[id]] = 0
    content_kings[AcqData.get_users()[id]] = 0
    max_likes[AcqData.get_users()[id]] = []
    user_all_combined_messages[AcqData.get_users()[id]] = ""
#count messages per day
for d in range(1,117):
    curr_start_day = (start_date + timedelta(days=d)).timestamp()
    curr_end_day = (start_date + timedelta(days=(d + 1))).timestamp()
    message_count_per_day[(start_date + timedelta(days=(d + 1))).strftime("%c")] = 0
    for msg in data.get_raw_data():
        if float(msg['created_at']) > curr_start_day and float(msg['created_at']) < curr_end_day:
            message_count_per_day[(start_date + timedelta(days=(d+1))).strftime("%c")] += 1
for msg in data.get_raw_data():
    #debate day
    if float(msg['created_at']) > debate_day_start and float(msg['created_at']) < debate_day_end:
        time = strftime('%I:%M:%S', localtime(int(msg['created_at'])))
        debate_day.append((AcqData.get_users()[msg['sender_id']],msg['text'],time))
    if float(msg['created_at']) > start_date_timestamp and float(msg['created_at']) < end_date_timestamp:
        if msg['text']:
            user_all_combined_messages[AcqData.get_users()[msg['sender_id']]] += msg['text']


        datetime.fromtimestamp(float(msg['created_at'])).weekday()
        weekday_buckets[datetime.fromtimestamp(float(msg['created_at'])).weekday()] += 1
        #most liked
        if len(msg['favorited_by']) == 10:
            likers = [AcqData.get_users()[liker_id] for liker_id in msg['favorited_by']]
            time = strftime('%Y-%m-%d %H:%M:%S', localtime(int(msg['created_at'])))
            max_likes[AcqData.get_users()[msg['sender_id']]].append((likers,msg['text'],time))
            # if not test_flag:
            #     print(msg)
            #     test_flag = True
        if msg['text'] and 'https' in msg['text']:
            content_kings[AcqData.get_users()[msg['sender_id']]] += 1
        # if msg['text'] and len(msg['text']) >= 100:
        #     if msg['text'] not in potential_pastas:
        #         potential_pastas.append(msg['text'])
        #     else:
        #         print("else")
        #         if msg['text'] not in copy_pastas.keys():
        #             copy_pastas[msg['text']] = [1,[]]f
        #             copy_pastas[msg['text']][1].append(AcqData.get_users()[msg['sender_id']])
        #             print("here")
        #         else: 
        #             copy_pastas[msg['text']][0] += 1
        #             copy_pastas[msg['text']][1].append(AcqData.get_users()[msg['sender_id']])

        user_total_messages_in_season[AcqData.get_users()[msg['sender_id']]] += 1
        for liker in msg['favorited_by']:
            user_total_favorites_received_in_season[AcqData.get_users()[msg['sender_id']]] += 1
typos_per_user = {}
for user in user_all_combined_messages.keys():
    typos_per_user[user] = spell3(user_all_combined_messages[user])

for user in user_total_messages_in_season:
    if user in user_total_favorites_received_in_season.keys():
        # print("numbs")
        # print(user_total_messages_in_season[user])
        # print(user_total_favorites_received_in_season[user])
        if user_total_messages_in_season[user] != 0:
            user_ratios[user] = float('%.3f'%(user_total_favorites_received_in_season[user] / user_total_messages_in_season[user]))

# print("USER RATIOS")
ratios_sorted = dict(sorted(user_ratios.items(), key=lambda item: item[1], reverse=True))
# print(ratios_sorted)
# print("content king")
content_kings = dict(sorted(content_kings.items(), key=lambda item: item[1], reverse=True))
# print("most liked most times messages")
# print(max_likes)
max_likes= dict(sorted(max_likes.items(), key=lambda item: item[1], reverse = True))
user_total_messages_in_season= dict(sorted(user_total_messages_in_season.items(), key=lambda item: item[1], reverse = True))
message_count_per_day= dict(sorted(message_count_per_day.items(), key=lambda item: item[1], reverse = True))

typos_ratios = {}
for user in typos_per_user.keys():
    if user_total_messages_in_season[user] > 0:
        typos_ratios[user] = float('%.3f'%(typos_per_user[user] / user_total_messages_in_season[user]))

#print(dict(sorted(typos_per_user.items(), key=lambda item: item[1], reverse = True)))

typos_per_user = dict(sorted(typos_per_user.items(), key=lambda item: item[1], reverse = True))
typos_ratios = dict(sorted(typos_ratios.items(), key=lambda item: item[1], reverse = True))


print(max_likes)
for msg in max_likes:
    print(msg)
print(weekday_buckets)
typos_per_user.pop("temp bot",None)
typos_per_user.pop("Zo",None)
typos_per_user.pop("calendar",None)
typos_per_user.pop("NoName",None)
typos_per_user.pop("system",None)
plt.figure(figsize=(10, 10))
bars = plt.bar(list(typos_per_user.keys()),list(typos_per_user.values()))#, align='edge', width=0.3)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)
ax = plt.gca()
ax.set_xticklabels(list(typos_per_user.keys()), rotation=45)
plt.title(
    "Typos Total 2022",
    fontsize='large',
    loc='left',
    fontweight='bold',
    style='italic',
    family='monospace')
plt.xlabel("Manager")
plt.ylabel("typos")
plt.show()


#print debate datsd
# for msg in debate_day:
#     print(msg)
#print(weekday_buckets)
# ratios_sorted.pop("temp bot",None)
# ratios_sorted.pop("Zo",None)
# ratios_sorted.pop("calendar",None)
# ratios_sorted.pop("NoName",None)
# plt.figure(figsize=(10, 10))
# bars = plt.bar(list(ratios_sorted.keys()),list(ratios_sorted.values()))#, align='edge', width=0.3)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x(), yval + .005, yval)
# ax = plt.gca()
# ax.set_xticklabels(list(ratios_sorted.keys()), rotation=45)
# plt.title(
#     "Verma Efficieny Index 2022",
#     fontsize='large',
#     loc='left',
#     fontweight='bold',
#     style='italic',
#     family='monospace')
# plt.xlabel("Manager")
# plt.ylabel("Likes / Messages")
# plt.show()

# content_kings.pop("temp bot",None)
# content_kings.pop("Zo",None)
# content_kings.pop("calendar",None)
# content_kings.pop("NoName",None)
# plt.figure(figsize=(10, 10))
# bars = plt.bar(list(content_kings.keys()),list(content_kings.values()))#, align='edge', width=0.3)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x(), yval + .005, yval)
# ax = plt.gca()
# ax.set_xticklabels(list(content_kings.keys()), rotation=45)
# plt.title(
#     "Content Kings",
#     fontsize='large',
#     loc='left',
#     fontweight='bold',
#     style='italic',
#     family='monospace')
# plt.xlabel("Manager")
# plt.ylabel("How Content pilled are you")
# plt.show()

# keys_to_pop = []
# for x in max_likes:
#     if len(max_likes[x]) == 0:
#         keys_to_pop.append(x)
# for x in keys_to_pop:
#     max_likes.pop(x,None)
# plt.figure(figsize=(10, 10))
# lengths_max_likes = []
# print(max_likes)
# for x in max_likes.values():
#     print(len(x))
#     lengths_max_likes.append(len(x))
# #print([len(x) for x in max_likes.values()])
# bars = plt.bar(list(max_likes.keys()),list([len(x) for x in max_likes.values()]))#, align='edge', width=0.3)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x(), yval + .025, yval)
# ax = plt.gca()
# ax.set_xticklabels(list(max_likes.keys()), rotation=45)
# plt.title(
#     "the 10 Likes Club",
#     fontsize='large',
#     loc='left',
#     fontweight='bold',
#     style='italic',
#     family='monospace')
# plt.xlabel("Manager")
# plt.ylabel("Number of decaMessages")
# plt.show()

# user_total_messages_in_season.pop("temp bot",None)
# user_total_messages_in_season.pop("Zo",None)
# user_total_messages_in_season.pop("calendar",None)
# user_total_messages_in_season.pop("NoName",None)
# plt.figure(figsize=(10, 10))
# bars = plt.bar(list(user_total_messages_in_season.keys()),list(user_total_messages_in_season.values()))#, align='edge', width=0.3)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x(), yval + .005, yval)
# ax = plt.gca()
# ax.set_xticklabels(list(user_total_messages_in_season.keys()), rotation=60)
# plt.title(
#     "Total Messages Sent",
#     fontsize='large',
#     loc='left',
#     fontweight='bold',
#     style='italic',
#     family='monospace')
# plt.xlabel("Manager")
# plt.ylabel("Total Messages")
# plt.show()