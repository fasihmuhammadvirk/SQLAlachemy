
#the create engine is going to help us in creating database and also connecting with the database 
from sqlalchemy import create_engine


#this is a database url and we can say the connection string
#it contain 
#server://username:password@host:port/databasename
database_url = 'postgresql://postgres:1213@localhost:5432/practice_database'

#creating the engine first argument is the database url or connection string
engine = create_engine(database_url,echo = True)

from sqlalchemy.orm import sessionmaker #used for creating sessions 

#creating a session for doing operations on the database
Session = sessionmaker()

#creating a lst of dic for different users to add in the database