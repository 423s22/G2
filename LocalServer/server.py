from flask import Flask
from flask import render_template
import fileParser


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Dissertation Validator")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

