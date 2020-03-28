# Democrance

### Installation

Democrance requires [Python ](https://python.org/) v3.6+ to run.

- [optional] Install virtualenv to install the dependencies in an isolated python environement.

```sh
$ python -m pip install virtualenv
$ pythoon -m virtualenv democranceEnv
$ cd democranceEnv/bin/
$ source activate
```

- Install the dependencies and start the server.

> > Clone the repository and change the current directory to the repo directory then run the below commands.

```sh
$ python -m pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
python manage.py runserver
```

### Create Customer

How to create a customer instance?

There are three ways to create a new customer instance:

#### 1) Using python requests library:

- Inside the cloned django project there is a python script "client/create_customer_api.py" by running this script will call the django endpoint "http://localhost:8000/api/v1/create_customer" to create a new customer instance.
- Using the admin panel you should find the customer instance has been created.

```sh
$ python client/create_customer_api.py
```

#### 2) Using python rest-framework browsable Api:

- Navigate the browser to "http://localhost:8000/api/v1/create_customer"
  and use the browserable API form to create a new customer instance.

#### 3) Using Postman:

-Using Postman application send an api to the same end point with the below request object:

```json
{
  "first_name": "Ben",
  "last_name": "Stokes",
  "dob": "25-06-1991"
}
```

### Create an Insurance Policy for a specific customer:

How to create an insurance policy for the created customer?

There are three ways to create a new insurance policy instance:

#### 1) Using python requests library:

- Inside the cloned django project there is a python script "client/create_policy_api.py" by running this script will call the django endpoint "http://localhost:8000/api/v1/create_insurance_policy" to create a new insurance policy instance.
- Using the admin panel you should find the insurance policy instance has been created.

```sh
$ python client/create_policy_api.py
```

#### 2) Using python rest-framework browsable Api:

- Navigate the browser to "http://localhost:8000/api/v1/create_insurance_policy"
  and use the browserable API form to create a new customer instance.

#### 3) Using Postman:

-Using Postman application send an api to the same end point with the below request object:

```json
{
  "type": "personal-accident",
  "premium": 200,
  "cover": 200000,
  "customer": 1
}
```
