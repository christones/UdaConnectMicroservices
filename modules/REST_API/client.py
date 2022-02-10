import requests

r = requests.get('http://localhost:5000/health')

if r.status_code=200:
	print(r.json())
	
	
located = requests.get('http://localhost:5001/location_api/locations')
     
if located.status_code=200:
	print(located.json())	
	
	
person = requests.get('http://localhost:5002/person_api/person')

if person.status_code=200:
	print(person.json()) 
	
	
	
	

