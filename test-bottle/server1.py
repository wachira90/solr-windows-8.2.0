#!python
import os
import sys
from bottle import run, get, post, request, delete, route, template, response
from json import dumps
import requests




@get('/')
def emp():
	employee = [{'name': 'Sam', 'address': 'Ranchi', 'Dept': 'HR'},
            {'name': 'Sarah', 'address': 'Ranchi', 'Dept': 'MGR'},
            {'name': 'Arsh', 'address': 'Delhi', 'Dept': 'HR'}]
	# response.headers['Content-Type'] = 'application/json'
    return{'employees': employee}

@get('/list')
def list1():
	response.headers['Content-Type'] = 'application/json'
	r = requests.get(
		"http://localhost:8983/solr/db/select?q=*%3A*&rows=200&sort=id%20desc&start=1",
		params = {},
		# params = {'q': '*%3A*&rows=80&sort=id%20desc&start=1'},
		headers = {'Content-Type': 'application/json'},
	)
	res = r.json()['response']['docs']
	
	return dumps(res)

run(host='localhost', port=8080, reloader=True, debug=True)
