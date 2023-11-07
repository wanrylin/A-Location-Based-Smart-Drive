from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import shutil


app = Flask(__name__)
#UPLOAD_FOLDER = '/Users/wanrylin/Python code/ECE 569 IOT/Backend test/test file'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# find if the directory exist or not and create the folder if not exist
def ensure_path_exist(directory):
    flag = "True"
    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        flag = "False"
        os.mkdir(directory)
        print(f'Directory {directory} created.')
    else:
        print(f'Directory {directory} already exists.')
    # return the father path of the file, flag of path existance(T:exist, F:not)
    return directory, flag

# Get the directory according to the location
def get_path(address):
    # turn address str into str list
    add_lst = address.split(", ")
    # in country, province, postal code, city, town order
    add_lst.reverse()
    # just use province, city and town
    # remove postal code inside
    for names in add_lst:
        contains_number = any(char.isdigit() for char in names)
        if contains_number:
            add_lst.remove(names)
    # just need 3 levels
    add_level = add_lst
    # replace space by _
    add_level = [x.replace(" ", "_") for x in add_level]
    # check whether "Backend test" folder exist or not
    # Get the current working directory
    current_directory = os.getcwd()
    # Now to get the father (parent) directory:
    father_directory = os.path.dirname(current_directory)
    test_repository = os.path.join(current_directory, "Received file")
    # find it "test_repository" exist or not
    test_repository,test_repository_flag = ensure_path_exist(test_repository)
    # create a folder to store all the generated files
    test_file_folder = os.path.join(test_repository, "test file")
    # find it "test_file_folder" exist or not
    test_file_folder,test_file_folder_flag = ensure_path_exist(test_file_folder)
    flag = "True"
    add_path = test_repository
    for add_directory in add_level:
        # Construct the path to the next directory
        add_path = os.path.join(add_path, add_directory)
        # Check if the directory exists, if not create it
        add_path,add_flag = ensure_path_exist(add_path)

    return add_path,add_flag,test_repository_flag,test_file_folder

# Save a file with a unique name in the specified directory
def copy_file(file_path, file_name):
    # Get the file name and extension
    base, extension = os.path.splitext(file_name)
    counter = 1
    unique_filename = file_name

    # Check if the file exists and create a new filename if necessary
    while os.path.exists(os.path.join(file_path, unique_filename)):
        unique_filename = f"{base}({counter}){extension}"
        counter += 1

    new_file_path = os.path.join(file_path, unique_filename)
    return new_file_path

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # 从表单数据中获取地址
    address = request.form.get('address', None)
    if not address:
        return 'Address is required', 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # get file path according to the address
        folder_path, add_flag, test_repository_flag, test_file_folder = get_path(address)
        file_path = copy_file(folder_path, filename)
        # save received file
        try:
            # Attempt to copy the file
            file.save(file_path)
            # Check if the file exists
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                # Return the file path in the response
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
    # 使用 render_template 渲染 HTML 文件
    return render_template('index.html')

@app.route('/AutoLocation')
def autolocation():
    # Render AutoLocationFrontendv1.html when the corresponding button is clicked
    return render_template('AutoLocationFrontendv1.html')

@app.route('/TypeLocation')
def manuallocation():
    # Render frontendv2.html when the corresponding button is clicked
    return render_template('TypeLocationFrontendv1.html')

@app.route('/location-data', methods=['POST'])
def handle_location_data():
    if request.method == 'POST':
        location_data = request.json  # This will contain the JSON data sent from the client
        # Do something with location_data, for example, save it to a database or file
        print(location_data)  # For demonstration purposes
        return 'Location data received', 200


if __name__ == '__main__':
    app.run(debug=True)