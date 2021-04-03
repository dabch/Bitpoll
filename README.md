# Bitpoll

Bitpoll is a software to conduct polls about Dates, Times or general Questions.


This is a new version of the Dudel from opatut (<https://github.com/opatut/dudel>) used on <mafiasi.de>, rewritten using the Django framework as a backend.

# Install

Get the code:

~~~
git clone https://github.com/dabch/Bitpoll.git
~~~

Generate a Python virtualenv and install dependencies:

```
virtualenv -p $(which python3) .pyenv
source .pyenv/bin/activate
pip install -r requirements.txt
```

The following settings have to be adjusted to the intended production setting (but are not necessary for debugging):

* SECRET_KEY: This key should be set once on first install.
* FIELD_ENCRYPTION_KEY: `./manage.py generate_encryption_key`
* SOCIALACCOUNT_PROVIDERS: More infos are in the code.
* BASE_URL: Bitpoll app base url
* HOME_URL: Nextcloud instance base url
* ALLOWED_HOSTS: Bitpoll app base url / host

Initialise Database:

```
./manage.py migrate
```

Run Testserver:

```
./manage.py runserver
```

# Production

In production Senty is used for error reporting.

Install Dependencies for Production:

```bash
sudo apt install python3 python3-dev python3-pip python3-virtualenv
```

Install Python Dependencies

```
pip install -r requirements.txt
```

For Production systems it is nessesarry to run

```bash
./manage.py compilemessages
./manage.py collectstatic --no-input
```

And of course migrate the database for every production deploy

```bash
./manage.py migrate
```

# Apache Webserver Setup

We use an apache2 webserver in production which serves the bitpoll django application via the mod_wsgi module.

Install this module first (if it doesn't exist yet):

```
pip install mod_wsgi
```

Then, add the following line to your apache2 webserver config file (not the virtual host file):

```apache2
LoadModule wsgi_module <path-of-python>/dist-packages/mod_wsgi/server/mod_wsgi-<...>.so
WSGIPythonHome <path-to-virtual-environment-folder>
WSGIPythonPath <path-to-bitpoll-django-app>
```

To successfully serve the bitpoll application, we still need to correctly route the static files and give apache access 
to the wsgi.py entrypoint file. This code snipped has to be added to the **VirtualHost**-file which will be used for
serving the bitpoll application.

```apache2
Alias /static <repository_root_path>/_static

<Directory <repository_root_path>/_static>
    Require all granted
</Directory>

WSGIScriptAlias / <repository_root_path>/bitpoll/wsgi.py

<Directory <repository_root_path>/bitpoll>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
```

# Management of Dependencies

We use pip-tools to manage the dependencies.
After modification or the requirements*.in files or for updates of packages run

```bash
pip-compile --upgrade --output-file requirements.txt requirements.in
pip-compile --upgrade --output-file requirements-production.txt  requirements-production.in requirements.in
```

to sync your enviroment with the requirements.txt just run

```bash
pip-sync
```

this will install/deinstall dependencies so that the virtualenv is matching the requirements file
