from flask import Flask, render_template, url_for

# url_for('static', filename='arquivo.teste')

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)