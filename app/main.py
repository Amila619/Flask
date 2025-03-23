from flask import Flask, jsonify, request
import schemas, models
from database import engine, get_db
from sqlalchemy.orm import Session
from pydantic import ValidationError

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>this is a modified flask application</h1>"

@app.route("/items", methods = ["GET"])
def get_items():
    db : Session = get_db()
    products = db.query(models.Product).all()
    data = [product.as_dict() for product in products]
    return {"data" : data}

@app.route("/items/<int:id>", methods = ["GET"])
def get_item(id : int):
    db : Session = get_db()
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        return {"message" : "post does not exist"}, 404
    return {"data" : product.as_dict()}

@app.route("/items", methods = ["POST"])
def create_item():
    db : Session = get_db()
    try:
        data = request.json
        product = schemas.Product(**data)
    except ValidationError as error:
        e = error.errors()[0]
        return {"error" :{"type" : e["type"], "loc" : e["loc"], "msg" : e["msg"]}}, 400
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return{"data" : new_product.as_dict()}, 201

@app.route("/items/<int:id>", methods = ["DELETE"])
def delete_post(id : int):
        db : Session = get_db()
        product = db.query(models.Product).filter(models.Product.id == id)
        if not product.first():
            return {"message" : "post does not exist"}, 404
        product.delete(synchronize_session = False)
        db.commit()
        return {}, 204

@app.route("/items/<int:id>", methods = ["PUT"])
def update_item(id : int):
    db : Session = get_db()
    product_query = db.query(models.Product).filter(models.Product.id == id)
    if product_query.first() == None:
        return {"message" : "post does not exist"}, 404
    try:
        data = request.json
        product = schemas.Product(**data)
    except ValidationError as error:
        e = error.errors()[0]
        return {"error" :{"type" : e["type"], "loc" : e["loc"], "msg" : e["msg"]}}, 400
    updated_product = product_query.update(product.dict(), synchronize_session=False)
    db.commit()
    return {"data" : product.dict()}


if __name__ == '__main__':  
    app.run(debug=True, port=8080,)
   