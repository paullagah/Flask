from flask import Flask
from flask import render_template
app = Flask(__name__)

dummyData = [
    {
        "firstname": "Paul",
        "lastname": "Lagah",
        "gymnast_id": "001"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Homepage', posts=dummyData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run()
