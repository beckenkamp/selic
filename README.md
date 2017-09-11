# selic

## Installation
Clone this repo. Make a virtualenv and run the Flask app. Access it through `http://127.0.0.1:5000/`.

    $ git clone https://github.com/beckenkamp/selic.git
    $ cd selic
    selic$ mkvirtualenv selic_env --python=python3.6  # Choose your favorite virtualevn and create it with Python 3.6
    (selic_env)selic$ pip install -r requirements.txt
    (selic_env)selic$ export FLASK_APP=app.py
    (selic_env)selic$ export FLASK_DEBUG=1  # To activate the debug server
    (selic_env)selic$ flask run
     * Serving Flask app "app"
     * Forcing debug mode on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
