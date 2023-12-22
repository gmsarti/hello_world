import unittest
from src.core.models.political_structures.legislature import Legislature
from src.data_generators.political_structures.legislature_gen import LegislatureGenerator

class TestLegislature(unittest.TestCase):
 def setUp(self):
   self.generator = LegislatureGenerator()

 def test_generate_legislature(self):
   legislature = self.generator.generate_legislature()
   self.assertIsInstance(legislature, Legislature)
   self.assertIsInstance(legislature.name, str)
   self.assertIsInstance(legislature.members, list)
   self.assertIsInstance(legislature.location, str)

if __name__ == '__main__':
 unittest.main()
