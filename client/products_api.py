import requests
# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjA2NzMxOTksImp0aSI6IjU4MjkxYzU0Y2I4YzRlYmQ4NTUxYTVhMGU5ZWEwNDEzIiwidXNlcl9pZCI6MSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsIm5hbWUiOiJtYXJ0aW4ifQ.w_k8gTstyJWQs8Izt4zcHQGSsk5JkTlYjanwwU56pMc'}
# , auth=('user', 'pass'))


def getAllProducts():
    r = requests.get('http://127.0.0.1:8000/products/')

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def getProductByID(id):
    r = requests.get(f'http://127.0.0.1:8000/products/{id}')

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def createProduct():
    data = {"code": "1", "name": "chaniliah", "product_type": "1"}
    r = requests.post('http://127.0.0.1:8000/products/', data=data)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


# getAllProducts()
createProduct()
# getProductByID(1)
