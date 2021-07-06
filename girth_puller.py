import requests
import json


def _url(path):
    return 'https://api.groupme.com/v3' + path + _key()


def _key():
    return '?token=M1M8YopHGQjeMCVxR77EqVWJmn5rF6isgEb4Hy1y'


def get_groups():
    return requests.get(_url('/groups'))


def get_group():
    return requests.get(_url('/groups/' + _haven_id()))


def _haven_id():
    return '59947499'


def get_messages():
    print(_url('/groups/' + _haven_id() + 'messages'))
    return requests.get(_url('/groups/' + _haven_id() + '/messages'))


def get_before_messages(id):
    return requests.get(_url('/groups/' + _haven_id() + '/messages') + '&limit=100' + '&before_id=' + id)
