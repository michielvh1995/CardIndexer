from typing import List, Annotated
from fastapi import APIRouter, Body

from ..models import Card

router = APIRouter(
    prefix="/cards",
    tags=["cards"],
    responses={404: {"Description": "Not found"}},
)

mock_cards_data : List[Card] = [
        { "foil" : False, "internal_id": 0, "name": "rings of brighthearth", "card_count": 1, "multiverseID": 420608},
        { "foil" : False, "internal_id": 1, "name": "sylvan caryatid", "card_count": 1},
        { "foil" : False, "internal_id": 2, "name": "phyrexian swarmlord", "card_count": 1, "multiverseID": 218086},
        { "foil" : False, "internal_id": 3, "name": "deafening silence", "card_count": 1},
        { "foil" : False, "internal_id": 4, "name": "crashing drawbridge", "card_count": 1},
        { "foil" : False, "internal_id": 5, "name": "roving keep", "card_count": 1},
        { "foil" : False, "internal_id": 6, "name": "pia nalaar", "card_count": 1},
        { "foil" : False, "internal_id": 7, "name": "jaya, venerated firemage", "card_count": 1},
        { "foil" : False, "internal_id": 8, "name": "force of despair", "card_count": 1},
        { "foil" : False, "internal_id": 9, "name": "asylum visitor", "card_count": 1},
        { "foil" : False, "internal_id": 10, "name": "liliana dreadhorde general", "card_count": 1},
        { "foil" : False, "internal_id": 11, "name": "ob nixilis, the hate-twisted", "card_count": 1}
    ]

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
        for key, value in filters.items():

            if value is not None and card[key] != value:
                return False
            
        return True
    
    # DEBUG: print the results of the query
    print(list(filter(filterFunc, mock_cards_data)))
    return { "Cards" : list(filter(filterFunc, mock_cards_data)) }


@router.post("/new/")
async def add_card(
        cards : Annotated[List[Card], Body(embed = True)]
    ):
    total = sum(cards.card_count)
    return {"message": "successfully inserted {total} cards"}

@router.post("/move/{card_name}")
async def move_card(card_name:str):
    return {}

@router.post("/{card_name}")
async def update_card(card_name:str):
    return {}


@router.put("/updatebyID/{card_id}")
async def update_card_by_ID(card_id : int, new_values : Annotated[Card, Body()]):
    updated_fields : List[str] = []

    for key, value in new_values.dict.items():
        if mock_cards_data[card_id][key] != value:
            updated_fields.append(key)
            mock_cards_data[card_id][key] = value

    return {"updated" : updated_fields}