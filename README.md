# poehub


Web-based interface for the data in Content.ggpk.

[![Build Status](https://travis-ci.org/henrikolsson/poehub.svg)](https://travis-ci.org/henrikolsson/poehub)

## Running

Install dependencies:

    $ pip install -r requirements.txt

Create database model (make sure the database settings in poehub/settings.py are valid first:

    $ python manage.py syncdb
    
Extract data from Content.ggpk:

    $ PYTHONPATH=. python ggpk/ggpk.py ~/Content.ggpk

Insert data into database:    

    $ python main.py 
    
Run web:

    $ python manage.py runserver
