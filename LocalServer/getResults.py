from flask import Flask, render_template, send_from_directory, safe_join, abort
import os
import parser

app = Flask(__name__)


@app.route('/result')
def evaluate_file():
    return render_template('upload.html')


@app.route('/result', methods=['GET'])
def evaluate_file():
    path_unpacked = '/UnpackedDissertations'
    path_packed = '/Uploads'

    fileTMP = os.listdir(path_packed)
    fileToEval = fileTMP[0] # This makes sure that the parser can be passed the acccurate filename for the current working file

    # This is where the parser will be called something like
    # path_evaluated = parser.parseDisertation(fileToEval)

    path_evaluated = 'Changes'  # For Testing Only, the parser will return the full path with file name in the end
    fTest = open('exampleChanges', 'w')                 # Testing
    fTest.write('These are some example Changes')       # Testing
    fTest.close()                                       # Testing
    evalTMP = os.listdir(path_evaluated)                # testing
    fileEvaled = evalTMP[0]                               # testing

    try:
        return send_from_directory(path_evaluated, filename=fileEvaled, as_attachment=True)
    except FileNotFoundError:
        abort(404)

    if os.path.exists(fileToEval):
        os.remove(fileToEval)
    else:
        abort(404)

    if os.path.exists(fileEvaled):
        os.remove(fileEvaled)
    else:
        abort(404)










