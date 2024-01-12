from models import Pet,Adopter,Adoption,Base,engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

engine=create_engine ("sqlite:///pets.db")
Session=sessionmaker(bind=engine)
session_obj=Session()


fake=Faker()
print("Seeding to the db")


pet_name=["Snowy","Roxy","Rusty","Bosco","Stitch","Blackie","Boki","Rupers","Trixie","Cuddles"]
breed=["Bulldog","German Shepherd","Chihuahua","Golden Retriever","Daschund","Spaniel","Poodle","Labrador","Husky","Havanese"]
application_status=["Pending","Approved","Rejected"]
ages=["3","4","5","7","12","11","10","8","2","1"]

adopter=[
    Adopter(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email()
    )
for _ in range(10)]

session_obj.bulk_save_objects(adopter)
session_obj.commit()

pet=[
    Pet(
        name=random.choice(pet_name),
        breed=random.choice(breed),
        age=random.choice(ages),
)for _ in range(10)]
session_obj.bulk_save_objects(pet)
session_obj.commit()


adoptions=[
    Adoption(
            adoption_fee=random.randint(0,90000),
            application_status=random.choice(application_status)
        )for _ in range(10)]
session_obj.bulk_save_objects(adoptions)
session_obj.commit()    

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    


print("seeding complete")

