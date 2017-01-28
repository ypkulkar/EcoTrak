from flask import Flask, render_template
import requests # pip install requests
app = Flask(__name__)

@app.route('/')
def render():
   
    return render_template('ecotrak.html')

@app.route('/calories')
def render1():
    return render_template('calories.html')

@app.route('/carbon')
def render2():
    return render_template('carbon.html')

if __name__=='__main__':
    app.run(debug=True)
