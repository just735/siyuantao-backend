from fastapi import APIRouter, Depends
from app.services.product_service import ProductService
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/favorites/{product_id}")
def add_favorite(product_id: int, product_service: ProductService = Depends(), user=Depends(get_current_user)):
    product_service.add_favorite(user.id, product_id)
    return {"message": "Added to favorites"}

@router.delete("/favorites/{product_id}")
def remove_favorite(product_id: int, product_service: ProductService = Depends(), user=Depends(get_current_user)):
    product_service.remove_favorite(user.id, product_id)
    return {"message": "Removed from favorites"}

@router.get("/favorites")
def get_user_favorites(product_service: ProductService = Depends(), user=Depends(get_current_user)):
    return product_service.get_user_favorites(user.id)