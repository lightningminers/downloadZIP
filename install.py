__author__ = 'wwxiang'

import sys
import os
import zipfile
#https://pypi.python.org/packages/source/s/suds-jurko/suds-jurko-0.4.1.jurko.3.zip#md5=921205d8f9d3f8db2ecb9bae5cd9411a

def sudsInstall():
    if not os.path.isdir(os.getcwd() + os.path.sep + 'sudsinstall'):
        sudsSetup = os.getcwd() + os.path.sep + 'suds-jurko-0.4.1.jurko.3.zip'
        zip_suds = zipfile.ZipFile(sudsSetup,'r')
        zip_suds.extractall(path=os.getcwd())
        os.rename(os.getcwd() + os.path.sep + 'suds-jurko-0.4.1.jurko.3',os.getcwd() + os.path.sep + 'sudsinstall')
    import sudsinstall.setup
    sudsinstall.setup.setup()
    pass
sudsInstall()





