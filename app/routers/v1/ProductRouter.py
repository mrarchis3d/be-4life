

from fastapi import Body, status, Depends
from fastapi import APIRouter
from app.schemas.ProductSchema import ProductBase, ProductCreated
from app.services.ProductService import ProductService


product_router = APIRouter(
    prefix='/v1/products',
    tags=['products']
)


# @routers.get("/products", response_model=List[Product])
# async def get_products():
#     return products_db

# # Ruta para obtener un producto por su índice en la lista
# @router.get("/products/{product_id}", response_model=Product)
# async def get_product(product_id: int):
#     if product_id < 0 or product_id >= len(products_db):
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     return products_db[product_id]

# Ruta para crear un nuevo producto
@product_router.post("/", response_model=ProductCreated, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductBase = Body(...), service: ProductService = Depends()):
    return service.create(product)

# # Ruta para actualizar un producto existente
# @router.put("/products/{product_id}", response_model=Product)
# async def update_product(product_id: int, product: Product):
#     if product_id < 0 or product_id >= len(products_db):
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     products_db[product_id] = product
#     return product

# # Ruta para eliminar un producto existente
# @router.delete("/products/{product_id}")
# async def delete_product(product_id: int):
#     if product_id < 0 or product_id >= len(products_db):
#         raise HTTPException(status_code=404, detail="Producto no encontrado")
#     del products_db[product_id]
#     return {"message": "Producto eliminado satisfactoriamente"}