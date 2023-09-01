from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="./templates", static_folder="./static")


@app.route('/', methods=['GET', 'POST'])
def home(name=None):
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('user', name=name))
    return render_template('base.html')


@app.route('/custom', methods=['GET', 'POST'])
def custom_name():
    return render_template("name.html")


@app.route('/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template('base.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)