# Flask Api Example for Beginners

This piece of Python code just a example of how to make an rest api with python using flask module in minutes


## Install and activate virtualenv (highly recommended)
* Install pip first

LINUX;

```sh
~$ sudo apt-get install pip3
```

then install virtualenv using pip3

*recommended style of installation*
```sh
~$ pip3 install virtualenv --user
```


*not recommended style of installation*
```sh
~$ sudo pip3 install virtualenv
```

*NOTE: Installing python libs with 'sudo' can change your current libraries versions and can corrupt your installed apps or scripts on your distrubition which written in python. So to be safe I recommend you to install libs locally with using '--user'*



now let's create our virtualenv, you can add your python interpreter in your command. Mine is python3.6

```sh
~$ virtualenv -p /usr/bin/python3.6 venv
```

after all of it done activate your virtualenv with this command;

```sh
~$ source venv/bin/activate
```


andd... after all your work done you can deactivate your virtualenv with 'deactivate' command

```sh
~$ deactivate
```


## Running App

for python3

```sh
~$ python3 app.py
```


and hit enter after that our terminal responds us like this;


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

opening *http://127.0.0.1:8080/* in your browser will make your app visible for you in browser.

You can see if your api works or not by entering values like */kafesler*, */kafesler/mavi_kafesler*, */kafesler/mavi_kafesler/order*, */kafesler/mavi_kafesler/adet* after your localhost's name.


## Explanation

- App actually works as database reader, reads database and make it accessable from browser with localhost or smth.

## Modules Installation

- We use flask, flask_restful, sqlalchemy in making this app and it's not a built-in function so we need to install it with pip


```sh
~$ pip3 install flask, flask_restful, sqlalchemy
```

## NOTE
This app based on a scenario, so you may need to change a value or some values from app file or database file
