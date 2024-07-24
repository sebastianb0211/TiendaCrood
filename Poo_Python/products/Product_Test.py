from products.Category import Category
from products.Product import Product

category = Category(None, None)

product = Product(None, None,None, None , None, None, None)

category.create_category()
category.create_category()
category.list_categories()


product.find_category(category)
product.create_product(category)
product.listing_products()

