import unittest
from src.core.models.political_structures.judiciary import Judiciary
from src.data_generators.political_structures.judiciary_gen import JudiciaryGenerator

class TestJudiciary(unittest.TestCase):
 def setUp(self):
   self.generator = JudiciaryGenerator()

 def test_generate_judiciary(self):
   judiciary = self.generator.generate_judiciary()
   self.assertIsInstance(judiciary, Judiciary)
   self.assertIsInstance(judiciary.name, str)
   self.assertIsInstance(judiciary.judges, list)
   self.assertIsInstance(judiciary.location, str)

if __name__ == '__main__':
 unittest.main()
