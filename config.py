import os

DEBUG_ENABLED = False
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
DATABASE_URI = 'sqlite:////tmp/github-flask.db'
GITHUB_OAUTH_APP_NAME = 'purl_editor'
GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')
