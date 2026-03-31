from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS messages (name TEXT, message TEXT)")
    cur.execute("INSERT INTO messages VALUES (?, ?)", (name, message))

    conn.commit()
    conn.close()

    return "Message Saved Successfully!"

if _name_ == '_main_':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
