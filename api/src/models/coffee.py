from pydantic import BaseModel


class CoffeeCreate(BaseModel):
    name: str
    roast: str = None  # light, medium, dark
    country_id: int


class Coffee(CoffeeCreate):
    id: int

    class Config:
        from_attributes = True