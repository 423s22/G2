import shutil
from zipfile import ZipFile
import os


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
