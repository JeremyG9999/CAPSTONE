from flask import Flask, session, redirect, render_template
from routes.login_routes import login_routes 
from routes.stats_routes import stats_routes 
from routes.home_routes import home_routes 
from database_layer import *
import sqlite3

app = Flask(__name__) 
app.debug = True
app.config['SECRET_KEY'] = 'secret_key' 
db_setup()

# Routes from routes folder
app.register_blueprint(login_routes, url_prefix='/')
app.register_blueprint(stats_routes, url_prefix='/')
app.register_blueprint(home_routes, url_prefix='/')

# Routes
@app.route('/logout')
def logout():
    session.clear()  
    return redirect('/login')

@app.route('/home')
def home():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')
    conn = sqlite3.connect("DB_layer/site.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    conn.close()
    if user:
        return render_template('home_templates/home.html', current_user=user)
    return redirect('/login')

if __name__ == '__main__':
    app.run()
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"""