# This python file uses SQLAlchemy to perform CRUD operations on an sqlite database


# The sys module provides a number of functions and variables that can be used to used
# to manipulate different parts of the Python runtime environment.
import sys

# The following imports will come in handy when writing the mapper code.
from sqlalchemy import Column, ForeignKey, Integer, String

# The following will be used in the configuration and class code.
from sqlalchemy.ext.declarative import declarative_base

# Creates the foreign key relationships. This will be used when writing the mapper
from sqlalchemy.orm import relationship

# Will be used in the configuration code at the end of file.
from sqlalchemy import create_engine

# Makes an instance of the declarative_base() class. The declarative_base will let
# sqlAlchemy know that our classes are special sqlAlchemy classes that correspond to
# tables in our database
Base = declarative_base()

# Class code is the object oriented representation of a table in the database.
# This class extends from the Base class that I created above.
# This class will have all of the table and mapper code
class Restaurant(Base):
    # Table representation. The double underscore syntax lets sqlAlchemy know
	# which variable to refer to for the table.
	__tablename__ = 'restaurant'
	
	# The mapper code creates variables that will be used to create columns
	# in the database.
	# When creating a column you must also pass in attributes to that column
	name = Column(String(80), nullable = False)

	id = Column(Integer, primary_key = True)



class MenuItem(Base):
    __tablename__ = 'menu_item'
	
    name = Column(String(80), nullable = False)

    id = Column(Integer, primary_key = True)
	
    course = Column(String(250))
	
    description = Column(String(250))
	
    price = Column(String(8))
	
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	
    restaurant = relationship(Restaurant)







####### Insert at End of File #######

# Create instance of create_engine class and point to the database to be used
engine = create_engine('sqlite:///restaurantmenu.db')
# Goes into database and adds the classes we will soon create as new tables in our database.
Base.metadata.create_all(engine)

