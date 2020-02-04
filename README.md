# Mos'Gallery


## Description
A personal gallery application that displays my photos for others to see. You can visit the live site on `https://gallery100.herokuapp.com/`


## Author


* [**John Mbugua**](https://github.com/Jmos-Mbugua)

## Features


As a user of the application you will be able to:

1. See all posted photos
2. See each photo's description and location on hover.
3. Be able to copy a photo's url to the clipboard
4. Click on `view image` to expand a photo
5. Search for a photo by category e.g. _outdoor_, _photoshoot_

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View all posted photos  | Hover over a photo | Shown details about the photo | 
Details about the photo | Click on `Copy Link` | Pop up that shows that the image link has been copied appears |
|  Details about the photo | Click on `View Image`  | Photo expands |
|  Search in the search field | Input keywords to be searched then press ENTER | Search page is loaded and displays with the searched results |


## Getting started
### Prerequisites
* python3.6
* virtual environment
* pipenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/Jmos-Mbugua/Mos-Gallery
        $ cd Mos-Gallery

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ pipenv shell`
* Download pip in our environment using `$ pip3 install pipenv`
* Install all the dependencies from the requirements.txt file by running `python3.6 pipenv install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations photos
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py test 
        
## Technologies Used
* Python3.6
* Django
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Django](https://www.djangoproject.com/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)


## Support and Team
John Mbugua


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
