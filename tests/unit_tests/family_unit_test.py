import unittest
from src.core.models.social_structures.family import Family
from src.data_generators.social_structures.family_gen import FamilyGenerator

class TestFamily(unittest.TestCase):
 def setUp(self):
    self.generator = FamilyGenerator()

 def test_generate_family(self):
    family = self.generator.generate_family()
    self.assertIsInstance(family, Family)
    self.assertIsInstance(family.name, str)
    self.assertIsInstance(family.members, list)
    self.assertIsInstance(family.address, str)

if __name__ == '__main__':
 unittest.main()
