from faker import Faker
from src.core.models.social_structures.family import Family

class FamilyGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_family(self):
     name = self.fake.last_name()
     members = [self.fake.first_name() for _ in range(self.fake.random_int(min=1, max=5))]
     address = self.fake.street_address()

     return Family(name=name, members=members, address=address)