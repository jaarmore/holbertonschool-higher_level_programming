# 0x0F. Python - Object-relational mapping
In this project we learn about how to use an ORM to connect to a DataBase

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (dont ask me how to pronounce it) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be What can I do with my objects and not How this object is stored? where? when?. You wont write any SQL queries only Python code. Last thing, your code wont be storage type dependent. You will be able to change your storage easily without re-writing your entire project.

## General
+ Why Python programming is awesome
+ How to connect to a MySQL database from a Python script
+ How to SELECT rows in a MySQL table from a Python script
+ How to INSERT rows in a MySQL table from a Python script
+ What ORM means
+ How to map a Python Class to a MySQL table

## General
+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted/compiled on `Ubuntu 14.04 LTS` using `python3 (version 3.4.3)`
+ Your files will be executed with `MySQLdb` version 1.3.x
+ Your files will be executed with `SQLAlchemy` version 1.2.x
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/python3`
+ Your code should use the `PEP 8` style (version 1.7.*)
+ All your files must be executable

## Tasks

### [0. Get all states](0-select_states.py)
Script that lists all states from the database hbtn_0e_0_usa.

### [1. Filter states](1-filter_states.py)
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

### [2. Filter states by user input](2-my_filter_states.py)
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

### [3. SQL Injection...](3-my_safe_filter_states.py)
script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

### [4. Cities by states](4-cities_by_state.py)
Script that lists all cities from the database hbtn_0e_4_usa.

### [5. All cities by state](5-filter_cities.py)
script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.

### [6. First state model](model_state.py)
python file that contains the class definition of a State and an instance Base = declarative_base().

### [7. All states via SQLAlchemy](7-model_state_fetch_all.py)
Script that lists all State objects from the database hbtn_0e_6_usa.

### [8. First state](8-model_state_fetch_first.py)
Script that prints the first State object from the database hbtn_0e_6_usa.

### [9. Contains `a`](9-model_state_filter_a.py)
script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.

### [10. Get a state](10-model_state_my_get.py)
Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.

### [11. Add a new state](11-model_state_insert.py)
script that adds the State object Louisiana to the database hbtn_0e_6_usa.

### [12. Update a state](12-model_state_update_id_2.py)
script that changes the name of a State object from the database hbtn_0e_6_usa.

### [13. Delete states](13-model_state_delete_a.py)
script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.

### [14. Cities in state](model_city.py, 14-model_city_fetch_by_state.py)
Python file similar to model_state.py named model_city.py that contains the class definition of a City.

## AUTHOR
**_Jackson Moreno_**
