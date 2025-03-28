from flask import Flask, session, redirect, render_template
from flask_migrate import Migrate
from models import db, User
from routes.login_routes import login_routes 
from routes.stats_routes import stats_routes 
from routes.home_routes import home_routes 
from database_layer import db_setup

app = Flask(__name__) 
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'secret_key' 
db.init_app(app)  
migrate = Migrate(app, db)
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
    current_user = User.query.get(session.get('user_id')) 
    return render_template('home.html', current_user=current_user)

if __name__ == '__main__':
    app.run()
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"""