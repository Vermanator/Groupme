import apiEndpoints
import json

messages = []
resp1 = apiEndpoints.get_messages()
obj = resp1.json()

while resp1.status_code == 200:
    messages.append(resp1.json())
    obj = resp1.json()
    resp1 = apiEndpoints.get_before_messages(
        obj['response']['messages'][-1]['id'])

with open('group_data.json', 'a') as outfile:
    outfile.seek(0)
    outfile.truncate()
    json.dump(messages, outfile)
