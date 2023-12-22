import unittest
from src.core.models.social_structures.religions import Religion
from src.data_generators.social_structures.religions_gen import ReligionGenerator

class TestReligion(unittest.TestCase):
 def setUp(self):
    self.generator = ReligionGenerator()

 def test_generate_religion(self):
    religion = self.generator.generate_religion()
    self.assertIsInstance(religion, Religion)
    self.assertIsInstance(religion.name, str)
    self.assertIsInstance(religion.beliefs, list)
    self.assertIsInstance(religion.practitioners, int)

if __name__ == '__main__':
 unittest.main()
