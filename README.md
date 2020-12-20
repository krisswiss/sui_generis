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
