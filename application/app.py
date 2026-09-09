import socket
import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1")
    hostname = socket.gethostname()

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Application test</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 50px; background-color: #f4f4f4; }
            .card { background: white; padding: 20px; border-radius: 8px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
            .v1 { color: #2980b9; }
            .v2 { color: #27ae60; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Plateforme Haute Disponibilité</h1>
            <p>Version actuelle : <strong class="{{ version }}">{{ version }}</strong></p>
            <p>Servi par le conteneur / Hostname : <code>{{ hostname }}</code></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, version=version, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)