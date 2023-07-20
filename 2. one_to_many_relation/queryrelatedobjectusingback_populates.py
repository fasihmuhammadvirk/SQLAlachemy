#importing the session and engine from the other files in which we have already created them
from main import Session
from main import engine

#importing the declarative base to create our models 
from sqlalchemy.ext.declarative import declarative_base

#imorting elements to create models
from sqlalchemy import Column, String, Integer , ForeignKey

#importing the realtion to make a realtion
from sqlalchemy.orm import relationship

#to create our model we need to inherit it from the Base
Base = declarative_base()


class User(Base):
    
    #tablename 
    __tablename__ = 'users_info'
    
    #entities of the table 
    id = Column(Integer(), primary_key = True)
    username = Column(String(40),nullable=False)
    email = Column(String(50),nullable=True)
    
    #specifying the realtion with the post 
    post = relationship('Post',back_populates = 'author')
    
    #this function will be called when we print the object of this class 
    def __repr__(self):
        return f"<User {self.username}>"
    
class Post(Base):
    
    #tablename
    __tablename__ = 'posts'
    
    #entities of the table
    id = Column(Integer(),primary_key=True)
    title = Column(String(45),nullable = False)
    content = Column(String(225),nullable=False)
    
    #to create a realtionship with the table we need to speciy the foreign key 
    #for that we use the ForeignKey
    #in the Foreign Key we specify the tablename and with that what entites we should take as a foriegn key 
    #as in this case users_information is the table and id is the foreign key 
    user_id = Column(Integer(),ForeignKey('users_info.id'))
    
    #in back_populate we have to reverse the realtion like we set the author in the user same we have to do for the post table
    author = relationship('User',back_populates = 'post') 
    
    #this function will be called when we print the object of this class 
    def __repr__(self):
        return f'<User {self.title}>'
        
        
    
Base.metadata.create_all(engine)



#querying


local_session = Session(bind=engine)


user = local_session.query(User).filter(User.id == 1).first()
post = local_session.query(Post).filter(Post.id == 1).first()

#we will get the same answer as the backref but the difference is that backred is used in one db table while the back populate is used in both db table
print(user.post)
print(post.author)




