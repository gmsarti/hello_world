from faker import Faker
from src.core.models.social_structures.education_systems import EducationSystem

class EducationSystemGenerator:
 def __init__(self):
     self.fake = Faker()

 def generate_education_system(self):
     name = self.fake.word()
     levels = [self.fake.word() for _ in range(self.fake.random_int(min=1, max=5))]
     students = self.fake.random_int(min=10000, max=100000000)

     return EducationSystem(name=name, levels=levels, students=students)