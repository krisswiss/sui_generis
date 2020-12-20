# Sui Generis
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
    - [**Features Left to Implement**](#features-left-to-implement)
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

## UX
### Project Goals
The aim of the project is to create a ecommerce website where users can view, sort and choose different products in the gallery, get through the checkout process with their shopping bag and make a card payment through Stripe. The user can also create a personal profile where the can see all their historic order details.
### Site Owner Goals
To create a premium brand offering unique, handmade hampers that users can build from available products.
### User Stories
- As a **shopper** I want to:
  - access website from any device
  - view a list of all products so I can identify product, price and see picture
  - view individual product details
  - view a list of products within certain category
  - view a list of products sorted by name, price or category
  - search products by name in a serachbox
  - have an overview of my shopping bag and total amount to pay
  - modify or remove products in shopping bag
  - see updated shopping bag
  - easily and secure pay for my shopping
  - get order confirmation after payment/placing an order
  - read more about the company
  - contact the company directly
  - follow the company on social media
- As a **user** I want to:
  - login anytime, so that I can get access to my saved profile details and make next purchase quicker
  - see my order history
  - see and/or update my delivery details
  - be able to change my password, so that I can create the stronger password
- As a **staff member / admin** I want to:
  - have convenient and secure admin interface avalable only for website admin, so that I can add, edit and remove products
  - receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries
  - be able to hide out of stock products from displaying to the users
  - add, edit or remove faq section
  - add, edit or remove social links

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

### Features Left to Implement


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


    