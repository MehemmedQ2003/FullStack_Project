from . import technologies_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_ckeditor import CKEditor
from models import db, Technologies
from .forms import TechnologiesForm
from helpers import *
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_logged_in'):
            return redirect(url_for('app.login'))
        return f(*args, **kwargs)
    return decorated_function

@technologies_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    technologies = Technologies.query.all()
    return render_template('admin/technologies/index.html', technologies=technologies)


@technologies_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    technologyForm = TechnologiesForm()
    if request.method == 'POST':
        image = request.files['image']
        file_size = request.content_length
        extension = get_file_extension(image.filename)
        allowed_ext = ['jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG', 'PNG', 'GIF']
        
        if extension in allowed_ext and file_size < 1024*1024*5:
            img_name = random_filename_for_technology(image.filename)
            save_file(image, 'app/static/uploads', img_name)
        else:
            return redirect(url_for('admin.technologies.add'))
        
        technology = Technologies(
            title = technologyForm.title.data,
            image = img_name,
            content = technologyForm.content.data
        )
        db.session.add(technology)
        db.session.commit()
        return redirect(url_for('admin.technologies.index'))
    return render_template('admin/technologies/add.html', technologyForm=technologyForm)


@technologies_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    technology = Technologies.query.get(id)
    get_name_for_delete = technology.image
    if request.method == 'POST':
        image = request.files['image']
        new_name = random_filename_for_technology(image.filename)
        save_file(image, 'app/static/uploads', new_name)
        technology.title = request.form['title']
        technology.image = new_name
        technology.content = request.form['content']
        db.session.commit()
        delete_file_from_folder(get_name_for_delete, 'app/static/uploads')
        return redirect(url_for('admin.technologies.index'))
    return render_template('admin/technologies/update.html', technology=technology)

@technologies_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    technology = Technologies.query.get(id)
    file_name_for_delete= technology.image
    delete_file_from_folder(file_name_for_delete, 'app/static/uploads')
    db.session.delete(technology)
    db.session.commit()
    return redirect(url_for('admin.technologies.index'))