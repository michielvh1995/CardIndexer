USING_MONGO = False

from typing import Annotated
from fastapi import FastAPI, Query
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from .settings import Settings
from .routers import cards, decks
from .models import Card


app = FastAPI()
app.include_router(cards.router)

class Sample(Document):
    name: str

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

# @app.get("/card/{cardName}") 
# async def card(cardName : str):
#     example = Sample(name = cardName)
#     if USING_MONGO:
#         await example.insert()
    
#     return {"message": "Retrieved sample from the database", "Name": cardName }


# @app.post("/card/") 
# async def card(card : Card):
#     card.name.title()

#     if USING_MONGO:
#         await card.insert()
    
#     return card