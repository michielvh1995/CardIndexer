from typing import List

from fastapi import APIRouter, HTTPException, Depends
from beanie.fields import PydanticObjectId

from .models import CardType

card_router = APIRouter()

@card_router.get("/cards/", response_model=List[CardType])
async def list_cocktails():
   return await CardType.find_all().to_list()