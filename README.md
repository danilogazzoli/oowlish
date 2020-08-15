# Oowlish test

## Project Description

This project is built on Python Language and Django Rest Framework as a way to provide an API in order to list data for customers.

## Instalation and test instructions

To run this project it's necessary to have python >= 3.6 installed and follow the steps below:

#### Install the virtual environment:
```sh
$ sudo apt install virtualenv
```

In order to create the virtual environment, it's necessary to run:

```sh
$ virtualenv --python=python3.6 .my_env
```

and then, activate it:

```sh
$ source .my_env/bin/activate
```

### Install the requirements

Once the virtual environment is activated, it's necessary to run the requirements:

```sh
$ pip install -r requirements.txt
```

### .env settings file

It's also necessary to create a .env file at the root directory with the following entries:	
```sh
SECRET_KEY=AnythingYouWant
API_KEY= ThisIsTheGoogleAPIKey
DEBUG=False

```

### Migrate the database

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### Start the server

Now it's possible to start the server by running:

```sh
$ python manage.py runserver
```

### Run customized command

There's a special command that is intended to import the customers data as well as query on the Google Maps API their respective latitude and longitude.
The syntax of the command is:

```sh
$ python manage.py import_customers {customers.csv file}
```

Example:

```sh
$ python manage.py import_customers customers.csv
```

The customers file requires the following fields, separated by comma:

```sh
id,first_name,last_name,email,gender,company,city,title
```

### Customer's endpoints

In order to get the list of customers, it's necessary to do a GET action on:

```sh
http://localhost:8000/api/v1/customers/
```

Output:

```sh
[
    {
        "id": 1,
        "first_name": "Laura",
        "last_name": "Richards",
        "email": "lrichards0@reverbnation.com",
        "gender": "Female",
        "company": "Meezzy",
        "city": "Warner, NH",
        "title": "Biostatistician III",
        "latitude": "43.255657",
        "longitude": "-71.833414"
    },
    {
        "id": 2,
        "first_name": "Margaret",
        "last_name": "Mendoza",
        "email": "mmendoza1@sina.com.cn",
        "gender": "Female",
        "company": "Skipfire",
        "city": "East Natchitoches, PA",
        "title": "VP Marketing",
        "latitude": "41.203322",
        "longitude": "-77.194525"
    },
    (...)
]
``` 

```sh
Status: 200 OK
```

If you want to retrieve only one author:

```sh
http://localhost:8000/api/v1/customers/{Author id}
Example:
http://localhost:8000/api/v1/customers/1
```

Output:

``` sh
{
    "id": 1,
    "first_name": "Laura",
    "last_name": "Richards",
    "email": "lrichards0@reverbnation.com",
    "gender": "Female",
    "company": "Meezzy",
    "city": "Warner, NH",
    "title": "Biostatistician III",
    "latitude": "43.255657",
    "longitude": "-71.833414"
}
```

```sh
Status: 200 OK
```

All the functionalities of the API are documented on:

```sh
http://localhost:8000/swagger/
```

## Environment

This application was built on vim and Pycharm 2020.1 (Community Edition), running Ubuntu Linux:
```sh
Linux Inspiron 5.3.0-46-generic #38~18.04.1-Ubuntu SMP Tue Mar 31 04:17:56 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```






