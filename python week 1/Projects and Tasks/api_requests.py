# api requests

import requests
import json

post_codes_req = requests.get("https://postcodes.io/postcodes/sw22qr")

print(post_codes_req) #200
print(post_codes_req.headers) #gives the headers
print(post_codes_req.content) #gives json body

#short way
print(post_codes_req.json()) #inbuilt methods