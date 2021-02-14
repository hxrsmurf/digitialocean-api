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

def createDroplet():
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

def getDroplet():
    api_url = '{0}droplets'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    droplets = json.loads(response.content.decode('utf-8'))

    for key, dropletInfo in enumerate(droplets['droplets']):
        for k, v in dropletInfo.items():
                if k == 'id' or k == 'networks' or k == 'name':
                    if k == 'networks':
                        v = v['v4'][0]['ip_address']
                    print('{0}:{1}'.format(k, v))

def deleteDroplet(dropletID):
    api_url = '{0}droplets'.format(api_url_base)
    droplet_url = api_url + '/' + dropletID
    response = requests.delete(droplet_url, headers=headers)

def listDomains():
	api_url = api_url_base + "domains"
	response = requests.get(api_url, headers=headers)
	domains = json.loads(response.content.decode('utf-8'))
	for k, v in enumerate(domains['domains']):
		print('{0}:{1}'.format(k, v['name']))
	  
def listDomainRecords(domain):
	api_url = api_url_base + "domains/" + domain + "/records"
	response = requests.get(api_url, headers=headers)
	domainsRecords = json.loads(response.content.decode('utf-8'))
	for k, v in enumerate(domainsRecords['domain_records']):
		print('{0}:{1}:{2}:{3}'.format(v['id'],v['type'],v['name'],v['data']))
	  
def createDomainRecord(domain, type, name, data):
	api_url = api_url_base + "domains/" + domain + "/records"
	body = {
		"type": type,
		"name": name,
		"data": data
	}
	response = requests.post(api_url, headers=headers, json=body)
	print(response)
	
def updateDomainRecord(domain, data, recordID):
	api_url = api_url_base + "domains/" + domain + "/records/" + recordID
	body = {
		"data": data
	}
	response = requests.put(api_url, headers=headers, json=body)
	print(response)
	
def myIP():
	response = requests.get("https://api.ipify.org").text
	update_domain_record("hxrsmurf.info",response,"95875744")

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