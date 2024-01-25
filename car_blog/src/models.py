from src.ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()



class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_manufacturer = db.Column(db.String)
    car_model = db.Column(db.String)
    car_price = db.Column(db.Integer)
    img = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    from src.ext import app

    with app.app_context():
        db.create_all()

        admin_user = User(username='admin', password='12345678', role='admin')
        admin_user.save()