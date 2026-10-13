from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI()
@app.get("/")

def home() :
    return {"message" : "Hello Ankush"}

@app.get("/users/{user_id}")

def get_user(user_id : int)  : 
    return {"user_id" : user_id}

# Query parameter
# /products?category=mobile&price=20000

@app.get("/products")
def get_products(category : str , price : int) :
    return {
        "category" : category , 
        "price"  : price
    }

# how we can recieve the data frim client
# suppose client sending this data

# {
#   "name": "Laptop",
#   "price": 50000
# }

# model....

class Product(BaseModel) : 
    name  : str
    price : float
    description : str | None = None 

@app.post("/products")

def create_product(product : Product) : 
    return  {
        "message" : "Product created successfully" , 
        "product" : product.name , 
        "price"  : product.price, 
        "description" : product.description
    }