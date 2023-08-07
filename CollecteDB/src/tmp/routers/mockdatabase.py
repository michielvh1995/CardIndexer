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
   Card(name='Elesh Norn, Mother of Machines', internal_id = 14, versions=[CardVersion(card_count=1)]),
   Card(name='Bilbo, Adventurous Hobbit', internal_id = 15, versions=[CardVersion(card_count=4)]),
   Card(name='Grizzly Bears', internal_id = 16, versions=[CardVersion(card_count=1, multiverseID=129586)]),
   Card(name='Plains', internal_id = 17, versions=[CardVersion(card_count=1, multiverseID=129680), CardVersion(card_count=1, multiverseID=129681), CardVersion(card_count=1, multiverseID=129682), CardVersion(card_count=1, multiverseID=129683), CardVersion(card_count=1, multiverseID=11446), CardVersion(card_count=1), CardVersion(card_count=1, multiverseID=11447), CardVersion(card_count=1), CardVersion(card_count=1, multiverseID=11448), CardVersion(card_count=1), CardVersion(card_count=1, multiverseID=11449), CardVersion(card_count=1)]),
]