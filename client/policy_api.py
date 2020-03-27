import requests
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxMDg0NTE2LCJqdGkiOiJiZjliMmZiNWIzMTQ0YThhYmU4MDk5ZmUzZTkxZjk1YiIsInVzZXJfaWQiOjEsInVzZXJOYW1lIjoibWFydGluIiwidXNlckdyb3VwIjpbXX0.4qOfi9MIFfLwbT8VqAJDww23-NUf-_DIODm3rzk33qs'}


def createPolicy():
    data = {"type": "personal-accident",
            "premium": 200,
            "cover": 200000, "customer": 2}
    r = requests.post(
        'http://127.0.0.1:8000/api/v1/create_policy/', data=data)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


createPolicy()
