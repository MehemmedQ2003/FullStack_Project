from . import admin_bp
from flask import render_template, session, redirect, request
from flask import url_for
from datetime import datetime
from models import *
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_logged_in'):
            return redirect(url_for('app.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/')
@login_required
def index():
    return render_template('admin/index.html')