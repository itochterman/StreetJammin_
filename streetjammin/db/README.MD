Setting up Django to be connected to 1 database 

------------------------------------------------------------------------------------
How to modify global_settings in Django 

Apply changes in this file: db_settings.py

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

5. run commands inside this file to Create DB and associated tables: install_db.sh

<!-- 
4. Connect your MySQL db to Django: install_db.sh

5. 
python manage.py migrate



 -->