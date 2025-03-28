from flask import Blueprint, request, render_template, redirect, session
from models import db, User

login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/')
def index():
    return redirect('/login')

@login_routes.route('/login')
def login():
    data = User.query.all()
    return render_template('login.html', data=data)

@login_routes.route('/authenticate', methods=["POST"])
def login_check():
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    user = User.query.filter_by(user_name=user_name).first()  
    if user and user.password == password:
        session['user_id'] = user.id 
        return redirect('/home') 
    return redirect('/login')

@login_routes.route('/create_account')
def create_account():
    return render_template('create_account.html')

@login_routes.route('/post_create_account', methods=["POST"])
def post_create_account():
    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    if user_name and email and password:
        new_user = User(user_name=user_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
    return redirect('/login')

@login_routes.route('/delete_user/<int:id>')
def delete_user(id):
    erase_user = User.query.get(id)
    if erase_user:
        db.session.delete(erase_user)
        db.session.commit()
    return redirect('/')

@login_routes.route('/update_user/<int:id>')
def update_user(id):
    data = User.query.get(id)
    if data:
        return render_template('update_user.html', data=data)
    return redirect('/login')

@login_routes.route('/user_update/<int:id>', methods=["POST"])
def post_update_user(id):
    data = User.query.get(id)
    if data:
        data.email = request.form.get("email")
        data.password = request.form.get("password")
        db.session.commit()
    return redirect('/login')