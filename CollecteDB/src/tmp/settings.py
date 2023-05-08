from pydantic import BaseSettings

class Settings(BaseSettings):
    mongodb_url = "mongodb://localhost:27017/"
    db_name = "cards"