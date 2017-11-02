import json

filename = 'username.json'

with open(filename) as f_obj:
	usename = json.load(f_obj)
	print("Welcome back, " + usename + "!")