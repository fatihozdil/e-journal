# E-journal

- This project was developed within the Mediterranean Informatics Community in 2020.
- I wrote the front-end by myself using html, css, bootstrap.
- Its backend was written by batuhan bag.
- The purpose of this project was to publish a journal on behalf of the university and to publish technological articles.

it is hosted in azure [web site link](https://e-journal.azurewebsites.net/)

Since the project was not published within the university, I published this project myself.

## Local Installation

Create a virtual environment for the app:

```bash
    python3 -m venv .venv
    source .venv/bin/activate
```

Install the dependencies:

```bash
    pip install -r requirements.txt
```

Run the sample application with the following commands:

```bash
    # Run database migration
    python manage.py migrate
    # Run the app at http://127.0.0.1:8000
    python manage.py runserver
```

## Publishing to the azure server

check the below link which is created by Microsoft:  
[Link](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=django%2Cmac-linux)
