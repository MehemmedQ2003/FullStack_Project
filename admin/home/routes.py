from . import home_bp
from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Home
from .forms import HomeForm
from helpers import *
from datetime import datetime

@home_bp.route('/', methods=['GET', 'POST'])
def index():
    home_datas = Home.query.all()
    return render_template('admin/home/index.html', home_datas=home_datas)


@home_bp.route('/add', methods=['GET', 'POST'])
def add():
    homeForm = HomeForm()
    if request.method == 'POST':
        image = request.files['image']
        file_size = request.content_length
        extension = get_file_extension(image.filename)
        allowed_ext = ['jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG', 'PNG', 'GIF']
        
        if extension in allowed_ext and file_size < 1024*1024*5:
            img_name = random_filename_for_home(image.filename)
            save_file(image, 'app/static/uploads', img_name)
        else:
            return redirect(url_for('admin.home.add'))
        home_data = Home(
            title = homeForm.title.data,
            image = img_name,
            description = homeForm.description.data,
        )
        db.session.add(home_data)
        db.session.commit()
        return redirect(url_for('admin.home.index'))
    return render_template('admin/home/add.html', homeForm=homeForm)



@home_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    home_data = Home.query.get(id)
    get_name_for_delete = home_data.image
    if request.method == 'POST':
        image = request.files['image']
        new_name = random_filename_for_home(image.filename)
        save_file(image, 'app/static/uploads', new_name)
        home_data.image = new_name
        home_data.title = request.form['title']
        home_data.description = request.form['description']
        db.session.commit()
        delete_file_from_folder(get_name_for_delete, 'app/static/uploads')
        return redirect(url_for('admin.home.index'))
    return render_template('admin/home/update.html', home_data=home_data)


@home_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    home_data = Home.query.get(id)
    file_name_for_delete= home_data.image
    delete_file_from_folder(file_name_for_delete, 'app/static/uploads')
    db.session.delete(home_data)
    db.session.commit()
    return redirect(url_for('admin.home.index'))
