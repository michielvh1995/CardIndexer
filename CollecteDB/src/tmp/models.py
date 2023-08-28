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

    def __eq__(self, other):
        return self.foil == other.foil and ((self.number == other.number and self.set_code == other.set_code) or self.multiverseID == other.multiverseID )
    
    def __add__(self, other):
        if not self == other:
            raise Exception("Not adding copies of the same card!")
        
        self.card_count += other.card_count
        
        # And then we update the multiverse IDs etc, for data completeness
        if self.number is None and other.number is not None:
            self.number = other.number
        if self.set  is None and other.set is not None:
            self.set = other.set
        if self.multiverseID is None and other.multiverseID is not None:
            self.multiverseID = other.multiverseID
        



# Base model for the cards, currently using a legacy version as this is currently in use with the front end as well 
class Card(BaseModel):
    name : str                          # We need an index on this field
    internal_id : int | None
    versions : list[CardVersion]

    def __str__():
        return "add"
    
    def __eq__(self, other : Card):
        return self.name == other.name
    
    def __add__(self, other : Card):
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