from fastapi import APIRouter, Depends
from app.services.product_service import ProductService
from app.dependencies import get_current_user, get_current_active_admin_user

router = APIRouter()

@router.get("/products")
def get_products(product_service: ProductService = Depends(), **kwargs):
    return product_service.get_product_list(**kwargs)

@router.get("/products/{product_id}")
def get_product_detail(product_id: int, product_service: ProductService = Depends()):
    return product_service.get_product_detail(product_id)

@router.put("/products/{product_id}/status/activate")
def activate_product(product_id: int, product_service: ProductService = Depends(), admin=Depends(get_current_active_admin_user)):
    # 调用 service 中的激活商品方法
    pass

@router.put("/products/{product_id}/status/reject")
def reject_product(product_id: int, product_service: ProductService = Depends(), admin=Depends(get_current_active_admin_user)):
    # 调用 service 中的拒绝商品方法
    pass

@router.put("/products/{product_id}/status/withdraw")
def withdraw_product(product_id: int, product_service: ProductService = Depends(), user=Depends(get_current_user)):
    # 调用 service 中的下架商品方法
    pass