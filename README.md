# chobie
App for voting

    INSTALL:

0)  cd /source/directory/of/your/projects/
1)  git clone git@github.com:bryazginnn/chobie.git
2)  cd ./chobie/
3)  virtualenv venv
4)  source ./venv/bin/activate
5)  pip install -r requirements.txt
6)  <install PostgreSQL>
     a) sudo apt-get install postgresql-9.4
     b) useradd postgres
     c) passwd postgres 
7)  <open psql>
     a) su postgres
     b) psql
8)  CREATE DATABASE chobie;
9)  CREATE ROLE chobie PASSWORD 'H97fsTaf';
10) GRANT ALL ON DATABASE chobie TO chobie;
11) ALTER ROLE chobie WITH LOGIN;
12) python manage.py migrate
13) python manage.py createsuperuser
14) python manage.py runserver
 
  DONE!

