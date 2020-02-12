import os	

secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)	

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@127.0.0.1:5432/nyg-batch-qa'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False