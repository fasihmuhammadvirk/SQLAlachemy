
#the create engine is going to help us in creating database and also connecting with the database 
from sqlalchemy import create_engine

#this is a database url and we can say the connection string
#server://username:password@host:port/databasename
database_url = 'postgresql://postgres:1213@localhost:5432/practice_database'

#creating the engine first argument is the database url or connection string
engine = create_engine(database_url,echo = True)

#used for creating sessions 
from sqlalchemy.orm import sessionmaker 

#creating a session for doing operations on the database
session = sessionmaker()(bind=engine)

from sqlalchemy import(
    
    Column,
    String,
    Integer,
    ForeignKey
)


#importing the reationship and declarative base to create aur model 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#creating the parent class 
class Parent(Base):
    
    #tablename in the database 
    __tablename__ = 'parent'
    
    #table entities
    id = Column(Integer(),primary_key = True )
    name = Column(String(25),nullable = False)
    
    #creating a relationship with the child table
    child = relationship('Child',back_populates='parent',uselist=False)
    
    #retrun when we print the class object
    def __repr__(self):
    
        return f'<Parent {self.id}'


#child class 
class Child(Base):
    
    #tablename in the database
    __tablename__ = 'child'
    
    #table entities
    id = Column(Integer(),primary_key=True)
    name = Column(String(25),nullable= False)
    
    #defining foregin key 
    parent_id = Column(Integer(),ForeignKey('parent.id'))
    
    #creating realtion with the parent table
    parent = relationship('Parent',back_populates='child')
    
    #return when the object of the class is printed
    def __repr__(self):
        return f'<Child {self.id}>'
    

#to create all the table into database table 
Base.metadata.create_all(engine)