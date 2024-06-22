import os
def delete_file_from_folder(file_name,folder_name):
    try:
        os.remove(os.path.join(folder_name, file_name))
    except Exception as e:
        return str(e)
    return True

def allowed_file(filename, allowed_ext):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext

def save_file(file, folder_name,new_name = None):
    if new_name:
        file_name = new_name
    else:
        file_name = file.filename
    file.save(os.path.join(folder_name, file_name))
    return file_name

def random_filename_for_technology(file_name):
    import random
    extension = file_name.split('.')[-1]
    return 'technology' + '_' + str(random.randint(1,1000)) + '.' + extension


def random_filename_for_info(file_name):
    import random, datetime
    extension = file_name.split('.')[-1]
    return 'info' + '_' + str(random.randint(1,1000)) + '.' + extension


def random_filename_for_home(file_name):
    import random, datetime
    extension = file_name.split('.')[-1]
    return 'home' + '_' + str(random.randint(1,1000)) + '.' + extension

def random_filename_for_works(file_name):
    import random, datetime
    extension = file_name.split('.')[-1]
    return 'works' + '_' + str(random.randint(1,1000)) + '.' + extension

def get_file_extension(file_name):
    return file_name.split('.')[-1]

def get_file_name(file_name):
    return file_name.split('.')[0]

def get_file_size(file_name):
    return os.path.getsize(file_name)

def get_file_path(file_name):
    return os.path.abspath(file_name)
