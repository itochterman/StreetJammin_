#### FIRST INSTALL (LOCAL) ####

Install required packages:
brew install mysql
brew services start mysql (set password if want)

git clone git@github.com:itochterman/StreetJammin_.git
cd StreetJammin_
* if you do not have virtualevn installed:
* python -m pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd db
* if you get permission denied when trying to run './install_db.sh':
* chmod 777 install_db.sh
./install_db.sh (use password if set)
cd ..
cd streetjammin
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
