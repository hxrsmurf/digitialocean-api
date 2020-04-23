import json
import requests
import argparse
import time
import textwrap

api_token = ''
key = ''

api_url_base = 'https://api.digitalocean.com/v2/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
description = "Create DigitalOcean Droplets with Python"
image = 'debian-10-x64'
region = 'nyc1'
size = 's-1vcpu-1gb'
name = 'apitest'
userData = """
#cloud-config
runcmd: 
 - ssh-keygen
 - echo "stuff" > /root/stuff.txt
"""

def create_droplet():
    api_url = '{0}droplets'.format(api_url_base)
    body = {
        "name": name + '-' + (time.strftime("%Y-%m-%d-%H-%M")),
        "region": region,
        "size": size,
        "image": image,
        "ssh_keys": [key],
        "user_data": userData,          
    }
    response = requests.post(api_url, headers=headers, json=body)

def get_droplet():
    api_url = '{0}droplets'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    droplets = json.loads(response.content.decode('utf-8'))

    for key, dropletInfo in enumerate(droplets['droplets']):
        for k, v in dropletInfo.items():
                if k == 'id' or k == 'networks' or k == 'name':
                    if k == 'networks':
                        v = v['v4'][0]['ip_address']
                    print('{0}:{1}'.format(k, v))

def delete_droplet(dropletID):
    api_url = '{0}droplets'.format(api_url_base)
    droplet_url = api_url + '/' + dropletID
    response = requests.delete(droplet_url, headers=headers)

parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g", "--get", action='store_true', help="Get Droplets")
parser.add_argument("-c", "--create", action='store_true', help="Create Droplet")
parser.add_argument("-d", "--delete", nargs= '*' , help="Delete Droplet")
args = parser.parse_args()

if args.get:
    get_droplet()
elif args.create:
    create_droplet()
elif args.delete:
    for id in args.delete:
        delete_droplet(id)
else:
    print('Empty Input')
