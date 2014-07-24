import os

DEBUG = True

_HOST = 'localhost'
_PORT = int(os.environ.get('PORT', 5000))
SERVER_NAME = '%s:%s' % (_HOST, _PORT)
