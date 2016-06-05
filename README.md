# chobie
App for voting


INSTALL:
--------

install requirements programms
      
      sudo apt-get install python2.7 python-dev 
      
      sudo apt-get install git

download project:

      cd /source/directory/of/your/projects/

      git clone git@github.com:bryazginnn/chobie.git

      cd ./chobie/

install PostgreSQL:

       sudo apt-get install postgresql-9.3 postgresql-server-dev-9.3
     
       sudo useradd postgres
     
       sudo passwd postgres 
     
init virtualenv:
      
      sudo apt-get install python-virtualenv

      virtualenv venv

      source ./venv/bin/activate

      pip install -r requirements.txt

open psql:

       su postgres
     
       psql

execute in PostgreSQL:
     
      CREATE DATABASE chobie;

      CREATE ROLE chobie PASSWORD 'H97fsTaf';

      GRANT ALL ON DATABASE chobie TO chobie;

      ALTER ROLE chobie WITH LOGIN;

close psql and exit from postgres user:
    
      \q
      
      exit

initialize django's project:

      python manage.py migrate

      python manage.py createsuperuser

      python manage.py runserver

 
  DONE!
  
BIND WITH HEROKU:

      wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

      heroku login

      heroku git:remote -a chobie


