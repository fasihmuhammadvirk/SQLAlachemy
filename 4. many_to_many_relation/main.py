
from sqlalchemy import (

    Column,
    String,
    Integer,
    ForeignKey,
    Table
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# this is a database url and we can say the connection string
# server://username:password@host:port/databasename
database_url = 'postgresql://postgres:1213@localhost:5432/practice_database'
engine = create_engine(database_url, echo=True)



Base = declarative_base()

# creating association to create the many to many relationship b/w customers and products
association = Table(

    'association',  # table name of the association
    Base.metadata,  # we give it a metadata object
    
    # specifying the column in the table
    Column('customer_id', ForeignKey('customers.id')),
    
    # specifying the other column in the table
    Column('product_id', ForeignKey('products.id'))

)


class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)

    # creating a the realtionship between two tables
    # in this many to many we add an extra argument secondary to indetify the assocoation table
    # and after that we specofy the back_popualte that help us while we query
    products = relationship(
        'Product', 
        secondary=association,
        back_populates='customers')

    def __repr__(self):
        return f"Customer('{self.name}')"


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    price = Column(Integer(), nullable=False)

    # creating a the realtionship between two tables
    # in this many to many we add an extra argument secondary to indetify the assocoation table
    # and after that we specofy the back_popualte that help us while we query
    customers = relationship(
        'Customer',
        secondary=association, 
        back_populates='products')

    def __repr__(self):
        return f"Product('{self.name}')"


Base.metadata.create_all(engine)

session = sessionmaker()(bind=engine)
