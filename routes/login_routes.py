from flask import Blueprint, request, render_template, redirect, session
import sqlite3

login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/') 
def index():
    return redirect('/login')

@login_routes.route('/login')
def login():
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return render_template('login_templates/login.html', data=data) 

@login_routes.route('/authenticate', methods=["POST"])
def login_check():
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user_name = '{user_name}'")
    user = cursor.fetchone()
    conn.close()
    if user and user[3] == password:  
        session['user_id'] = user[0] 
        return redirect('/home')
    return redirect('/login')

@login_routes.route('/create_account')
def create_account():
    return render_template('login_templates/create_account.html')

@login_routes.route('/post_create_account', methods=["POST"])
def post_create_account():
    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    if user_name and email and password:
        conn = sqlite3.connect("DB_layer/site.db")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (user_name, email, password) VALUES ('{user_name}', '{email}', '{password}')")
        conn.commit()
        conn.close()
    return redirect('/login')

@login_routes.route('/delete_user/<int:id>')
def delete_user(id):
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {id}")
    conn.commit()
    conn.close()
    return redirect('/')

@login_routes.route('/update_user/<int:id>')
def update_user(id):
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {id}")
    data = cursor.fetchone()
    conn.close()
    if data:
        return render_template('login_templates/update_user.html', data=data)
    return redirect('/login')

@login_routes.route('/user_update/<int:id>', methods=["POST"])
def post_update_user(id):
    email = request.form.get("email")
    password = request.form.get("password")
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET email = '{email}', password = '{password}' WHERE id = {id}")
    conn.commit()
    conn.close()
    return redirect('/login')