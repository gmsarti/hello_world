from faker import Faker
from src.core.models.social_structures.religions import Religion

class ReligionGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_religion(self):
     name = self.fake.word()
     beliefs = [self.fake.sentence() for _ in range(self.fake.random_int(min=1, max=5))]
     practitioners = self.fake.random_int(min=10000, max=100000000)

     return Religion(name=name, beliefs=beliefs, practitioners=practitioners)