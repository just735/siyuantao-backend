from app.dal.product import ProductDAL
from app.dal.favorite import UserFavoriteDAL

class ProductService:
    def __init__(self, product_dal: ProductDAL, user_favorite_dal: UserFavoriteDAL):
        self.product_dal = product_dal
        self.user_favorite_dal = user_favorite_dal

    def get_product_detail(self, product_id):
        product = self.product_dal.get_product_by_id(product_id)
        # 假设还有获取图片的逻辑
        # images = self.product_image_dal.get_images_by_product_id(product_id)
        return product

    def add_favorite(self, user_id, product_id):
        try:
            self.user_favorite_dal.add_user_favorite(user_id, product_id)
        except Exception as e:
            # 处理重复收藏异常
            pass

    def remove_favorite(self, user_id, product_id):
        self.user_favorite_dal.remove_user_favorite(user_id, product_id)

    def get_user_favorites(self, user_id):
        return self.user_favorite_dal.get_user_favorite_products(user_id)