import os


host = os.environ.get('G_HOST', '127.0.0.1')
port = os.environ.get('G_PORT', '5000')
bind = [f"{host}:{port}"]
workers = 1
daemon = True
