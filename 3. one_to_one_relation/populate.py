from main import session, Parent, Child 

##comment this session after adding in the database so we can do futher task below 
# #adding the data in the parent table
# parent1 = Parent(name = 'user1')
# parent2 = Parent(name = 'user2' )

# #using session inserted the data in the parent table 
# session.add_all(
#     [
#         parent1,parent2
#     ]
# ) 

# #commit the session so the data is commited in the database
# session.commit()

parents = session.query(Parent).all()

for parent in parents:
    print(parent.name)
    print(parent.id)
    print(parent.child)


#parent1 = session.query(Parent).filter(Parent.id == 1).first()
# parent2 = session.query(Parent).filter(Parent.id == 2).first()

# child1 = Child(name = 'Child 1',parent = parent1)
# child2 = Child(name = 'Child 2',parent = parent2)

##adding one child for each user
# session.add_all(
    
#   [ 
#    child1,child2
#    ]  
    
# )
# session.commit()

parent1 = session.query(Parent).filter(Parent.id == 1).first()


##if we try to add more than one child it will one add the most newest child 
##cause it is a one to one relation

# child1 = Child(name = 'Child 1',parent = parent1)
# session.add(child1)
# session.commit()

child2 = Child(name = 'Child 2',parent = parent1)
session.add(child2)
session.commit()