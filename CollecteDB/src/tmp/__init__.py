USING_MONGO = False

from typing import Annotated
from fastapi import FastAPI, Query
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from .settings import Settings
from .routers import cards
from .models import Card


app = FastAPI()
app.include_router(cards.router)

class Sample(Document):
    name: str

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Buzzz"}, {"item_name": "Lightyear"}]


# ================================================================================
# ==================================== BEANIE ====================================
# ================================================================================
@app.on_event("startup")
async def init():
    # Create Motor client
    client = AsyncIOMotorClient(
        Settings().mongodb_url
    )

    # Initialize beanie with the Product document class and a database
    if USING_MONGO:
        await init_beanie(database=client.cards, document_models=[Sample])


@app.get("/card") 
async def card(skip : int = 0, limit : int = 100, optionalParam : Annotated[str |None, Query(max_length = 50, regex = ".*")] = None ):
    res = {"cards": fake_items_db[skip : skip + limit]}
    res.update({"message": "Got all the cards!"})
    return res



@app.get("/card/{cardName}") 
async def card(cardName : str):
    example = Sample(name = cardName)
    if USING_MONGO:
        await example.insert()
    
    return {"message": "Retrieved sample from the database", "Name": cardName }


@app.post("/card/") 
async def card(card : Card):
    card.name.title()

    if USING_MONGO:
        await card.insert()
    
    return card

# Insertion:
async def InsertExample():
    # for inserting a single document
    example = Sample(name = "test")
    if USING_MONGO:
        await example.insert()

    # For inserting multiple
    await Sample.insert_many([example])