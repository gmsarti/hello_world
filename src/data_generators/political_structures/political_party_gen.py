from faker import Faker
from src.core.models.political_structures.political_party import PoliticalParty

class PoliticalPartyGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_political_party(self):
     name = self.fake.word()
     ideology = self.fake.sentence()
     leaders = [self.fake.name() for _ in range(self.fake.random_int(min=1, max=5))]

     return PoliticalParty(name=name, ideology=ideology, leaders=leaders)