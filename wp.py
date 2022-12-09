import requests

file = open("site.txt","r").readlines()
for url in file:
	x=url.strip()
	r= requests.get(x+"/wp-content/")
	if r.status_code == 200:
		print("\033[1;32;40mWp "+x)
		
	elif r.status_code == 404:
		print("\033[1;31;40mNo "+x)