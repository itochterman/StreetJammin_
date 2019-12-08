------- How to run migration for models ---------
1. 
cd /Users/yumiobuchi/Desktop/StreetJammin_/streetjammin/streetjammin 

2. go into venv
virtualenv venv -p python3
source venv/bin/activate

3. ensure you have Django installed
python3 -m pip install Django

4. Do the migration
python3 manage.py makemigrations jammin
python3 manage.py migrate