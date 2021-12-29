
# SQL Commands

> NOTE:
> - All SQL Commands end with a semi-colon
> - It is a good practice to write SQL keywords in uppercase so that the user can easily identify the syntax


#### **REQUIREMENT**: *Create a new database and load the data from a file*

- CREATE DATABASE <nameofdatabse>

```
CREATE movie_data;
```

- USE <nameofdatabase>

```
USE movie_data;
```

- SOURCE <path_to_sql_file>;

```
SOURCE D:\Data\movie_data.sql
```

#### **REQUIREMENT**: *Inspect the database*

- SHOW TABLES;
- DESCRIBE <table_name>

```
DESCRIBE actors;
```

### SELECT

- **Syntax**: ``SELECT * FROM <table_name>;``

Here * represents all the columns. We can specify particular columns as well:``SELECT <col_names_seprated_by_commas> FROM <table_name>;``

- **GOAL**: Display all movies in the database

- **Example**:
```
SELECT * FROM movies;
```

> **NOTE**:
> - Select all columns from the given table
> - This is not recommended generally as in practical scenarios a table might have thousands of columns out of which only a handful might be needed for a given task
> - ``SELECT movie_name,year FROM movies;``

### LIMIT

- **Syntax**: ``SELECT <col_names> FROM <table_name> LIMIT <n>;``

> n is the number of rows to select

- **GOAL**: Select the first 25 movies in the database

- **Example**:
```
SELECT movie_name,year FROM movies LIMIT 25;
```

### OFFSET

- **Syntax**:  ``SELECT <col_names> FROM <table_name> LIMIT <n> OFFSET <x>;``

> x is the number of rows to skip from the top

- **GOAL**: Select and display 25 movies in the database on each page. Do it for the second page

- **Example**:
```
SELECT movie_name,year FROM movies LIMIT 25 OFFSET 50;
```

### Rename Columns in the result set **

- **Example**:
```SELECT name "Naam", rankscore "Izzat" FROM movies```

- Here, the name column would be renamed to Naam and the rankscore column to Izzat which can thought of as Hindi translations for the original column names in this context

### ORDER BY

- **Syntax**: ``SELECT <col_names> FROM <table_name> ORDER BY <col_name>;``

- **GOAL**: Select the top 25 highest rated movies

- **Example**:
```
SELECT movie_name,rankscore,year FROM movies ORDER BY rankscore DESC LIMIT 25;
```

- **Practical Usage**: Sort Products in an e-commerce website like Amazon.com by Price: High to Low or Low to High

> **NOTE: Multiple ORDER BY**:
>
> - It is possible to order the results first by column, then by the second, and so on and so worth
>
> - ```SELECT name,year,rankscore FROM movies ORDER by rankscore DESC, year ASC LIMIT 25;```

### DISTINCT 

- **Syntax**: ``SELECT DISTINCT <col_name> FROM <table_name>``

- **GOAL**: Obtain the list of all available genres

- **Example**
```
SELECT DISTINCT genre FROM movies_genres ORDER BY genre;
```

- **Practical Usage**:
    - Find the possible values for the filters in an e-commerce website like Amazon.com 
    - For Example: For laptops, if we wish to filter it by processor, we first need the list of all the processors found for the products labelled as laptops

> **NOTE**: Multi-Column Distinct:
> - This would consider a concatenation of the values of all the columns.
> Let us consider the following table student_majors:
>
> | First_Name|Last_Name| Major|
> |---|---|---|
> |Smaranjit | Ghose | Data Science|
> |Smaranjit | Ghose | Computer Science|
> | Anurag| Roy | Robotics|
> | Shashwat | Tripathi| Business Analytics|
> |Anurag | Bose | Industrial Engineering|
>
> Now the following query:
>
> ```SELECT DISTINCT First_Name, Last_Name FROM student_majors;```
>
> gives a result set:
>
> | First_Name|Last_Name|
> |---|---|
> |Smaranjit | Ghose | 
> | Anurag| Roy | 
> | Shashwat | Tripathi|
> |Anurag | Bose | 
>
> This can be confusing as the DISTINCT keyword is adjacent to the First_Name column in the above query

### WHERE

- **Syntax**: ``SELECT <col_names> FROM <table_name> WHERE <condition>;``

- **GOAL**: *Display the names of first 25 movies whose rating is above 9.2*

- **Example**
```
SELECT name,year,rankscore FROM movies WHERE rankscore>9.2 ORDER BY rankscore DESC LIMIT 25;
```

- The comparision operators allowed for the conditons are: 
    - < [Less Than]
    - \> [Greater Than]
    - = [Equal to]
    - <= [Less Than or Equal to]
    - \>= [Greater Than or Equal to]
    - <> [Not Equal to]

- **Another Example**:

```
SELECT movie_id FROM movies_genres WHERE genre = "Documentary" LIMIT 25;
```

- For NULL, we have to use `IS` and `IS NOT`


- **Yet Another example**:
```
SELECT movie_id FROM movies_genres WHERE rankscore IS NOT NULL LIMIT 25;
```






# MySQL:

## Starting:

- Open Terminal
- Initiate a MYSQL shell: `mysqlsh`
- Change mode to SQL:  `\sql`
- Connect to the database engine `\connect root@localhost`
    - Enter the password
    - For the purpose of learning, one may save the password but in real world applications, this is not advised
> *NOTE*:
> - Alternatively, one can directly login to the database engine by opening the terminal and writing `mysqlsh -u <username> -p`
> - By default, the username is root unless it was changed (perhaps during the installation phase)


## Miscellaneous:

- Clear Screen: CTRL + L


# Basics of Databases:

- What is a database?
- Why do we need a database?
- Disadvantages of File Systems (comapared to DBMS)
- RDBMS vs Non-RDBMS?
- Two Tier and Three Tier Architecture
- Scheme
- 3 Levels of Abstraction
- Data Independence
- Candidate Key
- Primary Key
- Foreign Key
- Super Key
- ER Model Basics
- Types of Attributes in ER 
- One to One Relationship
- One to Many Relationship
- Many to Many Relationship
- Normalization Basics
- First Normal Form
- Funtional Dependency: Basics, Closure, Properties
- Second Normal Form
- Third Normal Form
- Boyce Codd Normal Form
- Loseless Decomposition
- 


# References:


- [W3schools SQL](https://www.w3schools.com/sql/default.asp): Fundamentals of SQL Commands

- [Mode Analytics](https://mode.com/sql-tutorial/intro-to-advanced-sql/)

- [GATE DMBS Tutorials](https://www.youtube.com/watch?v=mMxjKFiIKxs&list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y&index=8): For theoretical understanding of databases

- [MySQL Documentation](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)



