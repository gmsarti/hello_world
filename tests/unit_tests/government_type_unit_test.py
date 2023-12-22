import unittest
from src.core.models.political_structures.government_type import GovernmentType
from src.data_generators.political_structures.government_type_gen import GovernmentTypeGenerator

class TestGovernmentType(unittest.TestCase):
 def setUp(self):
    self.generator = GovernmentTypeGenerator()

 def test_generate_government_type(self):
    government_type = self.generator.generate_government_type()
    self.assertIsInstance(government_type, GovernmentType)
    self.assertIsInstance(government_type.name, str)
    self.assertIsInstance(government_type.characteristics, list)
    self.assertIsInstance(government_type.countries, list)

if __name__ == '__main__':
 unittest.main()
