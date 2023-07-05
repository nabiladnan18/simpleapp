from flask import Flask, render_template

app = Flask(__name__, template_folder="./templates", static_folder="./static")

@app.route('/')
@app.route('/<name>')
def home(name=None):
        return render_template('base.html', name=name)

if __name__ == '__main__':
    app.run()