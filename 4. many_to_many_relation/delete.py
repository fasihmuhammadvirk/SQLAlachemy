from main import session, Customer, Product


#query the customer whose product you want to delete
customer = session.query(Customer).filter(Customer.id == 1 ).first()

#query the product you want to delete from the user 
product = session.query(Product).filter(Product.id == 1 ).first()


#remove the product from the customer 
customer.products.remove(product)

#commit the session 
session.commit()

#see if the product has been deleted or not 
print(customer.products)
