#Creating a Schema 

#we will use to create the model for our schema
from sqlalchemy.orm import declarative_base  
from sqlalchemy import Column, Integer, String ,DateTime #element for our table 
from datetime import datetime #to use the datatime 

Base = declarative_base() #this will be inherited by our schema 

# create our model that will be mapped to the database 
class User(Base):
    
    #tablename 
    __tablename__ = 'user_information'
    
    #tablecolumns
    id =   Column(Integer(), primary_key = True)
    username = Column(String(50),nullable = False,unique=True)
    password = Column(String(50),nullable = False)
    email = Column(String(80), nullable=False, unique = True)
    Datetime = Column(DateTime(), default = datetime.utcnow)
    
    #if we use print statement to saw the data it will return an object so  
    #the __repr__ is going to return the string representation of the object
    def __repr__(self):
        return(
            
            f'id = {self.id}, username = {self.username}, password = {self.password}, email = {self.email}, datetime = {self.Datetime}'
            
        )
    


# user = User(id = 1, username = "fasih", password = "1213", email = "fasih.virk@netsol")
# print(user)



