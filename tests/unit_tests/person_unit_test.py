import unittest
from src.core.models.person import Person
from src.data_generators.person_gen import PersonGenerator

class TestPerson(unittest.TestCase):
  def setUp(self):
      self.generator = PersonGenerator()

  def test_generate_person(self):
      person = self.generator.generate_person()
      self.assertIsInstance(person, Person)
      self.assertIsInstance(person.name, str)
      self.assertIsInstance(person.age, int)
      self.assertIsInstance(person.gender, str)
      self.assertIsInstance(person.nationality, str)

if __name__ == '__main__':
  unittest.main()
