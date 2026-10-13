# from fastapi import FastAPI
# from pydantic import BaseModel

# app  = FastAPI()
# @app.get("/")

# def home() :
#     return {"message" : "Hello Ankush"}

# @app.get("/users/{user_id}")

# def get_user(user_id : int)  : 
#     return {"user_id" : user_id}

# # Query parameter
# # /products?category=mobile&price=20000

# @app.get("/products")
# def get_products(category : str , price : int) :
#     return {
#         "category" : category , 
#         "price"  : price
#     }

# # how we can recieve the data frim client
# # suppose client sending this data

# # {
# #   "name": "Laptop",
# #   "price": 50000
# # }

# # model....

# class Product(BaseModel) : 
#     name  : str
#     price : float
#     description : str | None = None 

# @app.post("/products")

# def create_product(product : Product): 
#     return  {
#         "message" : "Product created successfully" , 
#         "product" : product.name , 
#         "price"  : product.price, 
#         "description" : product.description
#     }

# ---------------creating simple product Api------------

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app  = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 800}
]

#get all the products
@app.get("/products")

def getAllProducts() : 
    return products

#get one product

@app.get("/products/{id}")

def GetProductByid(id : int) : 
    for product in products : 
        if product["id"]  == id :
            return product

    return {"message" : "product not found....."}

# create a product using post

class Product(BaseModel) : 
    name  :  str
    price : float 
    description : str | None = None 

@app.post("/products") 

def create_product(product : Product) : 
    new_product =  {
        "id" : len(products)+1  , 
        "name" : product.name , 
        "price" : product.price , 
        "description" : product.description
    }
    products.append(new_product)
    return {
        "message" : "Product created successfully...." , 
        "product" : new_product
    }

print(products)

# UPDATE THE PRODUCT.....
@app.put("/products/{product_id}")
def update_product(product_id :  int , updated_product : Product) :
    for product in products : 
        if product["id"] == product_id : 
            product["name"] = updated_product.name
            product["price"] = updated_product.price
            product["description"] = updated_product.description
            return  {
                "message" : "product updated successfully...." , 
                "product"  : product
            }
    raise HTTPException(status_code=404, detail="Product not found")

# Delete the product using product id
@app.delete("/products/{product_id}")
def delete_product(product_id : int) : 
    for [index,product] in enumerate(products) : 
        if product["id"] == product_id : 
            deleted_Product = products.pop(index)
            return {
                "message" : "product deleted successfully...", 
                "product" : deleted_Product 
            }
    raise HTTPException(
        status_code = 404 , 
        detail = "Product not found"
    )