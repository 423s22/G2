from zipfile import ZipFile


def extractZip(zFile):
    z = zFile
    with ZipFile(z, 'r') as zip:
        zip.extractall('UnpackedDissertations')
