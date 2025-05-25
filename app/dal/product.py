import pyodbc 

class ProductDAL:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def get_product_list(self, **kwargs):
        with self.connection_pool.acquire() as conn:
            cursor = conn.cursor()
            cursor.execute('EXEC sp_GetProductList @searchQuery=?, @categoryName=?, @minPrice=?, @maxPrice=?, @page=?, @pageSize=?, @sortBy=?, @sortOrder=?, @status=?',
                           kwargs.get('searchQuery'), kwargs.get('categoryName'), kwargs.get('minPrice'), kwargs.get('maxPrice'),
                           kwargs.get('page'), kwargs.get('pageSize'), kwargs.get('sortBy'), kwargs.get('sortOrder'), kwargs.get('status'))
            return cursor.fetchall()

    def get_product_by_id(self, product_id):
        with self.connection_pool.acquire() as conn:
            cursor = conn.cursor()
            cursor.execute('EXEC sp_GetProductById @productId=?', product_id)
            return cursor.fetchone()

    # 其他方法...