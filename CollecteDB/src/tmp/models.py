from __future__ import annotations

from beanie import Document, Indexed
from pydantic import BaseModel, Field

# The card models:
# CardVersion is used to better keep track of the different versions of the cards in the database
class CardVersion(BaseModel):
    card_count : int = 1
    foil : bool = False
    multiverseID : int | None = None
    set_code : str | None = None
    number: str | None = None

    def to_json(self):
        return {
            'card_count' : self.card_count,
            'foil' : self.foil,
            'multiverseID' : self.multiverseID,
            'set_code' : self.set_code,
            'number': self.number
        }
    
    @staticmethod
    def from_dict(obj: any) -> CardVersion:
        card_count  = obj.get("card_count")
        foil  = obj.get("foil")
        multiverseID  = obj.get("multiverseID")
        set_code  = obj.get("set_code")
        number = obj.get("number")

        return CardVersion(card_count=card_count, 
                            foil= foil,
                            multiverseID = multiverseID,
                            set_code = set_code,
                            number = number)

    def __eq__(self, other : CardVersion):
        return self.foil == other.foil and ((self.number == other.number and self.set_code == other.set_code) or self.multiverseID == other.multiverseID )
    
    def __add__(self, other : CardVersion):
        if not self == other:
            raise Exception("Not adding copies of the same card!")
        
        self.card_count += other.card_count
        
        # And then we update the multiverse IDs etc, for data completeness
        if self.number is None and other.number is not None:
            self.number = other.number
        if self.set_code is None and other.set_code is not None:
            self.set_code = other.set_code
        if self.multiverseID is None and other.multiverseID is not None:
            self.multiverseID = other.multiverseID

        return self
        
# Base model for the cards, currently using a legacy version as this is currently in use with the front end as well 
class Card(BaseModel):
    name : str                          # We need an index on this field
    internal_id : int | None
    versions : list[CardVersion]

    def to_json(self):
        return {
            'name' : self.name,
            'internal_id' : self.internal_id,
            'versions' : [ver.to_json() for ver in self.versions]
        }
    
    @staticmethod
    def from_dict(obj: any):
        name = obj.get("name")
        internal_id = obj.get("internal_id")
        versions = [CardVersion.from_dict(ver) for ver in obj.get("versions")]

        return Card(name=name, internal_id=internal_id, versions = versions)

    def __str__(self):
        return f'{self.name}: {len(self.versions)} versions'
    
    def __eq__(self, other : Card):
        return self.name == other.name
    
    def __add__(self, other : Card):
        """ You can only add cards of the same name together.
        This then adds all the versions of that card to the versions of the other card, increasing each of their counts.
        If a CardVersion is not present in the one, but it is in the other, it gets added to the list of CardVersions.
        """
        if not self == other:
            raise Exception("Not adding copies of the same card!")
        
        for versionOther in other.versions:
            added = False

            for versionSelf in self.versions:
                if versionOther == versionSelf:
                    versionSelf += versionOther
                    added = True
            
            if not added:
                self.versions.append(versionOther)
        
        return self




# {"Cards":[{"name":"asdfasdf","versions":[{"card_count":1}]}]}

# class CardVersion(BaseModel):
#     multiverseid: int = 0
#     count: int = 0

# class CardType(Document):
#     class DocumentMeta:
#         collection_name = "cards"

#     name: Indexed(str, unique = True)
#     items: list[CardVersion]

# class Deck(Document):
#     name: str
#     showcaseCard: int   # This is the internal ID of the card

# class DeckCards(Document):
#     deckId: int
#     cardId: int         # This is the internal ID of the card
#     count:  int

# CardType.update_forward_refs()
# CardVersion.update_forward_refs()