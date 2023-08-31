import apiEndpoints
import json
from collections import OrderedDict
from time import strftime, localtime

from collector import GroupData
import sys
# import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
# 
# data.process(True)
# print(data.user_count)
def collect_data_to_file(data, name):
    with open('./trivia_data/' + name + '.json', 'a') as outfile:
        outfile.seek(0)
        outfile.truncate()
        json.dump(data, outfile)


resp = apiEndpoints.get_groups()
obj = resp.json()
stersGroup = []
every_group_data = []
AcqData = {} # acquaintersters
count = 0
#for group in obj['response']:
    #print(group['name'])
#     if 'sters' in group['name']:
#         count = count + 1
#         print(group['name'])
#         data = GroupData('Paulie\'s on 4th an 14')
#         data.process(False)
#         if data.get_name() == 'Paulie\'s on 4th and 14':
#             AcqData = data
#         every_group_data.append(data)
#         print(group['name'] + "processed")

#         print(group['name'])
#         data = GroupData(group['name'])
#         data.process(False)
#         if data.get_name() == 'Paulie\'s on 4th and 14':
#             AcqData = data
#         every_group_data.append(data)
#         print(group['name'] + "processed")
#         break

print(count)

data = GroupData('Paulie’s on 4th and 14')
data.process(False)
every_group_data.append(data)
AcqData = data
#gather all messages and see most ever

Process = True
print(every_group_data)
# if Process:
#     collect_data_to_file(every_group_data,'user_total_messages')
# else:
#     with open('./trivia_data/user_total_messages') as outfile:
#         every_group_data = json.load(outfile)
user_total_message = {}
user_ratios = {}
user_total_favorites_received = {}
for id in AcqData.get_users():
    user_total_message[AcqData.get_users()[id]] = 0
    user_ratios[AcqData.get_users()[id]] = 0
    user_total_favorites_received[AcqData.get_users()[id]] = 0
# print(user_total_message)
#GET TOTAL MESSAGES
for data in every_group_data:
    print(data)
    for user in user_total_message.keys():
        #print(user)
        if data.get_id_from_name(user) in data.get_user_count().keys():
            # print("COUNT")
            # print(data.get_user_count()[data.get_id_from_name(user)])
            user_total_message[user] = user_total_message[user] + data.get_user_count()[data.get_id_from_name(user)] 
    print(data.get_name())
print("USER TOTAL MESSAGES")
print(dict(sorted(user_total_message.items(), key=lambda item: item[1])))
#GET TOTALs favorites received
for data in every_group_data:
    for user in user_total_favorites_received.keys():
        if data.get_id_from_name(user) in data.get_user_count().keys() and user in user_total_favorites_received.keys():
            user_total_favorites_received[user] = user_total_favorites_received[user] + data.get_fav_rec()[data.get_id_from_name(user)]
    # print(data.get_name())
# for data in every_group_data:
#     for user in user_total_favorites_received.keys():

#TOTAL MESSAGES BY GROUP
print("TOTAL MESSAGES BY GROUP")
group_totals = {}
for data in every_group_data:
        group_totals[data.get_name()] = len(data.get_messages())
print(group_totals)
most_acqs_groups = []
acqUsers = AcqData.get_users()
print("GROUPS WITH ALL STERS IN IT")
#TODO VERIFY WITH LARGE AND MORE GROUPS THAT 11 is right number
for data in every_group_data:
    count = 0
    #print(data.get_group())
    for user in data.get_users():
        
        if user in acqUsers and user != 'calendar' and user != 'system' and user != '46185459' and user != '663430':
            count = count + 1
            print(data.get_users()[user])
    if count > 11:
        print("above")
        most_acqs_groups.append(data.get_name())
print(most_acqs_groups)

for user in user_total_message:
    if user in user_total_favorites_received.keys():
        # print("numbs")
        # print(user_total_message[user])
        # print(user_total_favorites_received[user])
        if user_total_message[user] != 0:
            user_ratios[user] = user_total_favorites_received[user] / user_total_message[user]
print("USER RATIOS")
print(dict(sorted(user_ratios.items(), key=lambda item: item[1])))

#LONGEST MESSAGES, who, message , liked
longest_message_length = 0
longest_message_set = []
longest_message = ''
longest_message_data = ()
longest_message_like_count = 0
# previous_mes = ''
# previous_holder = ''
# post_mes = ''
# post = False
print("LONGEST MESSAGE")
for data in every_group_data:
    for msgPlusData in data.get_raw_data():
        #print(msgPlusData['text'])
        # if msgPlusData['text']:
        #     previous_holder = msgPlusData['text']
        #     if post:
        #         post_mes = msgPlusData['text']
        if msgPlusData['text'] and len(msgPlusData['text']) > longest_message_length:
            # previous_mes = previous_holder
            # post = True
            longest_message_length = len(msgPlusData['text'])
            #print(longest_message_length)
            # print(msgPlusData['text'])
            # print(AcqData.get_name_from_id(msgPlusData['sender_id']))
            like_set = []
            for fav in msgPlusData['favorited_by']:
                like_set.append(AcqData.get_name_from_id(fav))
            # print(like_set)
            longest_message_set.append((AcqData.get_name_from_id(msgPlusData['sender_id']),msgPlusData['text'],msgPlusData['favorited_by']))
            longest_message_data = (AcqData.get_name_from_id(msgPlusData['sender_id']),msgPlusData['text'],like_set)
        elif msgPlusData['text'] and len(msgPlusData['text']) == longest_message_length:
            count = 0
            print("HERE SAME EQUAL")
            for faved in msgPlusData['favorite_by']:
                count = count + 1
            if count > longest_message_like_count:
                like_set = []
                for fav in msgPlusData['favorited_by']:
                    like_set.append(AcqData.get_name_from_id(fav))                
                longest_message_data = (AcqData.get_name_from_id(msgPlusData['sender_id']),msgPlusData['text'],like_set)
                longest_message_like_count = count

        # else:
        #     post = False
print(longest_message_data)
print(longest_message_length)
# print(previous_mes)
# print(post_mes)
print("SHORTEST MOST LIKED MESSAGE")
shortest_length = 10000000
shortest_message_like_count = 0
shortest_data = {}
for data in every_group_data:
    for msgPlusData in data.get_raw_data():
        #print(msgPlusData['text'])
        # if msgPlusData['text']:
        #     previous_holder = msgPlusData['text']
        #     if post:
        #         post_mes = msgPlusData['text']
        if msgPlusData['text'] and len(msgPlusData['text']) < shortest_length:
            count = 0
            for faved in msgPlusData['favorited_by']:
                count = count + 1
            if count > shortest_message_like_count:
                like_set = []
                for fav in msgPlusData['favorited_by']:
                    like_set.append(AcqData.get_name_from_id(fav))                
                shortest_data = (AcqData.get_name_from_id(msgPlusData['sender_id']),msgPlusData['text'],like_set)
                shortest_message_like_count = count
print(shortest_data)

curr_user = ''
temp_length = 0
best_length = 0
consecutive_messages = ('None','',None) #person, message, date
temp_consecutive_messages = ''
print("CONSECUTIVE MESSAGE")
# MOST CONSECUTIVE MESSGES
### TODO 
for data in every_group_data:
    for msgPlusData in data.get_raw_data():
        if msgPlusData['sender_id'] == 'system':
            continue
        elif msgPlusData['name'] != curr_user:
            if temp_length > best_length:
                best_length = temp_length 
                consecutive_messages = (curr_user,temp_consecutive_messages,msgPlusData['created_at'])
            temp_consecutive_messages = ''
            curr_user = msgPlusData['name']
            temp_length = 1
            if isinstance(msgPlusData['text'],str):
                temp_consecutive_messages = ''  + msgPlusData['text'] + ' ' +  temp_consecutive_messages
        else:
            temp_length = temp_length + 1
            if isinstance(msgPlusData['text'],str):
                temp_consecutive_messages = ''  + msgPlusData['text'] + ' ' +  temp_consecutive_messages
print(consecutive_messages)
            
print("ALL MOST LIKED MESSAGES")
print(AcqData.get_users())
most_liked_count = 0 
most_liked_messages = []
# MESAGE IS who sent, MESSAGE, WHO LIKED, HOW MANY, 
# MAYBE DO THIS WITH ONLY ACQ
for data in every_group_data:
    for msgPlusData in data.get_raw_data():
        if len(msgPlusData['favorited_by']) > most_liked_count:
            most_liked_count = len(msgPlusData['favorited_by'])
            most_liked_messages = []
            if most_liked_count == 10:
                print('10')
                print(msgPlusData['name'])
            temp = (AcqData.get_name_from_id(msgPlusData['sender_id']), msgPlusData['text'],AcqData.get_names_from_ids(msgPlusData['favorited_by']),len(msgPlusData['favorited_by']))
            most_liked_messages.append(temp)
        elif len(msgPlusData['favorited_by']) == most_liked_count:
            if most_liked_count == 10:
                print('10')
                print(msgPlusData['name'])
            temp = (AcqData.get_name_from_id(msgPlusData['sender_id']), msgPlusData['text'],AcqData.get_names_from_ids(msgPlusData['favorited_by']),len(msgPlusData['favorited_by']))
            most_liked_messages.append(temp)         


print(most_liked_messages)

print("VALERIA LIKES")
# valeria_likes_per_person = {}
# for user in AcqData.get_users():
#     valeria_likes_per_person[AcqData.get_users()[user]] = 0
# print(AcqData.get_group())
# for data in every_group_data:
#     for user in data.get_user_fav():
#         if 'val_number' in data.get_user_fav()[user].keys() and user in valeria_likes_per_person.keys():
#             valeria_likes_per_person[user] += data.get_user_fav()[user]['val_number']
# print(valeria_likes_per_person)
# print(dict(sorted(valeria_likes_per_person.items(), key=lambda item: item[1], reverse=True)))           

        

print("BIGGEST FAN")

#collect all dicts of all chats, add up only sters, make a new dict with sters or use acq data
AcqLikesByPerson = {}
AcqBigFan = {}
for ster in AcqData.get_users():
    AcqLikesByPerson[AcqData.get_name_from_id(ster)] = {} 
    for base_liker in AcqData.get_users():
        AcqLikesByPerson[AcqData.get_name_from_id(ster)][AcqData.get_name_from_id(base_liker)] = 0 
for data in every_group_data:
    for ster in AcqData.get_users():
        if ster in data.get_user_fav().keys():
            for liker in data.get_user_fav()[ster]:
                if isinstance(data.get_user_fav()[ster][liker],int):
                    AcqLikesByPerson[AcqData.get_name_from_id(ster)][AcqData.get_name_from_id(liker)] = AcqLikesByPerson[AcqData.get_name_from_id(ster)][AcqData.get_name_from_id(liker)] + data.get_user_fav()[ster][liker]

# print(AcqLikesByPerson)
for ster in AcqLikesByPerson:
    bigfan = max(AcqLikesByPerson[ster], key=AcqLikesByPerson[ster].get)
    AcqBigFan[ster] = (bigfan,AcqLikesByPerson[ster][bigfan])
print(AcqBigFan)
#NEED TO ENTRY THIS IN DATA TABLE


#LATE NIGHT OWLS VS MORNING RISERS
user_night_msg_count = {}
user_morning_msg_count = {}
print("MORNING BIRDS AND NIGHTOWLS")
for user in AcqData.get_users():
    user_morning_msg_count[AcqData.get_users()[user]] = 0
    user_night_msg_count[AcqData.get_users()[user]] = 0
for data in every_group_data:
    for user in data.get_user_time():
        for time in data.get_user_time()[user]:
            t = strftime('%H', localtime(time))
            t = int(t)
            if user in AcqData.get_users().keys():
                if (t > 1 and t < 5):
                    user_night_msg_count[AcqData.get_users()[user]] += 1 
                if t > 4 and t < 9:
                    user_morning_msg_count[AcqData.get_users()[user]] += 1 
print("morning")
print(dict(sorted(user_morning_msg_count.items(), key=lambda item: item[1], reverse=True)))
print("night")
print(dict(sorted(user_night_msg_count.items(), key=lambda item: item[1], reverse=True)))





