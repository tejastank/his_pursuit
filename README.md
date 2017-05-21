# pursuit

pursuit is a tailoring ordering system. It is built with [Python][3.5.2] using the [Django Web Framework][1.11].

This project has the following basic apps:

* pursuit  (the main app for settings)
* accounts
* profiles
* sales

## Tool Sets

* Django Crispy Forms 1.6.1
* Bootstrap 3.3.7
* Jquery 3.2.1
* Jquery UI 1.12.1
* ReactJS 15.3.1

The project skeleton is built based on Django Edge.  Read this link for details.  This has explain how to change the development database.
https://django-edge.readthedocs.io/en/latest/

## IDE
Eclipse with pydev or LiClipse

## Work Submit
All your work should be submitted in a seperate branch.  Don't commit to master directly.  
This is how we make sure only good codes will be merged to master.
I will merge everbody's code into the master branch in every 2 - 3 days.  
Please make sure you merge back the changes to your branch after master is updated, or, to make it simple, create a new branch afterwards.

To create a seperate branch, run:

```
git checkbout -b [new-branch-name]
```

## Installation

### Install all dependencies:

```
pip install -r requirements.txt
```
	
### Install Webpack (For ReactJS):
Go to /src/static folder

```
npm install
```

## Database Models and Migration
Other than accounts and profiles, all data models should be placed in the pursuit app.

To do migration in pursuit, run below command in the src folder:

```
python manage.py makemigrations pursuit
```

To make migration, run below command:

```
python manage.py migrate
```

To set initial data:

```
python manage.py loaddata dev_only
```


### Compile ReactJS
You need to compare ReactJS again everytime after changing the jsx code.  Execute this under in src\static folder

    node_modules\.bin\webpack --config webpack.config.js

## Forms
* Simple forms should be done by using crispy_form.
* Complicated forms like modifying sales order should be done by using ReactJS for better UI interaction.

## Layout
The page is designed to have the best looking in iPad Portrait size.  Be aware of the bootstrap columns setting you are using.
http://mspangenberg.github.io/Bootstrap-3-Grids/devices.html

## Business Logic
Business logic should be placed under a service class.  See sales.services.salesorder.py for example.

## Default Login
admin@abc.com / 1234