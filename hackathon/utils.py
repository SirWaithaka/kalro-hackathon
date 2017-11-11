import requests

base_url = 'https://atg-hackathon.mybluemix.net/api/'

goats = 'goats'
broodsites = 'broodsites'
irrigationforage = 'irrigationforage'
poultrygroups = 'poultrygroups'
weanercalves = 'weanercalves'
weightgains = 'weightgains'
weightgainbenefit = 'weightgainbenefit'
amaranthgroups = 'amaranthgroups'


def get_goats():
    r = requests.get(base_url + goats).json()
    return r


def get_broodsites():

    r = requests.get(base_url + broodsites).json()
    return r


def get_irrigationforage():
    r = requests.get(base_url + irrigationforage, ).json()
    return r


def get_weanercalves():

    r = requests.get(base_url + weanercalves,).json()
    return r


def get_amaranthgroups():
    r = requests.get(base_url + amaranthgroups, params=params).json()
    return r


def get_weightgains():

    r = requests.get(base_url + weightgains,).json()
    return r


def get_weightgainbenefit():

    r = requests.get(base_url + weightgainbenefit, params=params).json()
    return r
