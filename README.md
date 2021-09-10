# APlaceForUs API

## First Use - Creating an Account

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

## Technical Information
* **Language**: Python 3.7
* **Framework**: Flask  1.0.3
* **Database**: PostgreSQL / pgAdmin 4
* **Tested With**: Postman
