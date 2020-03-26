import requests
# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjA2NzMxOTksImp0aSI6IjU4MjkxYzU0Y2I4YzRlYmQ4NTUxYTVhMGU5ZWEwNDEzIiwidXNlcl9pZCI6MSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsIm5hbWUiOiJtYXJ0aW4ifQ.w_k8gTstyJWQs8Izt4zcHQGSsk5JkTlYjanwwU56pMc'}
# , auth=('user', 'pass'))


def getAllProductTypes():
    r = requests.get('http://127.0.0.1:8000/product-types/')

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def getProductTypeByID(id):
    r = requests.get(f'http://127.0.0.1:8000/product-types/{id}')

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


def createProductType():
    data = {"type": "fabric"}
    r = requests.post('http://127.0.0.1:8000/product-types/', data=data)

    print(r.encoding)
    print(r.status_code)
    # print(r.json())
    print(r.text)


getAllProductTypes()
# createProductType()
# getProductTypeByID(1)
