__author__ = 'wwxiang'

import sys
import os
import zipfile
#https://pypi.python.org/packages/source/s/suds-jurko/suds-jurko-0.4.1.jurko.3.zip#md5=921205d8f9d3f8db2ecb9bae5cd9411a

def sudsInstall():
    if not os.path.isdir(os.getcwd() + os.path.sep + 'suds-jurko-0.4.1.jurko.3'):
        sudsSetup = os.getcwd() + os.path.sep + 'suds-jurko-0.4.1.jurko.3.zip'
        msnlibSetup = os.getcwd() + os.path.sep + 'msnlib.zip'
        zip_suds = zipfile.ZipFile(sudsSetup,'r')
        zip_suds.extractall(path=os.getcwd())
        zip_suds.close()
        zip_msnlib = zipfile.ZipFile(msnlibSetup,'r')
        zip_msnlib.extractall(path=os.getcwd())
        zip_msnlib.close()
        return True
    return False
    pass