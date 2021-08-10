"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
import logging
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.logger.setLevel(logging.WARNING)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.WARNING)
    app.logger.addHandler(streamHandler)

    app.run(HOST, PORT, ssl_context='adhoc')
