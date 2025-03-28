from app import app, db
with app.app_context():
    db.create_all()
# migrations
"""  run these if you make a change to the models
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
"""