from flask import *
from flask import Flask, render_template, request, redirect, url_for
import fileParser


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
        return render_template('documentation.html')
    else:
        return render_template('validator_login_failed.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('result.html', fileName=f.filename)


@app.route('/bug_report')
def bug_report():
    return render_template('bug_report.html')


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
