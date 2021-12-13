from fastapi import FastAPI, Response

app = FastAPI()

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]


@app.get("/")
def index():
    return {"message": "Hello home"}


@app.get("/products/{id}")
def index(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            return product

    response.status_code = 404
    return "Product Not found"
