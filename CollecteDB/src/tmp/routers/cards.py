from typing import List, Annotated
from fastapi import APIRouter, Body

from ..models import Card

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

# Returns how many of a specific card are in the collection
@router.get("/count/{card_name}")
async def get_card_count(card_name:str):
    return { "name": card_name, "count": 0}

# Returns a list of all the card names in the collection
@router.get("/all")
async def get_all_cards(card_name:str):
    return { }

# Returns all information regarding a card in the collection
@router.get("/{card_name}")
async def get_cards(card_name:str):
    return { }

@router.post("/new/")
async def add_card(
        cards : Annotated[List[Card], Body(embed = True)]
    ):
    total = sum(cards.card_count)
    return {"message": "successfully inserted {total} cards"}

@router.put("/move/{card_name}")
async def move_card(card_name:str):
    return {}

@router.put("/{card_name}")
async def update_card(card_name:str):
    return {}
