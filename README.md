# Inventory_System
TO START PROJECT YOU NEED:
- First install Django 
https://www.djangoproject.com/download/ pip install Django==x.x.x
example: install Django==4.0.3
*************************************************************************************
- Install python-decouple,
pip install python-decouple
*************************************************************************************
- Install pymysql
pip install pymysql

in __init__.py file add:

import pymysql

pymysql.install_as_MySQLdb()
*************************************************************************************
- In settings.py file /mysitee/settings.py, adjust settings for database
X = adjust
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prazna',
        'HOST': 'X',
        'PORT': '3306',
        'USER': 'X',
        'PASSWORD': 'X',
    }
}
*************************************************************************************
In MySQl workbench create base "prazna".
*************************************************************************************
Type in VS code terminal python manage.py migrate
*************************************************************************************
Start the server using python manage.py runserver in terminal.
