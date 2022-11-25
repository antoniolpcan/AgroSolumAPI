from pydantic import BaseModel

class GroundInfo(BaseModel):
    color: str
    texture: str
    humidity: int
    city: str
