from faker import Faker
from src.core.models.person import Person

class PersonGenerator:
  def __init__(self):
      self.fake = Faker()

  def generate_person(self):
      name = self.fake.name()
      age = self.fake.random_int(min=18, max=100)
      gender = self.fake.random_element(['male', 'female'])
      nationality = self.fake.country()

      return Person(name=name, age=age, gender=gender, nationality=nationality)
