from typing import List
from ..models import Card, CardVersion

mock_cards_data : List[Card] = [
   Card(name='rings of brighthearth', internal_id = 0, versions=[CardVersion(card_count=1, multiverseID=420608)]),
   Card(name='sylvan caryatid', internal_id = 1, versions=[CardVersion(card_count=1)]),
   Card(name='phyrexian swarmlord', internal_id = 2, versions=[CardVersion(card_count=1, multiverseID=218086)]),
   Card(name='deafening silence', internal_id = 3, versions=[CardVersion(card_count=1)]),
   Card(name='crashing drawbridge', internal_id = 4, versions=[CardVersion(card_count=1)]),
   Card(name='roving keep', internal_id = 5, versions=[CardVersion(card_count=1)]),
   Card(name='pia nalaar', internal_id = 6, versions=[CardVersion(card_count=1)]),
   Card(name='jaya, venerated firemage', internal_id = 7, versions=[CardVersion(card_count=1)]),
   Card(name='force of despair', internal_id = 8, versions=[CardVersion(card_count=1)]),
   Card(name='asylum visitor', internal_id = 9, versions=[CardVersion(card_count=1)]),
   Card(name='liliana dreadhorde general', internal_id = 10, versions=[CardVersion(card_count=1)]),
   Card(name='ob nixilis, the hate-twisted', internal_id = 11, versions=[CardVersion(card_count=1)]),
   Card(name='Elesh Norn, Mother of Machines', internal_id = 14, versions=[CardVersion(card_count=1), CardVersion(card_count=1, set_code='one', number=415, multiverseID=605318)]),
   Card(name='Bilbo, Adventurous Hobbit', internal_id = 15, versions=[CardVersion(card_count=4)]),
   Card(name='Sword of the Animist', internal_id = 16, versions=[CardVersion(card_count=1, set_code='ltc', number=355)]),
   Card(name='Arwen Undomiel', internal_id = 17, versions=[CardVersion(card_count=2, set_code='ltr', number=194)]),
   Card(name='Great Hall of the Citadel', internal_id = 18, versions=[CardVersion(card_count=2, set_code='ltr', number=254)]),
   Card(name='Forest', internal_id = 19, versions=[CardVersion(card_count=2, set_code='ltr', number=270), CardVersion(card_count=2, set_code='ltr', number=271), CardVersion(card_count=3, set_code='ltr', number=280), CardVersion(card_count=3, set_code='ltr', number=281)]),
   Card(name='Island', internal_id = 20, versions=[CardVersion(card_count=2, set_code='ltr', number=274), CardVersion(card_count=2, set_code='ltr', number=274, foil = True), CardVersion(card_count=1, set_code='ltr', number=275), CardVersion(card_count=2, set_code='ltr', number=275, foil = True)]),
]