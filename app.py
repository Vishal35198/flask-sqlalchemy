
from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Machine learning engineer',
    'location': 'noida'
    },
    {
        'id':2,
        'title':'Data Sceinec engineer',
        'location':'Delhi'
    }
]

@app.route('/')
def index():
    return render_template('home.html',jobs = JOBS)

if __name__ =="__main__":
    app.run(debug=True)
