from faker import Faker
from src.core.models.settlements.city import City

class CityGenerator:
   def __init__(self):
       self.fake = Faker()

   def generate_city(self):
       name = self.fake.city()
       population = self.fake.random_int(min=1000, max=1_000_000)
       area = self.fake.random_number(digits=10) / 1_000_000.0 
       currency = self.fake.currency_code()
       language = self.fake.language_code()

       return City(name=name, population=population, area=area, currency=currency, language=language)
