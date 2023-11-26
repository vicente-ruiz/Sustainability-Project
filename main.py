from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return 'Sustainability of Artificial Intelligence'
    return render_template('home.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/economic')
def economic():
    return render_template('economic.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/environmental')
def environmental():
    return render_template('environmental.html')

@app.route('/conclusions')
def conclusions():
    return render_template('conclusions.html')


app.run(host='0.0.0.0', port=81)
