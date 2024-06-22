from . import whatsapp_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Whatsapp
from .forms import WhatsappForm
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_logged_in'):
            return redirect(url_for('app.login'))
        return f(*args, **kwargs)
    return decorated_function

@whatsapp_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    whatsappNums = Whatsapp.query.all()
    return render_template('admin/whatsapp/index.html', whatsappNums=whatsappNums)


@whatsapp_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    whatsappNumsForm = WhatsappForm()
    if request.method == 'POST':
        whatsappNum = Whatsapp(
            name = whatsappNumsForm.name.data,
            number = whatsappNumsForm.number.data
        )
        db.session.add(whatsappNum)
        db.session.commit()
        return redirect(url_for('admin.whatsapp.index'))
    return render_template('admin/whatsapp/add.html', whatsappNumsForm=whatsappNumsForm)


@whatsapp_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    whatsappNum = Whatsapp.query.get(id)
    if request.method == 'POST':
        whatsappNum.number = request.form['number']
        whatsappNum.name = request.form['name']
        db.session.commit()
        return redirect(url_for('admin.whatsapp.index'))
    return render_template('admin/whatsapp/update.html', whatsappNum = whatsappNum)


@whatsapp_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    whatsappNum = Whatsapp.query.get(id)
    db.session.delete(whatsappNum)
    db.session.commit()
    return redirect(url_for('admin.whatsapp.index'))