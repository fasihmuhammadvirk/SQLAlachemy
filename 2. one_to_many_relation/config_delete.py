from main import Session
from main import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer , ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    
    #tablename 
    __tablename__ = 'users_info'
    
    id = Column(Integer(), primary_key = True)
    username = Column(String(40),nullable=False)
    email = Column(String(50),nullable=True)
    
    #configurating the delete behaviour
    
    #if we want that ke if we delete the user so all of the user post should be deleted with him for that
    #we have to use cascade we can define it as cascase = 'all,delete' and it will delete the all post if we delete the user
    post = relationship('Post',back_populates = 'author',cascade= 'all , delete')
    
    def __repr__(self):
        return f"<User {self.username}>"
    
class Post(Base):
    
    #tablename
    __tablename__ = 'posts'
    
    id = Column(Integer(),primary_key=True)
    title = Column(String(45),nullable = False)
    content = Column(String(225),nullable=False)
    user_id = Column(Integer(),ForeignKey('users_info.id'))
    author = relationship('User',back_populates = 'post') 
    
    def __repr__(self):
        return f'<User {self.title}>'
        
        
    
Base.metadata.create_all(engine)


### Querying to Delete User ###

local_session = Session(bind= engine)

user_to_del = local_session.query(User).filter(User.id == 1).first()
local_session.delete(user_to_del)
local_session.commit()


all_posts = local_session.query(Post).all()
all_user = local_session.query(Post).all()

print(all_user)
print(all_posts)