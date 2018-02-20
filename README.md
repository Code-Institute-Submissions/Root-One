# Root One Foods

## Overview

### What is the app for?

This app is an e-commerce web app for Root One foods. Root One Foods is a food production start up currently specialising in chickpea based pasta. 

### What does it do?

The app will serve as a place for users to:

- Learn about Root One, who they are, and what they do. 
- Check updates on the companies products
- View Root One's social media platforms
- Take a look at Root One's products and choose to buy them using PayPal
- View Recipes posted by Root One as well as being able to comment on certain recipes. 
- Register and log in to the site in order to make payments to purchase products.

### How does it work?

This is an App using the Django frame work to host a dynamic, multi functional web app made up of multiple python packages.
Python packages used are: 
- Accounts - For managing user accounts as well as super users.
- Paypal store - For managing paypal payments from users. 
- Products - For managing product libraries
- Recipes Blog - A blog to post recipes for users to view and comment on. 
	
Packages are rendered into views and displayed in the frontend using templates written in HTML, CSS and Javascript.

## Features

### Existing features

- User based
    - Register to become member of the site
    - Log in and Log out of account
    - Purchase Products using Pay Pal
    - Comment on Recipes

- Display features
    - Home page
    - Home Page Updates Using Flat Pages
    - About Us page
	- View of Recipes posted on the Recipes Blog
	- View of current product range
    - Contact page

## Tech Used

- [Django] (https://www.djangoproject.com/)
    - We use **Django** as our framework for python.
- [Bootstrap] (http://getbootstrap.com/)
    - We use **Bootstrap** to give our webapp a responsive layout.
- [JQuery] (https://jquery.com/)
    - We use **JQuery** to produce a more interactive webapp. 
- [MongoDB] (https://www.mongodb.com/)
    - We use **MongoDB** for our NoSQL database. and local server testing. 
- [Disqus] (https://disqus.com/api/docs/)
    - We use **Disqus** to allow for users to comment on recipes in the Recipes Blog.
- [Django Paypal] (https://django-paypal.readthedocs.io/en/stable/)
    - We use **Django Paypal** to allow for users to make purchases of products in the product range.

## Testing Done
- HTML testing using HTML validator (https://validator.w3.org/)
- CSS testing using CSS validator (http://www.css-validator.org/)
- Javascript testing using JSHint (http://jshint.com/)
- Python testing using PEP8 Tool (http://pep8online.com)
- UX testing used by trialling with external parties.
- Performance testing by measuring load times and reducing.
- Stress testing done by using limited browser functionality. 
- Mobile adaptibility tested on various devices.

## Contributing

### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've done that you'll need to make sure that you have tools from the requirements.txt file. To do this you'll need to: 
  1. cd to the directory with the requirments.txt file is located.
  2. Then you'll need to activate your local environment.
  3. Then you'll need to run: 
    '''
    pip install -r requirements.txt
    '''
3. Once **requirements.txt** is installed run **heroku local -f Procfile.local** from your virtual environment.
4. The project will now run on [localhost](http://127.0.0.1:5000)
5. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

Thanks given to the Code Institute for guidance and teaching to assist in making this app. 
Thanks also given to Root One for providing of content and testing of App usability. 
Other organisation's content that assisted in the creation of this web app: 
- W3schools
- DJango official documentation
- Assistance for troubleshooting with Stack Overflow
	
