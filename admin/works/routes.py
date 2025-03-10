from . import works_bp
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_ckeditor import CKEditor
from models import db, Works
from .forms import WorksForm
from helpers import *
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_logged_in'):
            return redirect(url_for('app.login'))
        return f(*args, **kwargs)
    return decorated_function

@works_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    works = Works.query.all()
    return render_template('admin/works/index.html', works=works)


@works_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    workForm = WorksForm()
    if request.method == 'POST':
        image = request.files['image']
        file_size = request.content_length
        extension = get_file_extension(image.filename)
        allowed_ext = ['jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG', 'PNG', 'GIF']
        
        if extension in allowed_ext and file_size < 1024*1024*5:
            img_name = random_filename_for_works(image.filename)
            save_file(image, 'app/static/uploads', img_name)
        else:
            return redirect(url_for('admin.works.add'))
        
        work = Works(
            title = workForm.title.data,
            image = img_name,
            detail = workForm.detail.data,
        )
        db.session.add(work)
        db.session.commit()
        return redirect(url_for('admin.works.index'))
    return render_template('admin/works/add.html', workForm=workForm)


@works_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    work = Works.query.get(id)
    get_name_for_delete = work.image
    if request.method == 'POST':
        image = request.files['image']
        new_name = random_filename_for_works(image.filename)
        save_file(image, 'app/static/uploads', new_name)
        work.title = request.form['title']
        work.image = new_name
        work.detail = request.form['detail']
        db.session.commit()
        delete_file_from_folder(get_name_for_delete, 'app/static/uploads')
        return redirect(url_for('admin.works.index'))
    return render_template('admin/works/update.html', work=work)

@works_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    work = Works.query.get(id)
    file_name_for_delete= work.image
    delete_file_from_folder(file_name_for_delete, 'app/static/uploads')
    db.session.delete(work)
    db.session.commit()
    return redirect(url_for('admin.works.index'))