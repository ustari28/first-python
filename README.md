# first-python
install tool for managing dependencies
````sh
pip install --user pipenv
````
install dependencies for project
````sh
pipenv install
````
# Set up application
Create file appengine_config.py with the content
```
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
```
create file requirements.txt with libraries
```
Flask==1.0.2
Werkzeug<0.15.0,>=0.14.0
flask-restful==0.3.7
requests==2.13.0
pyyaml==3.13
```
# Set up virtual environment
We must create a virtual environment for executing application with dependencies
```
virtualenv env
source env/bin/activate
```
After Starting the virtualenv python need to install all dependencies
```
pip install -t lib -r requirements.txt
```
Configure the app.yml that it starts your application
```
dev_appserver.py app.yml
```