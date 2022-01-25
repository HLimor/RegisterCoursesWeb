from flask import render_template, url_for, request
from flask import Flask
from readDB import fetchData
from writeDB import writeData
app = Flask(__name__, template_folder='./templates')


@app.route("/")
def index():
    to_send = fetchData.fetch_data()

    return render_template('index.html', to_send=to_send)


@app.route('/register.html')
def register():
    return render_template('register.html', course_name=request.args)


@app.route('/register', methods=['POST'])
def handle_data():
    FormRequest = request.form
    writeData(FormRequest)

    return index()


if __name__ == "__main__":
    app.run()
