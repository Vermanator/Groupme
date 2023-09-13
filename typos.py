from collections import OrderedDict
from spellchecker import SpellChecker
import apiEndpoints
import json
from collector import GroupData
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
def spell3(wl):
    wordlist=wl.split()
    spell = SpellChecker()
    return len(list(spell.unknown(wordlist)))
    #print("Possible amount of misspelled words in the text:",amount_miss)
   

data = GroupData('Paulie’s on 4th and 14')
#data = GroupData('Pokersters')
data.process(False)
messages = data.get_user_messages_time()
results = {}
start_date = datetime(2022, 9, 8).timestamp()
current_date = datetime(2023, 1, 2).timestamp()
# current_week_start = (start_date + timedelta(weeks=j)).timestamp()

users_messages = [(messages[msg],msg) for msg in messages]
for um in users_messages:
    user_messages = um[0]
    user_combined_msg = ''

    for msg in user_messages:
        if msg[0] and float(msg[1]) > start_date and float(msg[1]) < current_date:
            user_combined_msg = user_combined_msg + msg[0]
    #print(user_combined_msg)

    results[data.users[um[1]]] = spell3(user_combined_msg)
res = {key: val for key, val in sorted(results.items(), key = lambda ele: ele[1], reverse = True)}
print(res)