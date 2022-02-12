from flask import *
import fileParser


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


@app.route('/bug_report')
def bug_report():
    return render_template('bug_report.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

