# babalada

Project Stock Simulator

Login Tutorial for refrence
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

# creates virtual environment

    python -m venv venv

# activate environment

    source venv/bin/activate

# install requred packages

    pip install requirements.txt

# Steps to set up local environment

export FLASK_APP=auth
export PG_PASSWD=<<PASSWORD>>
export PG_USR=<<USERNAME>>
export PG_URL=<<URL>>

# Run app locally

flask run
