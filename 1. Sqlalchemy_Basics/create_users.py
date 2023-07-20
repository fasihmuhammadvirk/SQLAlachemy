#sqlalcehmy offers sessions these sessoin allow use to do CRUD operation on the database

from sqlalchemy.orm import sessionmaker #used for creating sessions 
from create_db import engine 
from main import User 

#creating a session for doing operations on the database
Session = sessionmaker()
local_session = Session(bind=engine)

#creating a lst of dic for different users to add in the database

users = [    
    {
        'username':'jhon',
        'password':'1213',
        'email': 'jhon@company.com'
        
    },
        {
        'username':'jhon1',
        'password':'1213',
        'email': 'jhon1@company.com'
        
    },
            {
        'username':'jhon2',
        'password':'1213',
        'email': 'jhon2@company.com'
        
    },
                {
        'username':'jhon3',
        'password':'1213',
        'email': 'jhon3@company.com'
        
    },
                    {
        'username':'jhon4',
        'password':'1213',
        'email': 'jhon4@company.com'
        
    },    
]

#adding multiple users in the database 
# for user in users:
#     new_user = User(username = user['username'] , password = user['password'], email = user['email'])
#     local_session.add(new_user)
#     local_session.commit()
#     print(f"Added User {user['username']}")
# print('User added successfully!')

#added a new user in the database 
# new_user = User(username = 'masif', password = '1213', email = 'masif.virk@gmail.com')
# local_session.add(new_user)
# local_session.commit()