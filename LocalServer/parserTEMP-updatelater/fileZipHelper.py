from zipfile import ZipFile
import os

def renameZip(zFile):
    fName = zFile.filename
    os.rename(fName, fName + '.zip')

def extractZip(zFile):
    path = '/UnpackedDissertations'
    z = zFile
    with ZipFile(z, 'r') as zip:
        zip.extractall(path)

