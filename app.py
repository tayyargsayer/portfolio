from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/portfolio-details')
def details():
    return render_template('portfolio-details.html')

@app.route('/service-details')
def service_details():
    return render_template('service-details.html')

@app.route('/starter-page')
def starter_page():
    return render_template('starter-page.html')




if __name__ == '__main__':
    app.run(debug=True)
