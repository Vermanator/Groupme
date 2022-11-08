import apiEndpoints
import json
from collections import OrderedDict

from collector import GroupData
import sys
# import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
#messages = collector.get_messages()
# data = GroupData('Paulie’s on 4th and 14')
# #data = GroupData('Pokersters')
# messages = data.get_messages()
# data.process(True)
# print(data.user_count)


resp = apiEndpoints.get_groups()
obj = resp.json()
stersGroup = []
count = 0
for group in obj['response']:
    if 'sters' in group['name']:
        count = count + 1
        print(group['name'])
        # stersGroup.append(apiEndpoints.get_group(group['name']))
print(count)

for group in stersGroup:
    group['id']
    