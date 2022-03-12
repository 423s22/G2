from zipfile import ZipFile
import os


def renameZip(fileName):
    fName = fileName
    os.rename('Uploads/' + fName,'Uploads/' + fName + '.zip')
    print(fName + 'renamedFile')


def extractZip(zFile):
    path = 'Unpacked/'
    z = zFile
    with ZipFile(z, 'r') as zip:
        zip.extractall(path)
