# all the imports
import os
import neopixel

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , lighthouse-web.py

app.config.from_envvar('LIGHTHOUSE_SETTINGS', silent=True)

neopixel = Neopixel()

@app.route('/')
def show_entries():
    return render_template('index.html')
    
@app.route('/set', methods=['POST'])
def set():
#    if not session.get('logged_in'):
#        abort(401)

    op = request.form['op']
    color  = Color(request.form['color'])

    if op == 'aus':
        neopixel.colorWipe(Color(0, 0, 0))
    elif op == 'zeile1':
        neopixel.zeile_1(color)
    elif op == 'zeile2':
        neopixel.zeile_2(color)
    elif op == 'zeile3':
        neopixel.zeile_3(color)
    else:
        neopixel.test
        
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))