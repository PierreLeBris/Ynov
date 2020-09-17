from flask import Flask, render_template, request
import pandas as pd
from utils import *

app = Flask(__name__)

@app.route('/')
def view():
    return render_template('home.html')

@app.route('/display_csv', methods=['GET', 'POST'])
def display_csv():
    if request.method == 'POST':
        f = request.files['file']
        df = pd.read_csv(f)
        df = df.to_dict('split')
    return render_template("diplay_csv.html", df = df)

if __name__ == '__main__':
    app.run(debug=True)
