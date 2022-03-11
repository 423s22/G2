from flask import Flask, render_template, request
import werkzeug.utils
from varname import nameof
import os
app = Flask(__name__)

@app.route('/result', methods=['GET'])
def evaluate_file(zFile):
