from __future__ import annotations
import json
from typing import Any

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

    # Extra details regarding the cards. These will be used in a future update
    rarity : str | None
    finish : str  = "nonfoil" # replace foil with this

    def to_json(self):
        return {
            'card_count' : self.card_count,
            'finish' : self.finish,
            'rarity': self.rarity,
            'multiverseID' : self.multiverseID,
            'set_code' : self.set_code,
            'number': self.number
        }
    
    @staticmethod
    def from_dict(obj: any) -> CardVersion:
        card_count  = obj.get("card_count")
        foil  = obj.get("foil", False)
        multiverseID  = obj.get("multiverseID")
        set_code  = str(obj.get("set_code"))
        number = obj.get("number")

        rarity = obj.get("rarity")
        finish = obj.get("finish", "nonfoil")

        if finish == "nonfoil" and foil:
            finish = "foil"

        return CardVersion(card_count=card_count, 
                            foil = foil,
                            multiverseID = multiverseID,
                            set_code = set_code,
                            number = number,
                            rarity =rarity,
                            finish =finish)

    def __eq__(self, other : CardVersion):
        # if (self.finish is not None) and (other.finish is not None):
        #     return self.finish == other.finish and ((self.number == other.number and self.set_code == other.set_code) or (self.multiverseID is not None and other.multiverseID is not None and self.multiverseID == other.multiverseID) )    
        
        return self.foil == other.foil and ((self.number == other.number and self.set_code == other.set_code) or (self.multiverseID is not None and other.multiverseID is not None and self.multiverseID == other.multiverseID) )

    def __gt__(self, rhs : CardVersion):
        if self.set_code > rhs.set_code: return True
        elif self.number > rhs.number: return True
        return self.foil > rhs.foil

    def __lt__(self, rhs : CardVersion):
        if self.set_code < rhs.set_code: return True
        elif self.number < rhs.number: return True
        return self.foil < rhs.foil
    
    def __add__(self, other : CardVersion):
        if not self == other:
            raise Exception("Not adding copies of the same card!")
        
        card_count = self.card_count + other.card_count
        
        # And then we update the multiverse IDs etc, for data completeness
        number = None
        if self.number is not None:
            number = self.number
        elif other.number is not None:
            number = other.number
        
        set_code = None
        if self.set_code is not None:
            set_code = self.set_code
        elif other.set_code is not None:
            set_code = other.set_code

        multiverseID = None
        if self.multiverseID is not None:
            multiverseID = self.multiverseID
        elif other.multiverseID is not None:
            multiverseID = other.multiverseID

        finish = None
        if self.finish is not None:
            finish = self.finish
        elif other.finish is not None:
            finish = other.finish

        rarity = None
        if self.rarity is not None:
            rarity = self.rarity
        elif other.rarity is not None:
            rarity = other.rarity

        return CardVersion(card_count = card_count,
                        set_code=set_code, 
                        number=number, 
                        multiverseID=multiverseID, 
                        foil=self.foil,
                        finish = finish,
                        rarity=rarity)
        
# Base model for the cards, currently using a legacy version as this is currently in use with the front end as well 
class Card(BaseModel):
    name : str                          # We need an index on this field
    internal_id : int | None
    versions : list[CardVersion]

    # Extra details regarding the cards
    colour: list[str] | None

    __name__ = "Card"

    def __len__(self):
        return len(self.versions)


    def __getitem__(self, key : dict[str, any]):
        slc = []
        keys = key.keys()
        
        for i in range(len(self.versions)):
            fits = True

            # Check if each atribute exists on the version, and if it does if it matches the filter value
            for k in keys:
                at = getattr(self.versions[i], k, None)

                if at is not None and at != key[k]:
                    fits = False
                    break
            
            if fits:
                slc.append(i)

        return Card(name=self.name, 
                    internal_id=self.internal_id, 
                    colour=self.colour, 
                    versions=[self.versions[i] for i in slc])

    def to_json(self):
        return {
            'name' : self.name,
            'internal_id' : self.internal_id,
            'colour' : json.dumps(self.colour),
            'versions' : [ver.to_json() for ver in self.versions]
        }
    
    @staticmethod
    def from_dict(obj: any):
        name = obj.get("name")
        internal_id = obj.get("internal_id")
        colour = obj.get("colour")
        versions = [CardVersion.from_dict(ver) for ver in obj.get("versions")]

        if colour is not None:
            colour = json.loads(colour)

        return Card(name=name, internal_id=internal_id, colour=colour, versions = versions)

    def __str__(self):
        return f'{self.name}: {len(self.versions)} versions'
    
    def __eq__(self, other : Card):
        return self.name.lower() == other.name.lower()
    
    def __add__(self, other : Card):
        """ You can only add cards of the same name together.
        This then adds all the versions of that card to the versions of the other card, increasing each of their counts.
        If a CardVersion is not present in the one, but it is in the other, it gets added to the list of CardVersions.
        """
        if not self == other:
            raise Exception("Not adding copies of the same card!")
        
        newVersions = []
        
        # We check per version in the other if it exists in ours
        for versionOther in other.versions:
            added = False

            for versionSelf in self.versions:
                if versionOther == versionSelf:
                    newVersions.append(versionSelf + versionOther)
                    added = True
            
            if not added:
                newVersions.append(versionOther)
        
        for versionSelf in self.versions:
            if not versionSelf in newVersions:
                newVersions.append(versionSelf)
        
        return Card(name=self.name, internal_id=self.internal_id, colour=self.colour, versions=newVersions)




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