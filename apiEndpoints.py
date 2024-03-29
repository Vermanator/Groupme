import requests
import json
import uuid


def _url(path):
    return 'https://api.groupme.com/v3' + path + _key()


def _key():
    return '?token=M1M8YopHGQjeMCVxR77EqVWJmn5rF6isgEb4Hy1y'


def get_groups():
    return requests.get(_url('/groups') + "&per_page=100")

def get_group_names():
    names = []
    resp = get_groups()
    obj = resp.json()
    for group in obj['response']:
        names.append(group['name'])
    return names


def get_group_id(groupName):
    resp = get_groups()
    obj = resp.json()
    for group in obj['response']:
        if groupName == group['name']:
            return group['group_id']
    return "Not Found"


def get_group(groupName):
    print(groupName)
    resp = get_groups()
    obj = resp.json()
    for group in obj['response']:
        # print(group['name'])
        if groupName == group['name']:
            return requests.get(_url('/groups/' + group['group_id']))
    print("groupNotFound")
    return


def collect_group_messages_to_file(groupID, name):
    messages = []
    resp1 = get_messages(groupID)
    obj = resp1.json()

    while resp1.status_code == 200:
        messages.append(resp1.json())
        obj = resp1.json()
        resp1 = get_before_messages(
            obj['response']['messages'][-1]['id'], groupID)
        if resp1.status_code != 200:
            print (resp1.status_code)

    with open('./group_data/' + name + '.json', 'a') as outfile:
        outfile.seek(0)
        outfile.truncate()
        json.dump(messages, outfile)


def _haven_id():
    return '59947499'


def get_messages(groupID):
    #print(_url('/groups/' + groupID + 'messages'))
    return requests.get(_url('/groups/' + groupID + '/messages'))

def post_messages(groupID,message):
    data = {
        "message": {
            "source_guid": str(uuid.uuid4()),
            "text": message
        }
    }
    #print(_url('/groups/' + groupID + 'messages'))
    r = requests.post(_url('/groups/' + groupID + '/messages'),json=data)
    print("Status Code", r.status_code)
    print("JSON Response ", r.json())
    return r

def get_before_messages(id, groupID):
    return requests.get(_url('/groups/' + groupID + '/messages') + '&limit=100' + '&before_id=' + id)

def get_chats():
    return requests.get(_url('/chats'))

def like_message(conversation_id,message_id):
    return requests.post('/messages/' + conversation_id + '/' + message_id + '/like')

# print(post_messages('41005523',"beep boop"))