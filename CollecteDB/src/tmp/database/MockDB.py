from .base import DatabaseEngine

from ..models import Card

class MockEngine(DatabaseEngine):
    type = "MockDB"
    Data = {}

    @classmethod
    def InitDatabase(cls, **kwargs):
        cards = kwargs.get('cards', {})
        for card in cards:
            cls.Data[card.name] = card

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
    def QueryByName(cls, name: str):
        if name in cls.Data.keys():
            return [cls.Data[name]]
        return []

    @classmethod
    def GetAll(cls):
        return cls.Data

