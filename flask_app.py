from flask import Flask, redirect, render_template, url_for, request
from src.db import Cancion

app = Flask(__name__)

app.secret_key = 'loqueseavaAqui'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/')
def home():
    select = Cancion()
    canciones = select.select()
    return render_template('home.html', canciones=canciones)

@app.route('/add', methods=['GET', 'POST'])
def add_song():
    if request.method == 'GET':
        return render_template('add_song_form.html')
    
    if request.method == 'POST':
        insert = Cancion()
        cancion = request.form['cancion']
        bpm = request.form['bpm']
        compas = request.form['compas']
        insert.add(cancion, bpm, compas)
        return redirect(url_for('home'))

@app.route('/edit', methods=['GET'])
def edit():
    select = Cancion()
    canciones = select.select()
    return render_template('edit.html', canciones=canciones)

@app.route('/edit/<id>', methods=['GET' ,'POST'])
def edit_song(id):    
    if request.method == 'GET':
        select = Cancion()
        cancion = select.edit_page(id)
        return render_template('edit_song.html', cancion=cancion)
    elif request.method == 'POST':
        edit = Cancion()
        cancion = request.form['cancion']
        bpm = request.form['bpm']
        compas = request.form['compas']
        edit.edit(id, cancion, bpm, compas)
        return redirect(url_for('home'))

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    delete_song = Cancion()
    delete_song.delete(id)
    return redirect(url_for('home'))

app.run(
    debug=True,
    port=3000
)