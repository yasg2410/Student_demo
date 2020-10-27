from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from flask import Response, send_file

app = Flask(__name__,template_folder="template")

import main as db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table', methods=['GET', 'POST'])
def table():
    details = db.get_details()
    dblist = []
    for detail in details:
        var = list(detail)
        dblist.append(var)
    return render_template('table.html', var=dblist)

@app.route('/insert', methods=['post'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        db.insert_details(name, email,contact,address)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        return render_template('index.html', var=var)


if __name__ == "__main__":
    app.run(debug=True)
