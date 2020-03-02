# 0x0D. SQL - Introduction
In this topic we learn about Databases and SQL languaje.

## General
+ What’s a database
+ What’s a relational database
+ What does SQL stand for
+ What’s MySQL
+ How to create a database in MySQL
+ What does `DDL` and `DML` stand for
+ How to `CREATE` or `ALTER` a table
+ How to `SELECT` data from a table
+ How to `INSERT`, `UPDATE` or `DELETE` data
+ What are `subqueries`
+ How to use MySQL functions

## Requirements
+ Allowed editors: `vi, vim, emacs`
+ All your files will be executed on `Ubuntu 14.04 LTS` using `MySQL 5.7` (version 5.7.8-rc)
+ All your SQL queries should have a comment just before (i.e. syntax above)
+ All your files should start by a comment describing the task
+ All SQL keywords should be in uppercase (`SELECT, WHERE…`)
+ The length of your files will be tested using `wc`

## Comments for SQL
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Tasks

### 0. List databases
Write a script that lists all databases of your MySQL server.
File: [0-list_databases.sql](0-list_databases.sql)

### 1. Create a database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.
File: [1-create_database_if_missing.sql](1-create_database_if_missing.sql)

### 2. Delete a database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
File: [2-remove_database.sql](2-remove_database.sql)

### 3. List tables
Write a script that lists all the tables of a database in your MySQL server.
File: [3-list_tables.sql](3-list_tables.sql)

### 4. First table
Write a script that creates a table called `first_table` in the current database in your MySQL server.
File: [4-first_table.sql](4-first_table.sql)

### 5. Full description
Write a script that prints the full description of the table first_table from the database `hbtn_0c_0` in your MySQL server.
File: [5-full_table.sql](5-full_table.sql)

### 6. List all in table
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
File: [6-list_values.sql](6-list_values.sql)

