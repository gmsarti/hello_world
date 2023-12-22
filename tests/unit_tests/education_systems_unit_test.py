import unittest
from src.core.models.social_structures.education_systems import EducationSystem
from src.data_generators.social_structures.education_systems_gen import EducationSystemGenerator

class TestEducationSystem(unittest.TestCase):
 def setUp(self):
    self.generator = EducationSystemGenerator()

 def test_generate_education_system(self):
    education_system = self.generator.generate_education_system()
    self.assertIsInstance(education_system, EducationSystem)
    self.assertIsInstance(education_system.name, str)
    self.assertIsInstance(education_system.levels, list)
    self.assertIsInstance(education_system.students, int)

if __name__ == '__main__':
 unittest.main()
