USING_MONGO = False

from contextlib import asynccontextmanager
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from .database import Database, MockEngine

from .settings import Settings
from .routers import cards, decks

def LoadDataFromJSON():
    cardData = {}
    with open('./src/tmp/cardsdata.json', 'r') as fil:
        cardData = json.load(fil)
    
    return cardData

@asynccontextmanager
async def lifespan(app: FastAPI):

    # MockDb uses a JSON file to load the data.
    # The mongo/motor/beanie database will use the database file with its own settings
    mockCards = LoadDataFromJSON()
    Database.InitDatabase(MockEngine, cards = mockCards)

    yield

    Database.ExportData()

app = FastAPI(lifespan=lifespan)
app.include_router(cards.router)

# I hope this works 
origins = [
    "http://localhost:4200",
    "http://localhost"
    ]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# app = FastAPI()
# app.include_router(cards.router)

# class Sample(Document):
#     name: str

# # ================================================================================
# # ==================================== BEANIE ====================================
# # ================================================================================



# @app.on_event("startup")
# async def init():
#     # Create Motor client
#     client = AsyncIOMotorClient(
#         Settings().mongodb_url
#     )

#     mock_cards = {}
#     with open('./src/tmp/cardsdata.json', 'r') as fil:
#         mock_cards = json.load(fil)


#     Database.InitDatabase(MockEngine, cards = mock_cards)

#     # Initialize beanie with the Product document class and a database
#     if USING_MONGO:
#         await init_beanie(database=client.cards, document_models=[Sample])

