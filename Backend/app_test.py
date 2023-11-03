from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Get the directory of the current script file
rootdir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    # Set the directory you want to start from
    # rootdir = os.path.expanduser("/Users/wanrylin/Python code/ECE 569 IOT/Backend")  # This will start at your home directory
    # For a specific path, you can use something like rootdir = 'C:/path/to/folder'
    files_and_dirs = [{'name': item, 'is_dir': os.path.isdir(os.path.join(rootdir, item)), 'path': item} for item in
                      os.listdir(rootdir)]
    return render_template('index.html', files_and_dirs=files_and_dirs, rootdir=rootdir)


@app.route('/files/<path:path>')
def download_file(path):
    # directory = os.path.expanduser("/Users/wanrylin/Python code/ECE 569 IOT/Backend")  # Adjust the path to your files' location
    return send_from_directory(rootdir, path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
