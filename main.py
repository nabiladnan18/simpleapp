from flask import Flask, render_template, session, redirect, url_for
from dotenv import load_dotenv
import os

app = Flask(__name__, template_folder="./templates", static_folder="./static")
load_dotenv(".env")

@app.route('/')
@app.route('/<name>')
def home(name=None):
        return render_template('base.html', name=name)

if __name__ == '__main__':
    app.run()