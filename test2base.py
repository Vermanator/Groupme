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
   

data = GroupData('Foodsters')
data.process(True)