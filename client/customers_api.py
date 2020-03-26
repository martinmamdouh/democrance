import requests
# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjA2NzMxOTksImp0aSI6IjU4MjkxYzU0Y2I4YzRlYmQ4NTUxYTVhMGU5ZWEwNDEzIiwidXNlcl9pZCI6MSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsIm5hbWUiOiJtYXJ0aW4ifQ.w_k8gTstyJWQs8Izt4zcHQGSsk5JkTlYjanwwU56pMc'}
# , auth=('user', 'pass'))


def getAllCusomers():
    r = requests.get('http://127.0.0.1:8000/customers/')

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def getCusomerByID():
    r = requests.get('http://127.0.0.1:8000/customers/1')

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def createCusomer():
    data = {"name": "martin", "phone": "090990"}
    r = requests.post('http://127.0.0.1:8000/customers/', data=data)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


# getAllCusomers()
# createCusomer()
getCusomerByID()
