# Flask Api Example for Beginners

This piece of Python code just a example of how to make an rest api with python using flask module in minutes

## Running App

LINUX;

for python2

```sh
$ python app.py
```

for python3

```sh
$ python3 app.py
```


MacOS and Windows;


You can use same command but use with which letter you use your python python/python3


and hit enter after that our terminal will respond us like this;


```sh
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 292-676-818
```

opening [http://127.0.0.1:8080/](http://127.0.0.1:8080/) in your browser will make your app visible for you in browser.

You can see if your api works or not by entering values like */kafesler*, */kafesler/mavi_kafesler*, */kafesler/mavi_kafesler/order*, */kafesler/mavi_kafesler/adet* after your localhost's name.


## Explanation

- App actually works as database reader, reads database and make it accessable from browser with localhost or smth.

## Modules Installation

- We use flask in making this app and it's not a built-in function so we need to install it with pip

for python2

```sh
$ pip install flask
```


for python3

```sh
$ pip3 install flask
```



We don't use only flask.. We need to install *flask_restful* and *sqlalchemy* for making database items accessable from api. Flask works together each of them.

We can install these with pip too..

for python2

```sh
$ pip install flask_restful, sqlalchemy
```

for python3

```sh
$ pip3 install flask_restful, sqlalchemy
```

just like that...


## Database
For making your own database you can simply use [github.com/ybgirgin3/BookStore-Database](github.com/ybgirgin3/BookStore-Database) app 


## NOTE
This app based on a scenario, so you may need to change a value or some values from app file or database file
