# Models for the places microservice

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from models.db import PyObjectId

class Place(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "ML515"
            }
        }
    )
    
class PlaceCollection(BaseModel):
    # A collection of places
    places: List[Place] = Field(...)