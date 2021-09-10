# APlaceForUs API

## First Use - Creating an Account

To use the API, an account must first be created. This happens through a POST request to the /users endpoint. Users can feel safe, knowing their passwords are SHA256 encrypted, when stored in the database.

![NewUserCreated](/testPictures/newAccountPost.jpg "New account created")

## Email Verification with Mailgun API

After having created an account, the user will be sent a verification email to their email address. Be sure to check the spam folder!

![MailGunAPI](/testPictures/accountVerification.jpg "MailGun API")

## Logging in and receiving a JSON Web Token

By passing email and password as keys with their respective values to the /tokens endpoint, a user is given a Bearer, with which they can log in.

![LoginSuccess](/testPictures/accountLogInSuccess.jpg "Logging in")

## Post your dog

Once an account is created and the user has logged in, they may share their dog's information!

![DogPostSuccess](/testPictures/dogPostSuccess.jpg "Uploading Dog Profile")

## Change your avatar

Don't like your avatar picture? Let's change it!

![AvatarChangePict](/testPictures/avatarPUTsuccess.jpg "Changing User Avatar")

## Deployed and running on Heroku

All of this is available from the Heroku platform!

![HerokuPict](/testPictures/herokuSuccessPost.jpg "Functionality on Heroku")

## HTTP Methods - as of 9/10/2021

These are all of the HTTP methods tested and available to users. Many have JWT (JSON Web Token) Requirements. This authentication prevents manipulation and provides basic security.

![HTTPMethods](/testPictures/HTTPMethods91021.jpg "HTTP Method Functions")

## Technical Information
* **Language**: Python 3.7
* **Framework**: Flask  1.0.3
* **Database**: PostgreSQL / pgAdmin 4
* **Tested With**: Postman
