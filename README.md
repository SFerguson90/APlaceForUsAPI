# APlaceForUs API

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

## API Functionality

* A POST method to the /token endpoint will return an access_token.

```
    {
        "email": "fakeEmail@fakeMail.com"
        "password": "fakePassword"
    }
```
* A GET method to the /me endpoint using the access_token will return user information. The KEY must be "Authorization", VALUE "Bearer asdfl;kadfa;ldfj".
```
    {
        "id": 1,
        "username": "fakeName",
        "email": "fakeEmail@fakeMail.com"
    }
```
## Technical Information
* **Language**: Python 3.7
* **Framework**: Flask 1.0.3
* **Database**: PostgreSQL / pgAdmin 4
* **Tested With**: Postman
