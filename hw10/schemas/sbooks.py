from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date

class SbookResponseSchema(BaseModel):
    bookid: int
    carname: str = Field(max_length=50) 
    cityfr: str = Field(max_length=50)  
    airpfr: str = Field(max_length=50)  
    cityto: str = Field(max_length=50)
    airpto: str = Field(max_length=50)
    fldate: date
    fltime: float = None 
    price: float = None 
    currency: Optional[str] = None

class CreateSbookSchema(BaseModel):
    userid: int
    carrid: int
    connid: int
    fldate: date
    sflight_seats: int

class CreateSbookResponse(BaseModel):
    success: bool
    message: str