Django Docker Launchpad
-
## Main Features
- #### Docker Django Web App Development
- #### Docker Django REST API Web App Development
- #### Production Security Settings for both Django and Django REST
- #### Heroku PostgreSQL for Production
- #### Heroku Deployment via Docker
- #### Amazon S3 for users uploads (media files)
- #### User email signup and OAuth social login with GitHub


### Tools and Settings:
##### Django Debug Toolbar and Django Extension on Development
>This is a recommended security measure not to reveal the admin login page

##### Custom admin url (instead of django's default 'admin')
>This is a recommended security measure not to reveal the admin login page

##### WhiteNoise for serving staticfiles 
>Making static files a self-contained unit that can be deployed anywhere 
without relying on nginx, Amazon S3 or any other external service.

##### Gunicorn Python WSGI HTTP UNIX Server 
>Production level WSGI server; Simply implemented, light on server resource usage, and fairly speedy. It natively supports WSGI, Django, and Paster.

##### DJ-Database-URL
>Simple utility to convert DATABASE_URL environment variable to configure database credentials and settings.
>
