from typing import List, Annotated
from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/decks",
    tags=["decks"],
    responses={404: {"Description": "Not found"}},
)
# Decks API endpoints:

# Returns all information regarding the cards in the collection
@router.get("/decks/all")
async def get_all_decks(card_name:str):
    return { }

# Returns the information of a deck plus what cards are in it
@router.get("/decks/{deck_name}")
async def get_deck(deck_name:str):
    return { }

# Create a new deck
@router.post("decks/new/")
async def create_deck():
    return {}

# Update a deck. This can be done either by removing or adding cards or deactivating the deck
@router.put("decks/update/{deck_name}")
async def update_deck(deck_name:str):
    return {}
