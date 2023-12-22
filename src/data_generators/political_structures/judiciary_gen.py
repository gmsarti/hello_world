from faker import Faker
from src.core.models.political_structures.judiciary import Judiciary

class JudiciaryGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_judiciary(self):
     name = self.fake.word()
     judges = [self.fake.name() for _ in range(self.fake.random_int(min=1, max=5))]
     location = self.fake.city()

     return Judiciary(name=name, judges=judges, location=location)