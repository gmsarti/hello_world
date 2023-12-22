from faker import Faker
from src.core.models.political_structures.government_type import GovernmentType

class GovernmentTypeGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_government_type(self):
     name = self.fake.word()
     characteristics = [self.fake.sentence() for _ in range(self.fake.random_int(min=1, max=5))]
     countries = [self.fake.country() for _ in range(self.fake.random_int(min=1, max=5))]

     return GovernmentType(name=name, characteristics=characteristics, countries=countries)

