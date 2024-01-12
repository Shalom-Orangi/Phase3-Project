# Phase3-Project
In this project, we're going to use these skills to create a CLI. We want you to display knowledge of as much from Phase 3 as you can- you won't be able to fit everything in, but we'll expect to see:

A CLI application that solves a real-world problem and adheres to best practices.
A database created and modified with SQLAlchemy ORM with 3+ related tables.
A well-maintained virtual environment using Pipenv.
Proper package structure in your application.
Use of lists, dicts, and tuples.
Appropriate and accurate implementation of an algorithm from the Data Structures and Algorithms Canvas module.

**The Pet Adoption Platform**
This is a platform that helps a pet adoption centre to manage all the records to do with the dogs they rescue and put up for adoption
The platform contains 3 tables : 
i)Pets table (pet_name ,breed,age,adoption_date)
ii)Adopters Table(adopter's_first_name, last_name,email,pet_id)
iii)Adoptions table (adopter's_id,pet_id,application_status,adoption_fee,adoption_date)

It contains migrations made through alembic
It contains one to many and many-to-many relationships between the tables
It contains cli.py file that contains commands that can edit/upgrade the information in the database
It also has a seed.py file that populates the db
It also contains the use of lists and tuples in both the cli and seed files

# Project by:
**Shalom Orangi**
