from typing import List, Annotated
from fastapi import APIRouter, Body, Response, Request

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

    return {"Cards" : cards[0:20]}

# Returns all information regarding a card in the collection
@router.get("/{card_name}")
async def get_cards(card_name:str):
    return {"Cards": Database.QueryByName(card_name) }

@router.get("")
async def get_cards(
        request: Request
    ):

    print("params:")
    for p in request.query_params:
        print(p, request.query_params[p])

    filters = {}


    queried = Database.QueryCards(dict({p: request.query_params[p] for p in request.query_params}))
    
    # DEBUG:
    print(queried[:40])
    return { "Cards" : queried[:40] }


@router.post("/new/")
async def add_card(
        Cards : Annotated[List[Card], Body(embed = True)]
    ):
    print("post: new", Cards)

    return {"Cards": Database.InsertCards(cards=Cards)}

@router.options("/new/")
async def allow_localhost(response: Response):
    print("OPTIONS REQUEST")
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:4200'
    return {
        "Access-Control-Allow-Origin" : 'http://localhost:4200' ,
        "Access-Control-Allow-Methods" : 'POST, OPTIONS'
    }

@router.post("/move/{card_name}")
async def move_card(card_name:str):
    return {}

@router.post("/{card_name}")
async def update_card(card_name:str):
    return {}


