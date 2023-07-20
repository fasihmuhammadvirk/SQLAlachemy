from main import User
from create_db import engine
from create_users import Session

#create a local session 
local_session = Session(bind=engine)

#create a query for whcih user you want to update 
user_to_update = local_session.query(User).filter(User.username == 'masif').first()

#updtae user entities 
user_to_update.username = 'fasih'
user_to_update.email = 'fasih@gmail.com'

#commmit 
local_session.commit()