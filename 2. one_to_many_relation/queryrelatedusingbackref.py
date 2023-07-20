#importing the session and engine to make a sesson to add to a database
from main import Session
from main import engine

#importing the table 
from onetomany import Post, User 

#creating the sessoin 
local_session = Session(bind=engine)


#quert the user for which you are going to create a post
user = local_session.query(User).filter(User.id == 1).first()

#query the post in the post table to and getting the first post 
post = local_session.query(Post).filter(Post.id == 1).first()

#this below represent the one to many and many to one relationship 

#checking all the post of the user 
print(user.post)

#checking the author of the post that we query
print(post.author)

