import os

def create_file_structure(base_dir, structure):
   for key, value in structure.items():
       new_item = os.path.join(base_dir, key)
       if isinstance(value, dict):
           os.makedirs(new_item, exist_ok=True)
           create_file_structure(new_item, value)
       else:
           open(new_item, 'w').close()

file_structure = {
   'src': {
       'core': {
           'models': {
               'country.py': {},
               'city.py': {},
               'person.py': {}
           },
           'main.py': {}
       },
       'data_generators': {
           'country_generator.py': {},
           'city_generator.py': {},
           'person_generator.py': {}
       },
       'social_structures': {
           'family.py': {},
           'profession.py': {},
           'religion.py': {},
           'education_system.py': {}
       },
       'political_structures': {
           'government_type.py': {},
           'political_party.py': {},
           'legislature.py': {},
           'judiciary.py': {}
       },
       'interactions.py': {}
   },
   'tests': {
       'unit_tests': {
           'test_country.py': {},
           'test_city.py': {},
           'test_person.py': {}
       },
       'integration_tests': {
           'test_world_creation.py': {},
           'test_world_simulation.py': {}
       }
   },
   'docs': {
       'design_documents': {},
       'user_manual.md': {}
   },
   'scripts': {
       'run_world_generator.sh': {}
   }
}

create_file_structure('.', file_structure)
