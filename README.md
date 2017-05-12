

# pursuit

pursuit is a _short description_. It is built with [Python][3.5.2] using the [Django Web Framework][1.11].

This project has the following basic apps:

* accounts
* profiles
* sales
* pursuit  (the main app for settings)

## Installation

### Quick start

Install all dependencies:

    pip install -r requirements.txt
	
Install Webpack:
Go to /src/static folder

    npm install webpack --save-dev
    npm install --save react react-dom babel-core babel-loader babel-preset-react

Run migrations:

    python manage.py migrate
	
Compile ReactJS
Execute this under in src\static folder

    node_modules\.bin\webpack --config webpack.config.js

