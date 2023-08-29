import json
from typing import List, Annotated
from fastapi import APIRouter, Body

from .mockdatabase import mock_cards_data

from ..database import Database

from ..models import Card



# ================================================================================
# ================================================================================
# ================================================================================

router = APIRouter(
    prefix="/cards",
    tags=["cards"],
    responses={404: {"Description": "Not found"}},
)

# DEBUG
@router.get("/storeCollection")
async def printDictionary():
    return {f"Stored the collection to file"}

# Cards API endpoints:

# Returns a list of how many of a specific card are in their locations
# i.e. {swamp: [{collection: 100}, {atraxa:5}] }
@router.get("/location/{card_name}")
async def get_card_locations(card_name:str):
    return { "name": card_name, "loc": [{"location": "name", "count": 0}]}

# Returns the collection
@router.get("/all")
async def get_all_cards():
    cardsData = Database.GetAll()
    cards = [cardsData[key] for key in cardsData.keys()]

    return {"Cards" : cards}

# Returns all information regarding a card in the collection
@router.get("/{card_name}")
async def get_cards(card_name:str):
    return {"Cards": Database.QueryByName(card_name) }

@router.get("")
async def get_cards(
        name : str | None = None,
        set : str | None = None,
        number: str | None = None,
        multiverseID : int | None = None,
        foil : bool = False
    ):

    # Filterfunction used to filter the mock database based on the query variables
    def filterFunc(card : Card):
        if name is not None and not card.name == name:
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

    return {"Cards": Database.InsertCards(cards=Cards)}

@router.post("/move/{card_name}")
async def move_card(card_name:str):
    return {}

@router.post("/{card_name}")
async def update_card(card_name:str):
    return {}