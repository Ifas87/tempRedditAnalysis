from flask import Flask, render_template, request, url_for, flash, redirect
from flask import render_template
from main import reddit, data_loading, all_analysis


app = Flask(__name__)
app.config['SECRET_KEY'] = '845ea0b38cc7bd5b7520d5bd54bb2e610008319c51b2ec15'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/request', methods=["POST"])
def handle_request():
    subreddit_name = ''

    if request.method == 'POST':
        subreddit_name = request.form['subreddit']
        print(subreddit_name)
    
    return redirect(url_for('report'))


@app.route('/results')
def report():
    return render_template("index.html")


if (__name__ == '__main__'):
    app.run()