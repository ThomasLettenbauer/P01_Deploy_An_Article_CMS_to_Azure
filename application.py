"""
This script runs the FlaskWebProject application using a development server.
"""
import sys
from os import environ
import logging
from FlaskWebProject import app

streamHandler = logging.StreamHandler(stream=sys.stdout)
app.logger.addHandler(streamHandler)
app.logger.setLevel(logging.INFO)
app.logger.info('********** App starting **********')

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT, ssl_context='adhoc')
