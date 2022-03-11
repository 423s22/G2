# Simple HTML for This File Uploader
# <html>
#   <body>
#       <form action = "http://localhost:5000/uploader" method = "POST" enctype = "multipart/form-data">
#           <input type = "file" name = "file" />
#           <input type = "submit"/>
#       </form>
#   </body>
# </html>

from flask import Flask, render_template, request
import werkzeug.utils
from varname import nameof
import os
import fileZipHelper
app = Flask(__name__)

path = "/Uploads"

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/result', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        fName = nameof('file')
        f = request.files[fName]
        f.save(os.path.join(path, werkzeug.secure_filename(f.filename)))
        fileZipHelper.renameZip(fName)
        fileZipHelper.extractZip(fName)


        return 'file uploaded successfully'

