# Root One Foods

## Overview

### What is the app for?



### What does it do?



### How does it work?



## Features

### Existing features

- User based
    - Interactive Graphs

- Display features
    - Home page
    - Dashboard page containting interactive graphs
    - Analysis of Graphs and plans
    - Contact page
    - Interactive graphs:
    	- Selectors for Donation County and Donation District
    	- Number displays to show total number of donations and amount in donations in USD
        - Number of donations over 5 years in USD (Line Graph)
        - Resource allocation by metro type (Row Graph)
        - Resource allocation by Primary Subject (Row Graph)
        - Allocation by Poverty (Pie)
        - Year Selector (Pie)

## Tech Used

- [Django] (http://flask.pocoo.org/)
    - We use **Django** as our framework for python.
- [Bootstrap] (http://getbootstrap.com/)
    - We use **Bootstrap** to give our webapp a responsive layout.
- [JQuery] (https://jquery.com/)
    - We use **JQuery** to produce a more interactive webapp. 
- [MongoDB] (https://www.mongodb.com/)
    - We use **MongoDB** for our NoSQL database. and local server testing. 

## Testing

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