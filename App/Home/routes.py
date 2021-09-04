from App.Home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from App import login_manager
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')