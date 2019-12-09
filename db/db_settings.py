# Modify the global_settings.py file in Django:

# Location: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/django/conf/global_settings.py

# Do 2 modifications:

# 1. modify DATABASE (see below)
# 2. modify TIME_ZONE = 'America/New_York'   (that's it)

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'songs',
        'USER': 'main_user',       
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',	#this is localhost. May need to change depending on how we're hosting
        'PORT': '5432',
    }
}


DATABASE_ROUTERS = [???] #needed? 