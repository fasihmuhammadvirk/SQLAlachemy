from main import session, Customer, Product

##commneted this session after adding it in the database or running it for the first time
# customer1 = Customer(name = "Customer 1")
# customer2 = Customer(name = "Customer 2")
# customer3 = Customer(name = "Customer 3")

# session.add_all(
    
#     [customer1,customer2,customer3]
    
# )

# session.commit()


#querying the first and second customer
customer = session.query(Customer).filter(Customer.id == 1 ).first()
customer2 = session.query(Customer).filter(Customer.id == 2 ).first()

#creating the products
product = Product(name =  "Chicken" , price = 2000)
product1 = Product(name = "Keyboard", price = 500)
product2 = Product(name = "Mouse", price = 1000)


## adding more product for the customer  
# customer.products.append(product)
# customer.products.append(product2)
# customer.products.append(product1)


print(customer.products)

session.commit()
