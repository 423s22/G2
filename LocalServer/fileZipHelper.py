from zipfile import ZipFile
import os

def renameZip(fileName):
    fName = fileName
    os.rename(fName, fName + '.zip')
    print(fName + 'renamedFile')

def extractZip(zFile):
    path = '/UnpackedDissertations'
    z = zFile
    with ZipFile(z, 'r') as zip:
        zip.extractall(path)

