#!/usr/bin/python3
import requests
def resolve(ip):
    access_key='9abe21f10366ba4bfe60ecf135013032'
    api = 'http://api.ipstack.com'
    try:
        data = requests.get(f'{api}/{ip}?access_key={access_key}').json()
        ip = data['ip']
        country_name = data['country_name']
        region_name = data['region_name']
    except:
        ip = ip
        country_name = 'unknown'
        region_name = 'unknown'
    return [ip,country_name,region_name]

data = resolve('104.200.20.46')
print(data)