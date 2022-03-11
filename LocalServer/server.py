from flask import *
from flask import Flask, render_template, request, redirect, url_for
import fileParser
import fileUpload
import getResults


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/bug_report')
def bug_report():
    return render_template('bug_report.html')


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
