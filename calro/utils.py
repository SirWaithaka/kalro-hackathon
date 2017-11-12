import requests

base_url = 'https://atg-hackathon.mybluemix.net/api/'

amaranthgroups = 'amaranthgroups'

def get_amaranthgroups():
    r = requests.get(base_url + amaranthgroups).json()
    return r
