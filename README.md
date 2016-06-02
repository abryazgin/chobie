# chobie
App for voting


INSTALL:
--------


download project:

      cd /source/directory/of/your/projects/

      git clone git@github.com:bryazginnn/chobie.git

      cd ./chobie/

init virtualenv:

      virtualenv venv

      source ./venv/bin/activate

      pip install -r requirements.txt

install PostgreSQL:

       sudo apt-get install postgresql-9.4
     
       useradd postgres
     
       passwd postgres 
     
open psql:

       su postgres
     
       psql

execute in PostgreSQL:
     
      CREATE DATABASE chobie;

      CREATE ROLE chobie PASSWORD 'H97fsTaf';

      GRANT ALL ON DATABASE chobie TO chobie;

      ALTER ROLE chobie WITH LOGIN;

close psql:
    
      \q

initialize django's project:

      python manage.py migrate

      python manage.py createsuperuser

      python manage.py runserver

 
  DONE!
  
BIND WITH HEROKU:

      wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

      heroku login

      heroku git:remote -a chobie


