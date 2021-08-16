Flask MKAD Distance Calculator
==============================

## This simple webapp was made for training purposes, *through a test*.

Obs: 

    # is incomplete.

Missing:

    # Unit tests
    # Corner Cases
    # More 'Forms' validations
    # And a lot of things (for sure) ;)

Dependencies
============
- Python==3.9.6
- Docker (https://www.docker.com/products/docker-desktop) * (optional).
- APIKEY from: https://positionstack.com/?utm_source=apilayer_home&utm_medium=Direct&utm_campaign=apilayer_home_products

Installation
============
- `clone` the project.
- Setup a `venv`, `activate`
- Install `requirements.txt` -> (pip install -r requirements.txt)
- Run the follow command inside `flask` folder: `python run.py`
- You can access through the address displayed.(default: http://127.0.0.0:5000).
- Create a `.env` file in the `/myapp/` folder.
  - SECRET_KEY=`CREATE_ONE`
  - YOUR_ACCESS_KEY=`YOUR_API_KEY_HERE`


Installation with docker-compose
===================================
- `clone` the project.
- Install `docker` and `docker-compose`
- Run the follow command inside the folder where docker-compose.yml where located `docker-compose up --build`
- Wait for the process to finish.
- You can access through the address.(default: http://127.0.0.0)
- Create a `.env` file in the `/myapp/` folder.
  - SECRET_KEY=`CREATE_ONE`
  - YOUR_ACCESS_KEY=`YOUR_API_KEY_HERE`


