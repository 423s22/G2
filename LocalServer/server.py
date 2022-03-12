import os

from flask import *
from flask import Flask, render_template, request, redirect, url_for
import fileParser
# import fileUpload
# import getResults
from LocalServer import fileZipHelper

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


@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('pass') == '1234':
        return render_template('upload.html')
    else:
        return render_template('validator_login_failed.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    path = 'Uploads/'
    unpack_path = 'Unpacked/'
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(path, f.filename))
        fileZipHelper.renameZip(f.filename)
        fileZipHelper.extractZip(path + f.filename + '.zip')
        return render_template('result.html')

@app.route('/result', methods=['GET'])
def evaluate_file():
    path_unpacked = '/UnpackedDissertations'
    path_packed = '/Uploads'

    fileTMP = os.listdir(path_packed)
    fileToEval = fileTMP[0] #This makes sure that the parser can be passed the acccurate filename for the current working file

    # This is where the parser will be called something like
    # path_evaluated = parser.parseDisertation(fileToEval)

    path_evaluatedTMP = 'Changes/'                      # For Testing Only, the parser will return the full path with file name in the end
    fTest = open('Changes/exampleChanges.txt', 'w')     # Testing
    fTest.write('These are some example Changes')       # Testing
    fTest.close()                                       # Testing
    evalTMP = os.listdir(path_evaluatedTMP)
    fileEvaled = evalTMP[0]

    if os.path.exists(fileToEval):
        os.remove('Uploads/' + fileToEval)
    else:
        abort(404)

    if os.path.exists(fileEvaled):
        os.remove(fileEvaled)
    else:
        abort(404)

    # When parsing is complete change the green text in send file to the path_evaluated var declared above
    # That should cause the website to download the file the parser spit out
    try:
        return send_file('Changes/exampleChanges.txt')
    except FileNotFoundError:
        abort(404)

@app.route('/bug_report')
def bug_report():
    return render_template('bug_report.html')


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
