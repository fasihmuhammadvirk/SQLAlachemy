
from sqlalchemy import create_engine
database_url = 'postgresql://postgres:1213@localhost:5432/practice_database'
engine = create_engine(database_url,echo = True)
from sqlalchemy.orm import sessionmaker 
session = sessionmaker()(bind=engine)

from sqlalchemy import(
    
    Column,
    String,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#creating the parent class 
class Parent(Base):
    
    __tablename__ = 'parent'
    
    id = Column(Integer(),primary_key = True )
    name = Column(String(25),nullable = False)    
    #configurating the delete by cascade 
    #that if we delete the parent its child should be delete with him
    child = relationship('Child',back_populates='parent',uselist=False,cascade='all, delete')
    
    
    def __repr__(self):
    
        return f'<Parent {self.id}'


#child class 
class Child(Base):
    
    __tablename__ = 'child'
    
    id = Column(Integer(),primary_key=True)
    name = Column(String(25),nullable= False)
    #and in foregin key we also have to add one extra argument to config delete 
    parent_id = Column(Integer(),ForeignKey('parent.id',ondelete='CASCADE'))
    parent = relationship('Parent',back_populates='child')
    
    def __repr__(self):
        return f'<Child {self.id}>'
    

Base.metadata.create_all(engine)

#cheking all the parents and childs
print(f'Parents {session.query(Parent).all()}')
print(f'Child {session.query(Child).all()}')

#this session was commented after deleting the parent1 
# parent_to_delete = session.query(Parent).filter(Parent.id == 1).first()


# session.delete(parent_to_delete)
# session.commit()

# print(parent_to_delete)
# print(parent_to_delete.child)