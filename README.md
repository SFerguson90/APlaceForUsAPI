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

## Technical Information
* **Language**: Python 3.7
* **Framework**: Flask 1.0.3
* **Database**: PostgreSQL / pgAdmin 4
* **Tested With**: Postman
