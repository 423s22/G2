import os
import shutil

from flask import *
from flask import Flask, render_template, request, redirect, url_for
import fileParser
# import fileUpload
# import getResults
import fileZipHelper

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


@app.route('/validation')
def validation():
    return render_template('validator_login.html')


@app.route('/upload')
def upload():
    if request.values.get('valid'):
        return render_template('upload.html')
    else:
        return redirect('/validation')


@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('pass') == '1234':
        return redirect(url_for('upload', valid=True))
    else:
        return render_template('validator_login_failed.html')


@app.route('/upload_file', methods=['POST'])
def upload_file():
    path = 'Uploads/'
    unpack_path = 'Unpacked/'
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(path, f.filename))
        fileZipHelper.renameZip(f.filename)
        return render_template('result.html')

@app.route('/result', methods=['GET'])
def evaluate_file():
    path_unpacked = 'Unpacked/'
    path_packed = 'Uploads/'

    fileTMP = os.listdir(path_packed)
    fileToEval = fileTMP[0] #This makes sure that the parser can be passed the acccurate filename for the current working file
    print(fileToEval)

    # This is where the parser will be called something like
    # path_evaluated = parser.parseDisertation(fileToEval)

    validate = fileParser.validatorMain()
    validate.parse('Uploads/' + fileToEval)

    shutil.rmtree('Unpacked')
    os.mkdir('Unpacked')

    os.remove('Uploads/' + fileToEval)
    # When parsing is complete change the green text in send file to the path_evaluated var declared above
    # That should cause the website to download the file the parser spit out
    try:
        return send_file('Changes/requiredChanges.txt', as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/bug_report')
def bug_report():
    return render_template('bug_report.html')


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
