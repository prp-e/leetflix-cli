import json 
import requests
import subprocess

API_URL = "https://leetflix.haghiri75.com"

movie_name = input("Enter a movie name (or keywords): ")

response = requests.post(API_URL, data=json.dumps({"keyword" : movie_name}), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0', 'content-type': 'application/json'})

index = 1
for result in response.text:
    print(f'{index} : {title}')
    index += 1 