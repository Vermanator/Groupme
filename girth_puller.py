import requests
import json

def _url(path):
    return 'https://api.groupme.com/v3' + path
def _key():
    return '?token=kf73g7TvqtF5VlIWHSgtDJaYYd7b1aiO2A3e7r3S'
def _haven_id():
    return '32859036'

def _shawn():
    return '30072237'
def _andrew():
    return '30295737'
def _wes():
    return '17827479'
def _ben():
    return '23839465'

def get_groups():
    return requests.get(_url('/groups'))
def get_group():
    return requests.get(_url('/groups/' + _haven_id() + _key()))
def get_messages():
    print (_url('/groups/' + _haven_id() +'messages'))
    return requests.get(_url('/groups/' + _haven_id() +'/messages' + _key()))
def get_before_messages(id):
    return requests.get(_url('/groups/' + _haven_id() +'/messages' + _key()) + '&limit=100' + '&before_id=' + id)
