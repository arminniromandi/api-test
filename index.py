from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

# مدل محصول
class Product(BaseModel):
    id: int
    name: str
    price: float

# داده‌های نمونه (میتونه از دیتابیس باشه)
products_db = [
    Product(id=1, name="کتاب", price=100000),
    Product(id=2, name="لپ‌تاپ", price=25000000),
    Product(id=3, name="هدفون", price=600000),
]

@app.get("/products", response_model=List[Product])
def get_products():
    return products_db