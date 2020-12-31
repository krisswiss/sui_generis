# Sui Generis
The live website can be viewed [here](https://sui-generis.herokuapp.com/)  

Sui Generis meaning “one of a kind” or “unique” is the exact description of this business model.

The aim of the company is to offer customers a unique shopping experience by giving them a choice of buying ready-made hampers or the chance to create their own without a limit on product selection.

Stock images have been used for this project but the companies aim would be to offer brands that are not in the mainstream market which would then truly reflect the name Sui Generis.


---


## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Site Owner Goals**](#site-owner-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement and Future development plans**](#features-left-to-implement-and-future-development-plans)
3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Modelling**](#data-modelling)

4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)

5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Content and Media**](#content-and-media)
    - [**Acknowledgements**](#acknowledgements)
8. [**Disclaimer**](#disclaimer)

---

## UX
### Project Goals
The aim of the project is to create a ecommerce website where users can view, sort and choose different products in the gallery, get through the checkout process with their shopping bag and make a card payment through Stripe. The user can also create a personal profile where the can see all their historic order details.
### Site Owner Goals
To create a premium brand offering unique, handmade hampers that users can build from available products.
### User Stories

##### Shopper
  - As a user, I want to access website from any device
  - As a user, I want to view a list of all products so I can identify product, price and see picture
  - As a user, I want to view individual product details
  - As a user, I want to view a list of products within certain category
  - As a user, I want to view a list of products sorted by name, price or category
  - As a user, I want to search products by name in a serachbox
  - As a user, I want to have an overview of my shopping bag and total amount to pay
  - As a user, I want to modify or remove products in shopping bag
  - As a user, I want to see updated shopping bag
  - As a user, I want to easily and secure pay for my shopping
  - As a user, I want to get order confirmation after payment/placing an order
  - As a user, I want to read more about the company
  - As a user, I want to contact the company directly
  - As a user, I want to follow the company on social media
  - As a user, I want to read company blog
##### Registered User
  - As a user, I want to login anytime, so that I can get access to my saved profile details and make next purchase quicker
  - As a user, I want to see my order history
  - As a user, I want to see and/or update my delivery details
##### Staff Member / Admin
  - As a user, I want to have convenient and secure admin interface avalable only for website admin or staff member
  - As a user, I want to be able to add products
  - As a user, I want to be able to edit products
  - As a user, I want to be able to remove products
  - As a user, I want to receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries
  - As a user, I want to add question to faq section
  - As a user, I want to edit question in faq section
  - As a user, I want to remove question from faq section
  - As a user, I want to add post to blog section
  - As a user, I want to edit post in blog section
  - As a user, I want to remove post from blog section

### Design
Website has been built with [Bootstrap](https://www.bootstrapcdn.com/) components. I have chosen it chosen for this project for its modern interface, ease of use and ability to be easily customized. It is used for creating features such as navbar, cards, forms, modals, as well as for the layout(grid).
### Color Scheme
Choice of colors was dictated by premium appeal of the brand.

### Wireframes

Original wireframes for desktop, tablet and mobile can be found [here](https://github.com/krisswiss/sui_generis/tree/master/wireframes).


---


## Features

### Existing Features

* Navigation(fixed at the top) containing:
  * links to access all sections(home, about us, hampers, products)
  * searchbox to serch for products by name
  * my account button
  * cart
* Home:
  * Button to show current specials
* Products view which:
  * displays ready made hampers and individual products
  * contains sorting by: category, name, price
* My Account:
  * Users can register, login and view their details and history of the orders
  * Admin / staff can modify products
* Cart:
  * products can be added, viewed, modified or removed
  * delivery threshold is being automatically calculated
* Checkout:
  * users can pay for the products
  * payments are being processed with Stripe
  * confirmation emails are sent to the users

### Features Left to Implement / Future development plans

  - I have started a new app called social, which will contain model for social icons, so store staff can change and modify social icons and links.
  - I would like to include functionality for store staff to update background picture, so they can change it when the theme of hampers change.
  - I also would like to finish my products functionality, so only in stock products will display.
  - I would like to add Pagination when there are many products accumulated in the product gallery.
  - I would like to Add 404 page, for better UX.

---

## Information Architecture
### Database Choice
During the development phase I worked with sqlite3 database which is installed with Django.
For deployment(production), a PostgreSQL database is provided by Heroku as an add-on.
* [PostgreSQL](https://www.postgresql.org/)
* [Sqlite3](https://www.sqlite.org/index.html)

### Data Modelling
#### Products App
##### Product
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
 category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 sku | CharField | max_length=254, null=True, blank=True
 name | CharField | max_length=254 
 description | TextField | 
 price | DecimalField |max_digits=6, decimal_places=2] 
 image_url | URLField | max_length=1024, null=True, blank=True
 image| ImageField | null=True, blank=True
 in_stock | BooleanField | default=True, null=True, blank=True

##### Category
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
name | CharField | max_length=254
friendly_name | CharField | max_length=254, null=True, blank=True

#### Profile App
##### Profile
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
 user | OneToOneField 'User' |  on_delete=models.CASCADE
 profile_phone_number | CharField | max_length=20, null=True, blank=True
 profile_address1 | CharField | max_length=80, null=True, blank=True
 profile_address2 | CharField | max_length=40, null=True, blank=True
 profile_town_or_city | CharField | max_length=80, null=True, blank=True
 profile_county | CharField | max_length=50, null=True, blank=True
 profile_postcode | CharField | max_length=20, null=True, blank=True
 profile_country | CountryField | blank_label='Country', null=True, blank=True

#### Checkout App
##### Order
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
 order_number | CharField | max_length=32, null=False, editable=False
 user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 full_name | CharField | max_length=50, null=False, blank=False
 email | EmailField | max_length=254, null=False, blank=False
 phone_number | CharField | max_length=20, null=False, blank=False
 country | CharField | blank_label='Country *', null=False, blank=False
 postcode | CharField | max_length=20, null=True, blank=True
 town_or_city | CountryField | max_length=40, null=False, blank=False
 street_address1 | CharFieldmax | max_length=80, null=False, blank=False
 street_address2 | CharField | max_length=80, null=True, blank=True
 county | CharField | max_length=80, null=True, blank=True
 date | DateTimeField | auto_now_add=True
 delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
 order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 original_bag | TextField | null=False, blank=False, default=''
 stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

##### OrderLineItem
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE
quantity | IntegerField | null=False, blank=False, default=0
lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

##### Post
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
title | CharField | max_length=254
introduction | CharField | max_length=254
post | TextField | null=False, blank=False
image_url | URLField | max_length=1024, null=True, blank=True
image | ImageField | max_length=1024, null=True, blank=True
date | DateField | auto_now_add=True

##### Faq
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
question | CharField | max_length=254
answer | TextField | null=False, blank=False

##### Social
| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
name | CharField | max_length=50
weblink | URLField |
icon | CharField | max_length=50


---

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python to display data within HTML

### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap](https://www.bootstrapcdn.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [JQuery](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions.
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style Django forms.

### Tools
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [Heroku](https://heroku.com/) - to host the project.
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static and media files in prodcution.
- [Coolors.co](https://coolors.co/) - to create colour palette used in the README.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.

---

## Testing


---

## Deployment
Sui Generis project was developed using the [GitPod](https://www.gitpod.io/) online IDE and
using Git & GitHub for version control. It is hosted on the [Heroku](https://heroku.com/) and user-uploaded images being hosted in AWS S3 Basket.
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE of your choice (I used [GitPod](https://www.gitpod.io/) for creating this project)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/download/releases/3.0/)    

Apart from that, you also need to create accounts with the following services:
- [Stripe](https://stripe.com/en-ie)
- [AWS](https://aws.amazon.com/) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Gmail](https://mail.google.com/)

#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/krisswiss/sui_generis`    
Alternatively, you can save a copy of this repository by clicking the green button **Clone or download** , then **Download Zip** button, and after extract the Zip file to your folder.      
In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).       

Note: You can read more information about the cloning process on the [GitHub Help page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).   

2. Set up environment variables.     
Note, that this process will be different depending on IDE you use.   
In this one it was done using Gitpod IDE Settings in the following way:      
    - in GitPod Settings press Add Variable button
    - in Name column, put name of the environment variable
    - in Value column, put the value for the variable
    - in path column, use the following syntax: 'your_username/*'    
    
Variables have then been imported in settings.py:

    
    import os  
    os.environ["DEVELOPMENT"] = "True"    
    os.environ["SECRET_KEY"] = "<Your Secret key>"    
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"

       
Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys)
    
3. Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`     
4. In the terminal in your IDE migrate the models to crete a database using the following commands:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     
5. Load the data fixtures(**categories**, **products**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`        
6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`   
7. You will now be able to run the application using the following command:     
`python3 manage.py runserver`     
8. To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

### Heroku Deployment
*To start Heroku Deployment process, you need to clone the project as described in the [Local deployment](#local-deployment) section above.*     
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:    
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:    
`pip3 freeze > requirements.txt`    
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:      
`web: gunicorn sui_generis.wsgi:application`    
3. `git add`, `git commit` and `git push` these files to GitHub repository.     
NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but illistrated here as they are required for the successfull deployment to Heroku.        
As well as that, other things that are required for the Heroku deployment and have to be installed: **gunicorn** (WSGI HTTP Server), **dj-database-url** for database connection and **Psycopg** (PostgreSQL driver for Python). All of the mentioned above are *already installed* in this project in the requirements.txt file.     
4. On the [Heroku](https://heroku.com/) website you need to create a **new app**, assign a name (must be unique),set a region to the closest to you(for my project I set Europe) and click **Create app**.   
5. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type `postgres`), select **Hobby Dev — Free** and click **Provision** button to add it to your project.     
6. In Heroku **Settings** click on **Reveal Config Vars**.   
7. Set the following config variables there (Postgres, database url, should be set automatically after instal from previous steps):     

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |
| DATABASE_URL | `postgres://<your link> `|
     
8. Copy **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in **settings.py**.     
You can temporary comment out the current database settings code and just paste the following in the settings.py:   
```bash 
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
  ```
Important Note: that's just temporary set up, this URL **should not be committed and published to GitHub** for security reasons, so makse sure not to commit your changes to Git while the URL is in the settings.py.     
9. Migrate the database models to the Postgres database using the following commands in the terminal:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     
10. Load the data fixtures(**categories**, **products**) into the  Postgres database using the following command:     
`python3 manage.py loaddata <fixture_name>`      
11. Create a **superuser** for the Postgres database by running the following command(*you need to follow the instructions and inserting username,email and password*):      
`python3 manage.py createsuperuser`     
12. You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.    
Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.     
13. Add your Heroku app URL to **ALLOWED_HOSTS** in the settings.py file.
14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.    
To do so, from the Heroku dashboard follow the steps:
-  **Deploy** section -> **Deployment method** -> select **GitHub**
-  link the Heroku app to your GitHub repository for this project
- click **Enable Automatic Deploys** in the Automatic Deployment section
- Run `git push` command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.     

Alternatively, in the terminal you can run:    
- `heroku login`    
-  after adding and comitting to Git, run the following command:     
`git push heroku master`
15. After successful deployment, you can view your app bu clicking **Open App** on Heroku platform.
16. You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!    
##### Hosting media files with AWS
The **static files** and **media files** (that will be uploaded by superuser - product/service images) are hosted in the [AWS S3 Bucket](https://aws.amazon.com/). To host them, you need to create an account in AWS and create your S3 basket with *public access*. More about setting it up you can read in [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) and [this tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).
##### Senging email via Gmail
In order to send real emails from the application, you need to connect it to your **Gmail account**, setting up your **email address** in EMAIL_HOST_USER variable and your **app password** generated by your email provider in EMAIL_HOST_PASS variable.

---

## Credits
### Code
- 
- 
- 

### Content and Media
- 
- 
- 


### Acknowledgements
    
-        
-
-       

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Disclaimer
For **educational purposes** only.        


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>