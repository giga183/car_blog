from flask import Flask, render_template, url_for, redirect, request
from src.ext import app
from src.forms import AddCarForm, RegisterForm, LoginForm
from src.models import User, Car
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/cars_for_sale')
def cars_sale():
    cars_list = Car.query.all()
    return render_template("Cars_Sale.html", cars_list=cars_list)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.save()
    return render_template("register.html", form=form)




@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
        return redirect(url_for('index'))
    return render_template("sign_in.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")


@app.route('/ABT')
def abt():
    return render_template("ABT_Urus.html")


@app.route('/X6M')
def x6m():
    return render_template('X6M.html')


@app.route('/Brabus')
def brabus():
    return render_template("Brabus.html")



@app.route('/add_car', methods=["GET", "POST"])
@login_required
def add_car():

    if current_user.role != "admin":
        return redirect(url_for('index'))

    form = AddCarForm()
    if form.validate_on_submit():
        new_car = Car(car_manufacturer=form.car_manufacturer.data,
                      car_model=form.car_model.data,
                      car_price=form.car_price.data,
                      img=form.image_link.data)
        new_car.save()
        return redirect(url_for('cars_sale'))
    return render_template("add_car.html", car_form=form)

