from flask import current_app as app
from models import Product, create_product, read_products, delete_product, update_product
from flask import request, render_template, redirect


@app.route("/", methods=["POST", "GET"])
def view_index():
    if request.method == "POST":
        create_product(request.form['name'], request.form['colour'], request.form['engine'], request.form['yearOfProduction'],
                       request.form['price'],)
    return render_template("index.html", products=read_products())


@app.route("/edit/<product_id>", methods=["POST", "GET"])
def edit_product(product_id):
    if request.method == "POST":
        update_product(product_id, name=request.form['name'], colour = request.form['colour'],
                       engine=request.form['engine'], yearOfProduction= request.form['yearOfProduction'], price=request.form['price'])
    elif request.method == "GET":
        delete_product(product_id)
    return redirect("/", code=302)

