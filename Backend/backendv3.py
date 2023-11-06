from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import shutil


app = Flask(__name__)
UPLOAD_FOLDER = '/Users/wanrylin/Python code/ECE 569 IOT/Backend test/test file'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def ensure_path_exist(directory):
    flag = "True"
    if not os.path.exists(directory):
        flag = "False"
        os.mkdir(directory)
        print(f'Directory {directory} created.')
    else:
        print(f'Directory {directory} already exists.')
    return directory, flag

def get_path(address):
    add_lst = address.split(", ")
    add_lst.reverse()
    for names in add_lst:
        contains_number = any(char.isdigit() for char in names)
        if contains_number:
            add_lst.remove(names)
    add_level = add_lst[1:4]
    add_level = [x.replace(" ", "_") for x in add_level]
    current_directory = os.getcwd()
    father_directory = os.path.dirname(current_directory)
    test_repository = os.path.join(father_directory, "Backend test")
    test_repository,test_repository_flag = ensure_path_exist(test_repository)
    test_file_folder = os.path.join(test_repository, "test file")
    test_file_folder,test_file_folder_flag = ensure_path_exist(test_file_folder)
    flag = "True"
    add_path = test_repository
    for add_directory in add_level:
        add_path = os.path.join(add_path, add_directory)
        add_path,add_flag = ensure_path_exist(add_path)

    return add_path,add_flag,test_repository_flag,test_file_folder

def copy_file(source_file_path, file_father_path,file_name):
    destination_path = os.path.join(file_father_path,file_name)
    try:
        dest = shutil.copy2(source_file_path, destination_path)
        return f'Copy successful: {dest}'
    except FileNotFoundError as e:
        return f'File not found: {e}'
    except PermissionError as e:
        return f'Permission error: {e}'
    except Exception as e:
        return f'An error occurred: {e}'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    address = request.form.get('address', None)
    if not address:
        return 'Address is required', 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        folder_path, add_flag, test_repository_flag, test_file_folder = get_path(address)
        file_path = os.path.join(folder_path, filename)
        try:
            file.save(file_path)
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                return jsonify({
                    'message': 'File successfully uploaded',
                    'file_path': file_path
                }), 200
            else:
                return 'Failed to save file', 500
        except Exception as e:
                return jsonify({'error': str(e)}), 500
    else:
        return 'File not allowed', 400


@app.route('/')
def home():
    return render_template('frontendv3.html')

@app.route('/location-data', methods=['POST'])
def handle_location_data():
    if request.method == 'POST':
        location_data = request.json
        print(location_data)
        return 'Location data received', 200

if __name__ == '__main__':
    app.run(debug=True)