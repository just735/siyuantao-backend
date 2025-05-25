import pyodbc

class UserFavoriteDAL:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def add_user_favorite(self, user_id, product_id):
        with self.connection_pool.acquire() as conn:
            cursor = conn.cursor()
            cursor.execute('EXEC sp_AddUserFavorite @userId=?, @productId=?', user_id, product_id)
            conn.commit()

    def remove_user_favorite(self, user_id, product_id):
        with self.connection_pool.acquire() as conn:
            cursor = conn.cursor()
            cursor.execute('EXEC sp_RemoveUserFavorite @userId=?, @productId=?', user_id, product_id)
            conn.commit()

    def get_user_favorite_products(self, user_id):
        with self.connection_pool.acquire() as conn:
            cursor = conn.cursor()
            cursor.execute('EXEC sp_GetUserFavoriteProducts @userId=?', user_id)
            return cursor.fetchall()