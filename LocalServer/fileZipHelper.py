import shutil
from zipfile import ZipFile
import os

from flask import send_file, abort


def send_File(filePath):
    try:
        return send_file(filePath, as_attachment=True)
    except FileNotFoundError:
        abort(404)

def renameZip(fileName):
    fName = fileName
    shutil.copyfile('Uploads/' + fileName, 'Uploads/temp.docx')
    extractZip('Uploads/temp.docx')
    print(fName + 'renamedFile')


def extractZip(zFile):
    path = 'Unpacked/'
    z = zFile
    with ZipFile(z, 'r') as zip:
        zip.extractall(path)
