# user_profile_system

clone the project<br>
git clone https://github.com/rh13/user_profile_system.git

## create and start a virtual environment:<br>
virtualenv --python=python3 venv <br>
source venv/bin/activate <br><br>

## Install django: <br>
pip install Django==2.1.3 <br><br>

cd messaging <br>

## to makemigrations for the app<br>
python manage.py makemigrations<br>
python manage.py migrate<br><br>

## create admin user:<br>
python manage.py createsuperuser<br><br>

## start server:<br>
python manage.py runserver<br><br>

and open localhost:8000 on your browser.
