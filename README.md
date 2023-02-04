# E-journal

- This project was developed within the Mediterranean Informatics Community in 2020.
- I wrote the front-end by myself using html, css, bootstrap.
- Its backend was written by batuhan bag.
- The purpose of this project was to publish a journal on behalf of the university and to publish technological articles.

it is hosted in azure [web site link](https://ejournal.fatihozdil.xyz/)

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

- Check the link which is created by Microsoft: [Link](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=django%2Cmac-linux)

## Delegating domain

[follow this link](https://learn.microsoft.com/en-us/azure/dns/dns-delegate-domain-azure-dns)

### Adding custom domain to the app service

- Go to the created dns zone. In the overview section click to the "Record Set"

- In the opened section put the name that you want to use as subdomain
select CNAME as type
- Put the url of the app service that u want to change

![](./mdAssets/Screenshot%20from%202023-02-04%2002-30-16.png)

- Go to resources and e-journal app service
- Click to the custom domains   
- In the opened section click to the Add custom domain  
- In the opened pane enter your domain 


![](./mdAssets/Screenshot%20from%202023-02-04%2002-37-19.png)

# !!! Don't forget to add the new domain to the allowed host in the production.py

## How to connect to the azure postgresql server

- First create a virtual machine  [follow these steps](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-connect-server-vnet#create-an-azure-linux-virtual-machine)  
- By following above link try to connect to the server from cli. 
- If you fail follow the 'vipullag-MSFT's solution: [link](https://learn.microsoft.com/en-us/answers/questions/1079890/download-ssh-private-key-(-pem))
- if you don't fail follow the 'vipullag-MSFT's yet.
- If you successfully connected to the server you can manage your database via cli. However it is not practical
- Install the pgAdmin [follow these steps](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/howto-connect?tabs=pgadmin)
- username is the user of the db
- password is the password if the db 
- These informations are in the configuration of the e-journal web app
- Also in the ssl section we need to add root certificate
- Download the certificate using below command
```bash  
 wget --no-check-certificate https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem
```
- After the steps in the link, additionally click to the ssh tunnel tab
- In the ssh tunnel tab host name is the public address of the VM that we used while we are connecting to the server from cli
- Username is the user of the VM that we used while connecting to the server from cli
- Choose the Identity file tab
- Choose your private key file (one without “.pub” extension). Or you can type path to the file into “Identity file” field by hand. [link for docs](https://medium.com/3-elm-erlang-elixir/faq-how-to-connect-pgadmin4-to-db-through-ssh-tunnel-with-public-key-authentication-b351750c20be)
- Click to the save 