import unittest
from src.core.models.country import Country
from src.data_generators.country_gen import CountryGenerator

class TestCountry(unittest.TestCase):
   def setUp(self):
       self.generator = CountryGenerator()

   def test_generate_country(self):
       country = self.generator.generate_country()
       self.assertIsInstance(country, Country)
       self.assertIsInstance(country.name, str)
       self.assertIsInstance(country.population, int)
       self.assertIsInstance(country.area, float)
       self.assertIsInstance(country.capital, str)
       self.assertIsInstance(country.currency, str)

if __name__ == '__main__':
   unittest.main()
