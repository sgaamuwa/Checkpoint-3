[![Build Status](https://travis-ci.org/andela-sgaamuwa/Checkpoint-3.svg?branch=develop)](https://travis-ci.org/andela-sgaamuwa/Checkpoint-3)
[![Coverage Status](https://coveralls.io/repos/github/andela-sgaamuwa/Checkpoint-3/badge.svg?branch=develop)](https://coveralls.io/github/andela-sgaamuwa/Checkpoint-3?branch=develop)
# Ebyokola API APPLICATION 
Ebyokola is a RESTful API application where users can create bucketlists with multiple items.
The application uses Token Based Authentication for user authentication and authorization.

## Application Description

### Dependencies
The Ebyokola API is a python/django application and is mainly dependent on the following technologies

* **[Python3](https://www.python.org/download/releases/3.0/)**
* **[Django Restframework](http://www.django-rest-framework.org/)** for RESTful implementation
* **[Djoser](https://github.com/sunscrapers/djoser)** for Token Authentication and User Handling
* **[Unittest](https://docs.python.org/2/library/unittest.html)**, **[Nose](http://nose.readthedocs.io/en/latest/)** for the testing

### Functionality
The user of the application has the ability to carry out the following

* Register a new user with the application 
    * Usernames have to be unique for a successful registration
    * Users must provide a password for a successful registration
    * Users may have an email, but this is optional
    * Usernames and passwords must be minimum 4 characters for successful registration 
    ```
        {
            "username": "sample_username",
            "password": "sample_password"
        }
    ```

* Login to use the system with the same information above

* Once logged in, the user then requests for token
    * Once logged in, a user can request another token, without having to log back in 

* Users can create new bucketlists each with a unique name with the POST information below
    ```
        {
            "name": "sample_bucketlist"
        }
    ```

* For each bucketlist, a user can add an items with a similar post

* Items and bucketlists can be deleted from the server
    * Deleting a bucketlist deletes all its items

* Bucketlist names can be updated and Items' done statuses can also be updated

* A user can request for all their bucketlists in the system, or a specific bucketlist

* **Users can only interact with bucketlists that they created**

### API endpoints and Routes 

|ENDPOINT | FUNCTIONALITY|
|--- | ---
|POST ```/auth/login``` | Logs a user in|
|POST ```/auth/register``` | Register a user|
|POST ```/bucketlists```| Create a new bucket list|
|GET ```/bucketlists``` | List all the created bucket lists|
|GET ```/bucketlists/<id>```| Get single bucket list|
|PUT ```/bucketlists/<id>```| Update this bucket list|
|DELETE ```/bucketlists/<id>```| Delete this single bucket list|
|POST ```/bucketlists/<id>/items/```| Create a new item in bucket list|
|PUT ```/bucketlists/<id>/items/<item_id>```|Update a bucketlist item|
|DELETE ```/bucketlists/<id>/items/<item_id>```| Delete an item in a bucket list|

## Installation
The bucketlist API is a flask and Python3 application and it is advisable to install it in a virtual environment. 
As most Linux machines come with Python 2 installed, it is required that you install Python 3 through the terminal using the commands 
```
$ sudo apt-get update 
$ sudo apt-get install python3 
```
If you are using macOS, python3 can be installed through the terminal using the command
```
$ brew install python3
```
If you do not already have git installed on your system install it as well
```
$ sudo apt-get install git
```
or on macOS
```
$ brew install git
```
Python3 comes with a package manager called pip, which enables you to install different packages in your environment 
We shall use pip to install virtualenv, which helps us create a virtual environment where dependencies can be installed without impacting the rest of the system
To install virtualenv run the following command 
```
$ pip install virtualenv
```
Once installed, create a directory for the application called Bucketlist and open it using the commands
```
$ mkdir Ebyokola
$ cd Ebyokola
```
Create a virtual environment for the application that is python3 specific 
```
$ virtualenv -p python3 venv-bucketlist
```
Activate the virtual environment 
```
$ source venv-ebyokola/bin/activate 
```
At this point, clone the project into the folder, move into the project directory and run the requirements file
```
$ git clone https://github.com/andela-sgaamuwa/Checkpoint-3.git
$ cd Checkpoint-3
$ pip install -r requirements.txt
```
Next you need to migrate and set up the database
The application uses a Postgresql database therefore one should setup the Postgres environment and created a database named ebyokola before these commands
```
$ python manage.py makemigrations
$ python manage.py migrate
```
The application is then ready to run, simply use the command 
```
$ python manage.py runserver
```

## Running tests
Upon installation it is advisable to run the tests to ensure that the application is running as it should and nothing is broken
In the root directory of the application, via the terminal, run the command
```
$ python manage.py test
```
A successful test should produce the following results 
```
(cp3-venv) Samuels-MacBook-Pro:ebyokola gaamuwa$ python manage.py test
nosetests --with-coverage --cover-package=api --verbosity=1
Creating test database for alias 'default'...
.....................................
Name                 Stmts   Miss  Cover
----------------------------------------
api/admin.py            10      0   100%
api/models.py           21      2    90%
api/pagination.py        5      0   100%
api/permissions.py       8      0   100%
api/serializers.py      29      1    97%
api/urls.py              5      0   100%
api/views.py            50      0   100%
----------------------------------------
TOTAL                  128      3    98%
----------------------------------------------------------------------
Ran 37 tests in 6.376s

OK
Destroying test database for alias 'default'...
```