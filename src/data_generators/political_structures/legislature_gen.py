from faker import Faker
from src.core.models.political_structures.legislature import Legislature

class LegislatureGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_legislature(self):
     name = self.fake.word()
     members = [self.fake.name() for _ in range(self.fake.random_int(min=1, max=5))]
     location = self.fake.city()

     return Legislature(name=name, members=members, location=location)