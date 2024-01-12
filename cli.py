import click
from models import Adopter, Pet, Adoption, Base, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random


engine=create_engine ("sqlite:///pets.db")
Session=sessionmaker(bind=engine)
session_obj=Session()

fake=Faker()

@click.group()
def cli():
    pass

@cli.command()
def display_pet_info():
    """Display information about pets with their adopters and adoption dates."""
    adoptions=session_obj.query(Adoption).all()
    for adoption in adoptions:
        pet_info=f"Pet:{adoption.pet.name}, Breed :{adoption.pet.breed}, Adopter:{adoption.adopter.first_name} {adoption.adopter.last_name}, Adoption Date:{adoption.adoption_date}"
        print (pet_info)

@cli.command()
def add_new_pet():
    """Add new pet to the database"""
    breed=["Bulldog","German Shepherd","Chihuahua","Golden Retriever","Daschund","Spaniel","Poodle","Labrador","Husky","Havanese"]

    pet_data = {
        'name':fake.first_name(),
        'breed':random.choice(breed),
        'age':random.randint(0,20),
    }
    pet=Pet.create_from_dict(pet_data)
    session_obj.add(pet)

    adopter_data={
        'first_name': fake.first_name(),
        'last_name' :fake.last_name(),
        'email': fake.email()
    }

    adopter=Adopter(**adopter_data)
    session_obj.add(adopter)

    adoption=Adoption(adopter=adopter, pet=pet)
    session_obj.add(adoption)

    session_obj.commit()
    print("New pet added successfully")

@cli.command()
def query_adopters():
    """Query and display information about adopters."""
    adopters=session_obj.query(Adopter).all()
    for adopter in adopters:
        adopter_info= f"<Adopter(id={adopter.id}, first_name={adopter.first_name}, last_name={adopter.last_name}, email={adopter.email}, pet_id={adopter.pet_id})>"
        print(adopter_info)


if __name__=="__main__":
    Base.metadata.create_all(bind=engine)
    cli()