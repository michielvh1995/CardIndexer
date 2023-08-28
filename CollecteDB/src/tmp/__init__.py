USING_MONGO = False

from fastapi import FastAPI, Query
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient


from .database import Database, MockEngine

from .settings import Settings
from .routers import cards, decks

from .routers.mockdatabase import mock_cards_data 


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

    Database.InitDatabase(MockEngine, cards = mock_cards_data)

    # Initialize beanie with the Product document class and a database
    if USING_MONGO:
        await init_beanie(database=client.cards, document_models=[Sample])
