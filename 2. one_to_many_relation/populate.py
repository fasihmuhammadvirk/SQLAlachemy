#importing the session and engine to make a sesson to add to a database
from main import Session
from main import engine

#importing the table 
from queryrelatedobjectusingback_populates import Post, User 

#creating the sessoin 
local_session = Session(bind=engine)


#addin the user in the usertable
new_user = User(
    
    username = 'testuser',
    email = 'testuser@gmail.com'
    
)

local_session.add(new_user)
local_session.commit()


#creating a lst of different post 
posts = [
    
    {
        'title':'Learn Django',
        'content': 'Lorem ispum'
    },
    
        {
        'title':'Learn Django',
        'content': 'Lorem ispum'
    },
        {
        'title':'Learn Django',
        'content': 'Lorem ispum'
    },  
        {
        'title':'Learn Django',
        'content': 'Lorem ispum'
    }
]

#quert the user for which you are going to create a post
user = local_session.query(User).filter(User.id == 1).first()

#add the post for the user that we query f
for post in posts:
    new_post = Post(
        
        title=post['title'],
        content = post['content'], 
        #backref author == user 
        author = user
    )

    #addind the post in the database
    local_session.add(new_post)
    local_session.commit()
    
    print(f"post Created {post['title']}")