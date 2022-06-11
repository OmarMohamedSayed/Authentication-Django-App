# Dev Authentication App WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3
- Django 4
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
https://github.com/OmarMohamedSayed/Authentication-Django-App.git
cd Authentication-Django-App

virtualenv venv -p python3
source my_env/bin/activate
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

You can create superuser
```
python manage.py createsuperuser
```

## Structure
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/register/` | POST | CREATE | new user with phone number
`api/login/`| POST | Create | create new auth-tone to user
`api/profile/:phonenumber` | Patch | UPDATE | Update user profile
`app/profile/:phonenumber` | GET | READ | Get user profile

#### Note
all endpoinsts with body you can find it in a [Dev-Task.postman_collection.json](https://github.com/OmarMohamedSayed/Authentication-Django-App/blob/main/Dev-Task.postman_collection.json) postman coolection 

## Use

### Development Part
First, we have to start up Django's development server.
```

python manage.py runserver
```

#### Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://127.0.0.1:8000/api/register/  username="Phone Number" password="PASSWORD"
```
Second we need to create a token
```
http POST http://127.0.0.1:8000/api/login/  username="Phone Number" password="PASSWORD"
```
Third you can update your profile 
```
http PUTCH http://127.0.0.1:8000/api/profile/<:phonenumber> "Authorization: Token {YOUR_TOKEN}"
```

Forth you can get your profile 
```velopment
http GET http://127.0.0.1:8000/api/profile/<:phonenumber> "Authorization: Token {YOUR_TOKEN}"
```


### Deployment Part


You can use Docker-compose , Docker, gunicorn to deploy on server by run.
```
docker-compose build
docker-compose up
```

#### Note
you can install docker-compose by using this [link](https://docs.docker.com/compose/install/)

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```
