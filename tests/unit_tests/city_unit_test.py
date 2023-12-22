import unittest
from src.core.models.city import City
from src.data_generators.city_gen import CityGenerator

class TestCity(unittest.TestCase):
   def setUp(self):
       self.city = City(name="New York", population=8622698, area=783.8, currency="USD", language="en")

   def test_city_properties(self):
       self.assertEqual(self.city.name, "New York")
       self.assertEqual(self.city.population, 8622698)
       self.assertEqual(self.city.area, 783.8)
       self.assertEqual(self.city.currency, "USD")
       self.assertEqual(self.city.language, "en")

class TestCityGenerator(unittest.TestCase):
   def setUp(self):
       self.generator = CityGenerator()

   def test_generate_city(self):
       city = self.generator.generate_city()
       self.assertIsInstance(city, City)
       self.assertIsInstance(city.name, str)
       self.assertIsInstance(city.population, int)
       self.assertIsInstance(city.area, float)
       self.assertIsInstance(city.currency, str)
       self.assertIsInstance(city.language, str)

if __name__ == '__main__':
   unittest.main()
