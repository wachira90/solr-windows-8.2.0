#!python

import requests

# http://localhost:8983/solr/db/select?q=*%3A*&rows=80&sort=id%20desc&start=1
r = requests.get(
    "http://localhost:8983/solr/db/select?q=*%3A*&rows=80&sort=id%20desc&start=1",
	params = {},
    # params = {'q': '*%3A*&rows=80&sort=id%20desc&start=1'},
    headers = {'Content-Type': 'application/json'},
)
print(r.url)
res = r.json()['response']['docs']
print(res)
# print(r.text)
