from . import contact_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import db, Contact
from .forms import ContactForm
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_logged_in'):
            return redirect(url_for('app.login'))
        return f(*args, **kwargs)
    return decorated_function

@contact_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    contacts = Contact.query.all()
    return render_template('admin/contact/index.html', contacts=contacts)


@contact_bp.route('/add', methods=['GET', 'POST'])
def add():
    contactForm = ContactForm()
    if request.method == 'POST':
        contact = Contact(
            country = contactForm.country.data,
            city = contactForm.city.data,
            title = contactForm.title.data,
            address = contactForm.address.data,
            address_link = contactForm.address_link.data,
            phone = contactForm.phone.data,
            email = contactForm.email.data,
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('admin.contact.index'))
    return render_template('admin/contact/add.html', contactForm=contactForm)


@contact_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.country = request.form['country']
        contact.city = request.form['city']
        contact.title = request.form['title']
        contact.address = request.form['address']
        contact.address_link = request.form['address_link']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        db.session.commit()
        return redirect(url_for('admin.contact.index'))
    return render_template('admin/contact/update.html', contact = contact)


@contact_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('admin.contact.index'))