from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def go():
    return render_template('Site.html')


@app.route('/Site.html')
def index():
    return render_template('Site.html')


if __name__ == '__main__':
    app.run(debug=True)
