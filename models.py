from sqlalchemy import Column,String,Integer,DateTime,create_engine,ForeignKey,func,Table
from sqlalchemy.orm import declarative_base,sessionmaker,relationship

Base=declarative_base()

engine=create_engine("sqlite:///pet.db", echo=True)

Session=sessionmaker(bind=engine)
session_obj=Session()

#used for the many-to-many rel
adoption_association= Table(
    'adoption_association',
    Base.metadata,
    Column('adopter_id',Integer,ForeignKey('adopters.id')),
    Column('pet_id',Integer,ForeignKey('pets.id')),
    Column('adoption_id',Integer,ForeignKey('adoptions.id'))
)

class Pet(Base):
    __tablename__='pets'

    #columns
    id=Column(Integer,primary_key=True)
    name=Column(String)
    breed=Column(String)
    age=Column(Integer)
    adoption_date = Column(DateTime, default=func.now()) 
    adoption_id=Column(Integer,ForeignKey('adoptions.id'))
    #rel
    adopters= relationship ('Adopter',secondary=adoption_association,back_populates='pets')
    adoptions=relationship('Adoption',secondary=adoption_association,back_populates='pets')


    def __repr__(self):
        return f"Pet(id={self.id},name={self.name},breed={self.breed}, age={self.age}, adoption_date={self.adoption_date})>"

    @classmethod
    def create_from_dict(cls,pet_data):
        return cls(name=pet_data.get('name'), breed=pet_data.get('breed'))
    

class Adopter(Base):
    __tablename__='adopters'

    #columns
    id=Column(Integer,primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String)
    pet_id=Column(Integer,ForeignKey('pets.id'))
    adoption_id=Column(Integer,ForeignKey('adoptions.id'))
    
    #rel
    pets=relationship('Pet',secondary=adoption_association,back_populates='adopters')
    adoptions=relationship('Adoption',secondary=adoption_association,back_populates='adopters')

    def __repr__(self):
        return f"<Adopter(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, pet_id={self.pet_id})>"

class Adoption(Base):
    __tablename__='adoptions'

    #columns
    id=Column(Integer,primary_key=True)
    adoption_date = Column(DateTime, default=func.now()) 
    adoption_fee= Column(Integer)
    application_status=Column(String)
    adopter_id=Column(Integer,ForeignKey('adopters.id'))
    pet_id=Column(Integer,ForeignKey('pets.id'))

    #rel
    pets=relationship('Pet', back_populates='adoptions')
    adopters=relationship('Adopter',back_populates='adoptions')

    def __repr__(self):
        return f"<Adoption (id={self.id},adopter_id={self.adopter_id}, pet_id={self.pet_id},adoption_date={self.adoption_date}, adoption_fee={self.adoption_fee},application_status={self.application_status}3)>"
    
    @classmethod
    def display_pet_info(cls,session):
        adoptions=session.query(cls).all()
        for adoption in adoptions:
            pet_info=f"Pet:{adoption.pet.name}, Breed :{adoption.pet.breed}, Adopter:{adoption.adopter.first_name} {adoption.adopter.last_name}, Adoption Date:{adoption.adoption_date}"
            print (pet_info)

