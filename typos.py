from collections import OrderedDict
from spellchecker import SpellChecker
import apiEndpoints
import json
from collector import GroupData
import sys
# import matplotlib.pyplot as plt
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
messages = data.get_user_messages()
results = {}
users_messages = [(messages[msg],msg) for msg in messages]
for um in users_messages:
    user_messages = um[0]
    user_combined_msg = ''

    for msg in user_messages:
        #print(msg)
        if msg:
            user_combined_msg = user_combined_msg + msg
    #print(user_combined_msg)

    results[data.users[um[1]]] = spell3(user_combined_msg)
print(results)