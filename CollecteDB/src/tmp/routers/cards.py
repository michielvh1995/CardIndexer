from typing import List, Annotated
from fastapi import APIRouter, Body

from ..models import Card, CardVersion

router = APIRouter(
    prefix="/cards",
    tags=["cards"],
    responses={404: {"Description": "Not found"}},
)


mock_cards_data : List[Card] = [
    Card(name = "rings of brighthearth", internal_id= 0, versions=[CardVersion(card_count=1, foil=False, multiverseID=420608)] ),
    Card(name ="sylvan caryatid", internal_id= 1, versions=[CardVersion(card_count = 1)]),
    Card(name ="phyrexian swarmlord", internal_id= 2, versions=[CardVersion(multiverseID = 218086)]),
    Card(name ="deafening silence", internal_id= 3, versions=[CardVersion(card_count = 1)]),
    Card(name ="crashing drawbridge", internal_id= 4, versions=[CardVersion(card_count = 1)]),
    Card(name ="roving keep", internal_id= 5, versions=[CardVersion(card_count = 1)]),
    Card(name ="pia nalaar", internal_id= 6, versions=[CardVersion(card_count = 1)]),
    Card(name ="jaya, venerated firemage", internal_id= 7, versions=[CardVersion(card_count = 1)]),
    Card(name ="force of despair", internal_id= 8, versions=[CardVersion(card_count = 1)]),
    Card(name ="asylum visitor", internal_id= 9, versions=[CardVersion(card_count = 1)]),
    Card(name ="liliana dreadhorde general", internal_id= 10, versions=[CardVersion(card_count = 1)]),
    Card(name ="ob nixilis, the hate-twisted", internal_id= 11, versions=[CardVersion(card_count = 1)])
]

def SearchForCardbyName(name : str, fields : List | None = None) -> tuple[bool, Card| None]:
    """ This function searches the database for the named card. 
    It then returns whether or not it exists and, if present, it's data.
    """
    for card in mock_cards_data:
        if card.name == name:
            return (True, card)
    return (False, None)

def AddCopiesofCard(name : str, copy : Card) -> Card:
    """ This function adds a copy of a card to the database.
    """
    for card in mock_cards_data:
        if card.name == name:

            # Here we either add more cards of the version we already have, to add a new version
            # To check whether or not it is present and updated, we use the updated variable
        

            # Cards with the same multiverse ID can either be foil or not
            for version in card.versions:
                updated : bool = False
                
                for copyVersion in copy.versions:
                    if version.multiverseID == copyVersion.multiverseID and version.foil == copyVersion.foil:
                        version.card_count += copyVersion.card_count
                        updated = True
            
                if not updated:
                    card.versions.append(copy)
                
            return card
                
    

def AddNewCard(copy : Card) -> Card:
    """ This function adds a new not-yet existing card to the database
    """
    internal_id = len(mock_cards_data) + 2
    copy.internal_id = internal_id
    mock_cards_data.append(copy)
    return copy



# Cards API endpoints:

# Returns a list of how many of a specific card are in their locations
# i.e. {swamp: [{collection: 100}, {atraxa:5}] }
@router.get("/location/{card_name}")
async def get_card_locations(card_name:str):
    return { "name": card_name, "loc": [{"location": "name", "count": 0}]}

# Returns how many of a specific card are in the collection
@router.get("/count/{card_name}")
async def get_card_count(card_name:str):
    return { "name": card_name, "count": 0}

# Returns a list of all the card names in the collection
@router.get("/all")
async def get_all_cards():
    return {"Cards" : mock_cards_data}

# Returns all information regarding a card in the collection
@router.get("/{card_name}")
async def get_cards(card_name:str):
    return { }

@router.get("")
async def get_cards(
        name : str | None = None,
        multiverseID : int | None = None,
        internal_id : int | None = None,
        foil : bool = False
    ):

    filters = locals()

    # Filterfunction used to filter the mock database based on the query variables
    def filterFunc(card : Card):
        if name is not None and not card.name == name:
            return False
        if internal_id is not None and not card.internal_id == internal_id:
            return False
        
        if multiverseID is not None and not multiverseID in [vers.multiverseID for vers in card.versions]:
            return False
        
        if foil and not foil in [vers.foil for vers in card.versions]:
            return False
        
        return True
    
    # DEBUG: print the results of the query
    print(list(filter(filterFunc, mock_cards_data)))
    return { "Cards" : list(filter(filterFunc, mock_cards_data)) }


@router.post("/new/")
async def add_card(
        Cards : Annotated[List[Card], Body(embed = True)]
    ):
    print("post: new", Cards)
    updated = []

    for card in Cards:
        search = SearchForCardbyName(card.name)

        # If the card is present in the database we add the new copies
        # and if it is a new card we create a new entry
        if search[0]:
            updated.append(AddCopiesofCard(card.name, card))
        else:
            updated.append(AddNewCard(card))

    return {"Cards": updated}

@router.post("/move/{card_name}")
async def move_card(card_name:str):
    return {}

@router.post("/{card_name}")
async def update_card(card_name:str):
    return {}


@router.put("/updatebyID/{card_id}")
async def update_card_by_ID(card_id : int, new_values : Annotated[Card, Body()]):
    updated_fields : List[str] = []

    for key, value in iter(new_values):
        if value is not None and mock_cards_data[card_id][key] != value:
            updated_fields.append(key)
            mock_cards_data[card_id][key] = value

    return {"updated" : updated_fields}