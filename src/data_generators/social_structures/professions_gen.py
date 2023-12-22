from faker import Faker
from src.core.models.social_structures.professions import Profession

class ProfessionGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_profession(self):
     title = self.fake.job()
     description = self.fake.sentence()
     qualifications = [self.fake.word() for _ in range(self.fake.random_int(min=1, max=5))]

     return Profession(title=title, description=description, qualifications=qualifications)