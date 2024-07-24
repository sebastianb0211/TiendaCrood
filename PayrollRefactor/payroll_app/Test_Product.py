from payroll_app.Category import Category
from payroll_app.Product import Product

category = Category(None, None)
product = Product(None, None, None, None, None, None)


category.create_category()
category.create_category()
category.listing_categories()

product.create_product(category)
product.listing_products()