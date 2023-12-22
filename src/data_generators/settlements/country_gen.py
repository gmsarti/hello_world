from faker import Faker
from src.core.models.settlements.country import Country

class CountryGenerator:
   def __init__(self):
       self.fake = Faker()

   def generate_country(self):
       name = self.fake.country()
       population = self.fake.random_int(min=1000000, max=1000000000)
       area = self.fake.random_number(digits=10) / 1000000.0
    #    TODO criar um gerador de nome de cidade aleatório
       capital = "Cidade Aleatória"
       currency = self.fake.currency_code()

       return Country(name=name, population=population, area=area, capital=capital, currency=currency)
