--------------------------------Google Cloud Deployment-----------------------------------

1. Create a new GCCE instance with boot image 'Ubuntu 16.04 LTS' & SSH into it
2. git clone https://github.com/itochterman/StreetJammin_.git
3. (Linux only) $ sudo apt-get update; sudo apt-get install mysql-server libmysqlclient-dev python-dev python-virtualenv
(Set a mysql root password)
4. $ ./first_install.sh --> source ./venv/bin/activate 
5. cd db
6. chmod a+x install_db.sh
7. ./install_db.sh
8. python manage.py makemigrations
9. python manage.py migrate 
10. python manage.py runserver
11. Add the external IP address (found on instance page of GCP) to the list of "allowed hosts" in settings.py 
12. run python manage.py runserver 0.0.0.0:8000
13. paste <external-IP-address>:<port(8000 in this case)> into browser to run site
	--> One such example would be: http://35.225.136.165:8000/ where ip address is 
		"35.225.136.165" and port is "8000"
14. gg

