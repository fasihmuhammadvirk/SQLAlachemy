
from main import User, Base

#Creating the database tables 

#the create engine is going to help us in creating database and also connecting with the database 
from sqlalchemy import create_engine


#this is a database url and we can say the connection string
#it contain 
#server://username:password@host:port/databasename
database_url = 'postgresql://postgres:1213@localhost:5432/practice_database'

#creating the engine first argument is the database url or connection string
engine = create_engine(database_url,echo = True)


'''
write the code for your model here 
'''


#this is going to create a database for us and the tables of the database
Base.metadata.create_all(engine)


# now to access the User class enttites and information about it what we can go it to 
# go to the terminal 
# write command : python3
# then after that we can do is
# write command: from main import User as user 
# now to know table name 
# write command: user.__tablename__
# like this we can do is to get information about the table 
# user.__table__

