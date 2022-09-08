import os
import shlex
import subprocess

from flask import Flask, request


app = Flask(__name__)


def exec_cmd(cmd):
    print(f'> {cmd}')
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    lines = process.stdout.readlines()
    return [line.strip().decode() for line in lines]


@app.route("/")
def home():
    return "Hi, there !"


form = """
<form action="" method="post">
  <input type="submit" value="Deploy">
</form>
"""

@app.route("/deploy-motherfucker", methods=['GET', 'POST'])
def deploy_hook():
    script_path = os.environ.get('SCRIPT_PATH')
    if request.method == 'POST':
        result = exec_cmd(script_path)
        text = '\n'.join(result)
        return f"Finished !<br> <pre>{text}</pre>"
    return form
