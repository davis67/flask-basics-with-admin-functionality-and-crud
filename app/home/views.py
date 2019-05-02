from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the home page on / route
    """
    return render_template('home/index.html', title="welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
        Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="dashboard")