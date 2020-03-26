import requests
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxMzg0NTY0LCJqdGkiOiIwNDgyMDNlNWRhOTY0ODg5OGViMzFmNmZiMmQyYzM1NCIsInVzZXJfaWQiOjEsInVzZXJOYW1lIjoibWFydGluIiwidXNlckdyb3VwIjpbXX0.8PSQb2D1KGPKHnKRJRlXKy5BrjhgYqfDaMfbs-2uESk'}
# , auth=('user', 'pass'))


def getAllBills():
    r = requests.get('http://127.0.0.1:8000/bills/', headers=headers)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def getBillByID(id):
    r = requests.get(f'http://127.0.0.1:8000/bills/{id}', headers=headers)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def createBill():
    data = {
        "customer": {
            "name": "andrew",
            "phone": "0990909",
            "email": "",
            "address": ""
        },
        "bill_items": [{"product": 1, "amount": 20, "price": 200, "bill_item_status_id": 1},
                       {"product": 1, "amount": 30, "price": 100, "bill_item_status_id": 1}],
        "paid": 300,
        "branch": "NC",
        # "payment_status": 1,
        "bill_status": 1,
        "seller": 1,
        "user": 1
    }
    r = requests.post('http://127.0.0.1:8000/bills/',
                      json=data, headers=headers)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def updateBill(id):

    data = {
        "seller": 1, "bill_status": 3, "branch": "MD", "paid": 200
    }
    # data = {
    #     "branch": "MD"
    # }
    r = requests.put(
        f'http://127.0.0.1:8000/bills/{id}', json=data, headers=headers)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


# getBillByID(59)
createBill()
# updateBill(68)
# getAllBills()
