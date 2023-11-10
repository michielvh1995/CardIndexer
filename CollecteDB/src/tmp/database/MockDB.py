import json
from .base import DatabaseEngine

from ..models import Card, CardVersion

class MockEngine(DatabaseEngine):
    type = "MockDB"
    Data = {}

    @classmethod
    def InitDatabase(cls, **kwargs):
        cards = kwargs.get('cards', {})
        
        for key in cards.keys():
            cls.Data[key] = Card.from_dict(cards[key])

    @classmethod
    def InsertCards(cls, cards: list[Card]) -> list[Card]:
        # We keep track of what cards have been udpated:
        updated = []

        # Simple for loop; updates cards if they exist, otherwise inserts them
        for card in cards:
            if card.name in cls.Data.keys():
                cls.Data[card.name] += card
                updated.append(cls.Data[card.name])
            else: 
                cls.Data[card.name] = card
                updated.append(cls.Data[card.name])

        return updated

    @classmethod
    def QueryCards(cls, filters : dict[str, any]) -> list[Card]:
        # Querying cards is a bit more annoying than expected:
        # We have both card and version filters:
        # Card filters are: name & colour
        # Version filters are: rarity, set, collectors number, finish, multiverseID
        selection = []

        if 'name' in filters:
            selection = [cls.Data[cardname] for cardname in cls.Data.keys() if filters["name"].lower() in cardname.lower()]
        else: 
            selection = cls.Data.values()
        
        # Then we filter the cards down to the right colours....
        if 'colours' in filters:
            if filters['cmt'] == '=': 
                selection = [card for card in selection if card.colour is not None and card.colour == filters['colours']]
            if filters['cmt'] == '>=':
                selection = [card for card in selection if card.colour is not None and set(filters['colours']).issubset(card.colour)]
            if filters['cmt'] == '<=': 
                selection = [card for card in selection if card.colour is not None and set(card.colour).issubset(filters['colours'])]
        
        selection = [card[filters] for card in selection]
        selection = [card for card in selection if len(card)]

        return selection
    

    @classmethod
    def QueryByName(cls, name: str):
        if name in cls.Data.keys():
            return [cls.Data[name]]
        return []

    @classmethod
    def GetAll(cls):
        return cls.Data
    
    @classmethod
    def ExportData(cls) -> None:
        cardsData = cls.GetAll()
        dictionized = {}
        for card in [cardsData[key] for key in cardsData.keys()]:
            if len(card): # This if removes cards without versions
                dictionized[card.name] = card.to_json()

        with open('./src/tmp/cardsdata.json', 'w+') as fil:
            json.dump(dictionized, fil, indent=2)
        
        print("stored data")

