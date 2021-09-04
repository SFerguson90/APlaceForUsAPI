# APlaceForUsGreyhounds API

 This is an API for the greyhound rescue organization "A Place For Us Greyhounds."

 https://www.aplaceforusgreyhounds.org

## First Use
It may be necessary to create a new environment for the API, because older libraries were used.
After having installed Python, go to the terminal and type:
    
    conda create --name apfug python=3.7

We then need to activate our new environment:

    conda activate apfug

All libraries required to run the API can be found in requirements.txt.

Change to the project directory in the terminal and type:

    pip install -r requirements.txt

This will install the framework and other libraries necessary to run the API.

## Database Information
PostgreSQL & pgAdmin 4 are recommended for establishing the API database. These are instructions for setting up said database. In the instructions, a password for the admin is established. It's recommended that you choose a stronger password and update the config.py file accordingly. The username may also need to be updated, should you choose something else.

After opening the GUI and logging in, the user will need to select "Login/Group Roles" on the left side.
Left-Click on the tab, and select Create > Login/Group Role...
Select General, populate "Name" with "apfugAdmin".
Select Definition, populate "Password" with "12345".
Select Privileges, switch "Can login?" to "Yes".

## API Functionality

* A POST method to the /token endpoint will return an access_token.
    {
        "email": "fakeEmail@fakeMail.com",
        "password": "fakePassword"
    }

* A GET method to the /me endpoint using the access_token will return user information. The KEY must be "Authorization", VALUE "Bearer asdfl;kadfa;ldfj".
    {
        "id": 1,
        "username": "fakeName",
        "email": "fakeEmail@fakeMail.com"
    }

## Technical Information
* **Language**: Python 3.7
* **Framework**: Flask 1.0.3
* **Database**: PostgreSQL / pgAdmin 4
* **Tested With**: Postman
