import requests
import json


def _url(path):
    return 'https://api.groupme.com/v3' + path + _key()


def _key():
    return '?token=38d12d705e0c0137d05b3a7df66bb9ac'


def get_groups():
    return requests.get(_url('/groups'))


def get_group():
    return requests.get(_url('/groups/' + _haven_id()))


def _haven_id():
    return '41005523'


def get_messages():
    print(_url('/groups/' + _haven_id() + 'messages'))
    return requests.get(_url('/groups/' + _haven_id() + '/messages'))


def get_before_messages(id):
    return requests.get(_url('/groups/' + _haven_id() + '/messages') + '&limit=100' + '&before_id=' + id)
