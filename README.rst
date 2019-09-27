Payinv
======
Payinv is a control system for Sales <-> Invoices And Payments for Customer.


Software Stack
--------------
The code base is written using the `Django <https://www.djangoproject.com/>`_ with `PostgreSQL <https://www.djangoproject.com/>`_ as database.

Includes the follow Javascripts and CSS libraries and toolkit
 - `Bootstrap <https://getbootstrap.com/>`_
 - `Font-Awesome  <https://fontawesome.com/>`_
 - `jQuery <https://jquery.com/>`_


To change the backend database should set this into the file  `src/payinv/settings/base.py` in
the `DATABASES` section.


Installing
----------

First to all you be sure in your system has installed Python 3, PostgreSQL and NPM

#. With npm install CSS/Javascript dependencies::

    npm install
#. Create a database in your PostreSQL called `payinv_production` and the role 
   permission for user `payinv`
#. Set credentials

   A) You can edit directly the file  `src/payinv/settings/base.py` and set the 
      database connection credencials and 
      `SECRET_KEY <https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECRET_KEY>`_

   B) Other way is set by environment variables::

       export PAYINV_ENVIRONMENT=production
       export PAYINV_DATABASE_PASSWORD=mypassword
       export PAYINV_SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64|head -n 1)
#. Install dependencies and set Python enviroment::

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

#. Run init script::

   ./run-payinv.sh



