from flask import Flask, render_template, url_for, request
import qr_utils

app = Flask(__name__, static_folder="static")


@app.route('/')
@app.route("/index")
def index():
    return render_template('data.html')


@app.route("/Qr", methods = ['POST'])
def success():
    if request.method == 'POST':
        data = request.form['qr_data']
        qr_utils.generate_qr(data, "static")
        return render_template("Qr.html")


if __name__ == "__main__":
    app.run()
