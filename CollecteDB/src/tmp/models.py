from typing import Optional, List

from beanie import Document, Indexed
from pydantic import BaseModel, Field

class Card(BaseModel):
    name : str
    card_count : int = 1
    foil : bool = False
    multiverseID : int | None = None
    set_code : str | None = None
    internal_id : int | None = None


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