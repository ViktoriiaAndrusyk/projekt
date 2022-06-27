from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    colour = db.Column(db.Text)
    engine = db.Column(db.Text)
    yearOfProduction = db.Column(db.Text)
    price = db.Column(db.Integer)

def create_product(name, colour, engine, yearOfProduction, price):
    product = Product(name=name, colour=colour, engine=engine, yearOfProduction=yearOfProduction, price=price)
    db.session.add(product)
    db.session.commit()
    db.session.refresh(product)


def read_products():
    return db.session.query(Product).all()


def update_product(product_id, name, colour, engine, yearOfProduction, price):
    db.session.query(Product).filter_by(id=product_id).update({
        "name": name,
        "colour": colour,
        "engine": engine,
        "yearOfProduction": yearOfProduction,
        "price": price

    })
    db.session.commit()


def delete_product(product_id):
    db.session.query(Product).filter_by(id=product_id).delete()
    db.session.commit()
