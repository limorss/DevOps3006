import  datetime
from time import sleep
import requests
print(datetime.datetime.now())
#sleep(10)
print(datetime.datetime.now())
response = requests.get("https://github.com")
if response.status_code == 200:
    print("github is up and running!")
