from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/card/{cardName}")
async def card(cardName:str):
    return {"message": "Searched for a card", "card": cardName }


# Cards API endpoints:

# Returns a list of how many of a specific card are in their locations
# i.e. {swamp: [{collection: 100}, {atraxa:5}] }
@app.get("/cards/location/{card_name}")
async def get_card_locations(card_name:str):
    return { "name": card_name, "loc": [{"location": "name", "count": 0}]}

# Returns how many of a specific card are in the collection
@app.get("/cards/count/{card_name}")
async def get_card_count(card_name:str):
    return { "name": card_name, "count": 0}

# Returns a list of all the card names in the collection
@app.get("/cards/all")
async def get_all_cards(card_name:str):
    return { }

# Returns all information regarding a card in the collection
@app.get("/cards/{card_name}")
async def get_cards(card_name:str):
    return { }

@app.post("/cards/new/{card_name}")
async def add_card(card_name:str):
    return {}

@app.put("/cards/move/{card_name}")
async def move_card(card_name:str):
    return {}

@app.put("/cards/{card_name}")
async def update_card(card_name:str):
    return {}



# Decks API endpoints:

# Returns all information regarding the cards in the collection
@app.get("/decks/all")
async def get_all_decks(card_name:str):
    return { }

# Returns the information of a deck plus what cards are in it
@app.get("/decks/{deck_name}")
async def get_deck(deck_name:str):
    return { }

# Create a new deck
@app.post("decks/new/")
async def create_deck():
    return {}

# Update a deck. This can be done either by removing or adding cards or deactivating the deck
@app.put("decks/update/{deck_name}")
async def update_deck(deck_name:str):
    return {}
