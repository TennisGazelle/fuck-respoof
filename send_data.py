#!/usr/bin/python
import requests
import json
import random


def flip_coin():
    return random.randint(0, 1) == 0


def makeCompanyName():
    length = random.randint(5, 10)
    ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
    name = random.choice(ascii_letters).upper()
    for i in range(length):
        name = name + random.choice(ascii_letters)
    return name

num_requests = 1000
url_header = 'http://revexpress.com/book-demo/'
with open ('./names.json', 'r') as f:
    names = json.load(f)

payload = {}

for i in range(num_requests):
    gender = 'male' if flip_coin() else 'female'
    region_index = random.randint(0, len(names)-1)
    first_name_index = random.randint(0, len(names[region_index][gender]) - 1)
    last_name_index = random.randint(0, len(names[region_index]['surnames']) - 1)

    company_name = makeCompanyName()
    firstname = names[region_index][gender][first_name_index]
    lastname = names[region_index]['surnames'][last_name_index]
    payload['et_pb_contact_name_0'] = firstname + ' ' + lastname
    payload['et_pb_contact_email_0'] =  firstname + '_' + lastname + '@' + company_name + '.com'
    payload['et_pb_contact_company_name_0'] = company_name
    payload['et_pb_contact_website_0'] = company_name + '.com'
    payload['et_pb_contactform_submit_0'] = 'et_contact_proccess'

    print(json.dumps(payload, indent = 3))

    response = requests.get(url_header, payload)
    print('SENT!' if response.status_code == 200 else 'ERROR NOT SENT', '({})'.format(gender))