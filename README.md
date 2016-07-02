# homework
Simple web application that shows a visit counter and lets you reset it. Written in Python on Flask with data in AWS DynamoDB.
## Setting up the server
Example applies to Ubuntu 14.04.
Install required packages to begin with.
```
# Install Apache and WSGI for Python 3
apt-get -y install apache2 libapache2-mod-wsgi-py3

# Install pip for Python 3
apt-get -y python3-pip

# Install required Python packages
pip3 install flask boto3
```
Create the WSGI file that Apache will use to hook into the Python application.
I placed mine under /var/www/homework.
```
import sys,os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

from homework.homework import app as application
```
Create an apache site. On Ubuntu, they file should go into /etc/apache2/sites-available/. I call mine homework.conf.
```
<virtualhost *:80>
    ServerName homework.cristian-contreras.me
    WSGIScriptAlias / /var/www/homework/homework.wsgi
    <Directory /var/www/homework>
        Order deny,allow
        Allow from all
    </Directory>
</virtualhost>
```
Enable the web site and restart the Apache service.
```
a2ensite homework
service apache2 restart
```
