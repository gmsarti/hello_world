import unittest
from src.core.models.social_structures.professions import Profession
from src.data_generators.social_structures.professions_gen import ProfessionGenerator

class TestProfession(unittest.TestCase):
 def setUp(self):
    self.generator = ProfessionGenerator()

 def test_generate_profession(self):
    profession = self.generator.generate_profession()
    self.assertIsInstance(profession, Profession)
    self.assertIsInstance(profession.title, str)
    self.assertIsInstance(profession.description, str)
    self.assertIsInstance(profession.qualifications, list)

if __name__ == '__main__':
 unittest.main()
