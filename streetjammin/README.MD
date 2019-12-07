Setting up Django to be connected to 2 databases


-------------- How to modify global_settings in Django-------------- 
Modify the global_settings.py file:

Location: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/django/conf/global_settings.py

Do 2 modifications:

1. modify DATABASE (see below)
2. modify TIME_ZONE = 'America/New_York'   (that's it)


To modify DATABASE, apply below changes: 

DATABASES = {
    'default':{},       #note: Django requires a default DB be included;   
                        #suggested by official docs to just keep this blank if we dont have a 'default' db
    'others': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'others',
        'USER': 'main_user',       
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },

    'songs':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'songs',
        'USER': 'main_user',       
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

------------------------------------------------------------------------------------
When you're inside streetjammin directory, log & activate venv

1. in the dir you want, create a venv:
virtualenv venv -p python3

2. activate venv:
source venv/bin/activate

3. Make sure you have Django along the path
python3 -m pip install Django

--------------------------------------------------------------------------------------------
Now, you're in (venv)Streetjammin. Ready to create DBs

5. go to your postgres db
sudo -u yumiobuchi psql postgres

6. run this command to create all necessary db & tables
\i init_6.sql

4. finally, connect to Django: 
python manage.py migrate



