from __future__ import annotations

from ..models import Card

class Database:
    Engine : DatabaseEngine = None

    @classmethod
    def InitDatabase(cls, engine, **kwargs):
        cls.Engine = engine
        return cls.Engine.InitDatabase(**kwargs)

    @classmethod    
    def InsertCards(cls, cards: list[Card]) -> list[Card]:
        return cls.Engine.InsertCards(cards)
    
    @classmethod
    def QueryCards(cls, filters : dict[str, any]):
        return cls.Engine.QueryCards(filters)

    @classmethod    
    def QueryByName(cls, name : str) -> list[Card]:
        return cls.Engine.QueryByName(name)
    
    @classmethod
    def GetAll(cls) -> list[Card]:
        return cls.Engine.GetAll()

    @classmethod
    def ExportData(cls):
        return cls.Engine.ExportData()


class DatabaseEngine:
    Data = None
    type = "base"

    @classmethod
    def InitDatabase(cls, **kwargs):
        return cls.InitDatabase(**kwargs)

    @classmethod    
    def InsertCards(cls, cards: list[Card]) -> list[Card]:
        return cls.InsertCards(cards)

    @classmethod
    def QueryCards(cls, filters : dict[str, any]):
        return cls.QueryCards(filters)

    @classmethod    
    def QueryByName(cls, name : str):
        return cls.QueryByName(name)

    @classmethod
    def GetAll(cls):
        return cls.GetAll()
    
    @classmethod
    def ExportData(cls):
        return cls.ExportData()