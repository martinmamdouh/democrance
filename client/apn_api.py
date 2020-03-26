import requests
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxMDg0NTE2LCJqdGkiOiJiZjliMmZiNWIzMTQ0YThhYmU4MDk5ZmUzZTkxZjk1YiIsInVzZXJfaWQiOjEsInVzZXJOYW1lIjoibWFydGluIiwidXNlckdyb3VwIjpbXX0.4qOfi9MIFfLwbT8VqAJDww23-NUf-_DIODm3rzk33qs'}
# , auth=('user', 'pass'))
r = requests.get('http://127.0.0.1:8000/apis/apn', headers=headers)
print(r.headers['content-type'])
print(r.encoding)
print(r.status_code)
print(r.json())
# print(r.text)
