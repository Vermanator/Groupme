import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import OrderedDict
import wordcloud
import stopwords
import sys
import json
import collector
import re
with open('group_data.json') as f:
    data = json.load(f)
messages = []
favorites_received = collector.get_fav_rec()
favorites_given = collector.get_fav_giv()
user_count = collector.get_user_count()
users = collector.get_users()
user_favorites = collector.get_user_fav()
user_time_messages = collector.get_user_time()
name = collector.get_name()
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
        if not (key['sender_id']) in user_time_messages:
            user_time_messages[key['sender_id']] = []
        size = len(key['favorited_by'])
        favorites_received[key['sender_id']] += size
        # print(key['text'])
        if key['system'] == False:
            messages.append(key['text'])
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
        user_time_messages[key['sender_id']].append(key['created_at'])
file_name = "data_" + name + ".txt"
# print(str(messages))
total = ""
for m in messages:
    total = total + str(m)
wordList = re.sub("[^\w]", " ",  total).split()
wordmap = {}
for w in wordList:
    if not (w in wordmap) and not (w.lower() in stopwords.get_words()):
        wordmap[w] = 1
    elif not (w.lower() in stopwords.get_words()):
        wordmap[w] = wordmap[w] + 1
t = OrderedDict(sorted(wordmap.items(), key=lambda x: x[1], reverse=True))
# print(t)

# convert list to string and generate
wordcloud = WordCloud(width=1000, height=500).generate(total)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("cloud.png")
plt.close()
print("done")
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
        outfile.write(str("\n".encode("utf-8") + "USER: ".encode("utf-8") +
                      users[key].encode('utf-8') + "\n".encode("utf-8")))
        for key2 in user_favorites[key]:
            outfile.write(str(users[key2].encode('utf-8') +
                          " ".encode("utf-8") + str(user_favorites[key][key2]).encode("utf-8") + "\n".encode("utf-8")))
