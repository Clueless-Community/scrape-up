from products import Product
__all__=['Product']


#For getting product details
print(Product("watch").get_product_details())
#for getting product image
print(Product("watch").get_product_image())
#for getting customer reviews
print(Product("watch").customer_reviews()) 
