import girth_puller
import json
import requests


resp = girth_puller.get_groups()
obj = resp.json()
stersGroup = []
for group in obj['response']:
    if 'sters' in group['name']:
        stersGroup.append(requests.get(_url('/groups/' + group['group_id'])))


for group in stersGroup:
    group['id']
    