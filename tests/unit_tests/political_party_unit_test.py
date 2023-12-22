import unittest
from src.core.models.political_structures.political_party import PoliticalParty
from src.data_generators.political_structures.political_party_gen import PoliticalPartyGenerator

class TestPoliticalParty(unittest.TestCase):
 def setUp(self):
   self.generator = PoliticalPartyGenerator()

 def test_generate_political_party(self):
   political_party = self.generator.generate_political_party()
   self.assertIsInstance(political_party, PoliticalParty)
   self.assertIsInstance(political_party.name, str)
   self.assertIsInstance(political_party.ideology, str)
   self.assertIsInstance(political_party.leaders, list)

if __name__ == '__main__':
 unittest.main()
