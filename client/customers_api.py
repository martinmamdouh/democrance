import requests
import datetime

# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjA2NzMxOTksImp0aSI6IjU4MjkxYzU0Y2I4YzRlYmQ4NTUxYTVhMGU5ZWEwNDEzIiwidXNlcl9pZCI6MSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsIm5hbWUiOiJtYXJ0aW4ifQ.w_k8gTstyJWQs8Izt4zcHQGSsk5JkTlYjanwwU56pMc'}
# , auth=('user', 'pass'))


def createCustomer():
    data = {"first_name": "martin", "last_name": "mamdouh",
            "dob": datetime.date(1989, 10, 4)}
    r = requests.post(
        'http://127.0.0.1:8000/api/v1/create_customer/', data=data)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def createPolicy():
    data = {"type": "personal-accident",
            "premium": 200,
            "cover": 200000, "customer": 1}
    r = requests.post(
        'http://127.0.0.1:8000/api/v1/create_policy/', data=data)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


# getAllCusomers()
# createCustomer()
createPolicy()
