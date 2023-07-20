from main import User
from create_db import engine
from create_users import Session

#create a local session 
local_session = Session(bind=engine)

#create a query for whcih user you want to delete 
user_to_delete = local_session.query(User).filter(User.username == 'jhon').first()

#delte user  
local_session.delete(user_to_delete)
#commmit 
local_session.commit()