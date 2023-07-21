from typing import Optional, List

from beanie import Document, Indexed
from pydantic import BaseModel, Field


# The card models:
# CardVersion is used to better keep track of the different versions of the cards in the database
class CardVersion(BaseModel):
    card_count : int = 1
    foil : bool = False
    multiverseID : int | None = None    # We need an index on this field
    set_code : str | None = None

# Base model for the cards, currently using a legacy version as this is currently in use with the front end as well 
class Card(BaseModel):
    name : str                          # We need an index on this field
    internal_id : int | None
    versions : List[CardVersion]

    def __str__():
        return "add"

# {"Cards":[{"name":"asdfasdf","versions":[{"card_count":1}]}]}

# class CardVersion(BaseModel):
#     multiverseid: int = 0
#     count: int = 0

# class CardType(Document):
#     class DocumentMeta:
#         collection_name = "cards"

#     name: Indexed(str, unique = True)
#     items: List[CardVersion]

# class Deck(Document):
#     name: str
#     showcaseCard: int   # This is the internal ID of the card

# class DeckCards(Document):
#     deckId: int
#     cardId: int         # This is the internal ID of the card
#     count:  int

# CardType.update_forward_refs()
# CardVersion.update_forward_refs()