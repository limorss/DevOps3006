import requests
# Client that talks with the server flask
expected = "saved new car1"
response = requests.post("http://localhost:5001/whatismyname", data="aaa")
actual = response.text
assert actual == expected
