from main import User
from create_db import engine
from create_users import Session

#create a local session 
local_session = Session(bind=engine)


###for all the objects###
#create a query to fetch of all the users data in the User Table
users = local_session.query(User).all()

#printing all of the data at once 
for user in users:
    print(user.username)
    

print('Limited Data')
#limiting the data we fetch 
#let say we only want the data uptop 3 rows 

userss = local_session.query(User).all()[:3]

for user in userss:
    print(user.username)
    

###for one object###
masif = local_session.query(User).filter(User.username == 'masif').first() #the first user has the name masif 

#it will give only the information about masif user in the database
print(masif)