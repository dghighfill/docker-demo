from fastapi import FastAPI, Path, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Optional

from models.coffee import Coffee as CoffeeModel
from models.coffee import CoffeeCreate as CoffeeCreateModel

from models.country import Country as CountryModel
from models.country import CountryCreate as CountryCreateModel

from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from controller.database_controller import DatabaseController
from typing import Dict


app = FastAPI()
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

controller = DatabaseController()

Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/coffees")
def get_coffees(db: Session = Depends(get_db)):
    return controller.get_coffees(db)


@app.get("/coffees/coffee")
def get_coffee_by_name(name: Optional[str] = None, db: Session = Depends(get_db)):
    # /coffees/coffee?name=sumatra
    coffee = controller.get_coffee_by_name(name, db)
    if coffee is not None:
        return coffee
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")


@app.get("/coffees/{item_id}")
def get_coffee_by_id(item_id: int = Path(description="The ID of the coffee you'd like to retrieve", gt=0)
                     , db: Session = Depends(get_db)):
    coffee = controller.get_coffee_by_id(item_id, db)
    if coffee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")

    return coffee


@app.post("/coffees/coffee")
def create_coffee(coffee: CoffeeCreateModel, db: Session = Depends(get_db)):
    coffee = controller.create_coffee(coffee, db)

    if coffee is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Coffee already exists")

    return coffee


@app.put("/coffees/coffee")
def update_coffee(coffee: CoffeeModel, db: Session = Depends(get_db)):
    coffee = controller.update_coffee(coffee, db)

    if coffee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")
    return coffee


@app.delete("/coffees/{item_id}")
def delete_coffee(coffee_id: int, db: Session = Depends(get_db)):
    try:
        controller.delete_coffee(coffee_id, db)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee does not exists")

    return {}


@app.get("/countries")
def get_countries(db: Session = Depends(get_db)):
    return controller.get_countries(db)


@app.get("/countries/{country_id}/coffees")
def get_coffees_for_country(country_id: int, db: Session = Depends(get_db)):
    country = controller.get_country_by_id(country_id, db)
    return country.coffees


@app.get("/countries/{country_id}")
def get_country_by_id(country_id: int = Path(description="The ID of the Country you'd like to retrieve", gt=0)
                      , db: Session = Depends(get_db)):
    country = controller.get_country_by_id(country_id, db)

    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country does not exists")
    return country

@app.post("/countries/country")
def create_country(country: CountryCreateModel, db: Session = Depends(get_db)):
    country = controller.create_country(country, db)

    if country is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Country already exists")

    return country


@app.put("/countries/country")
def update_country(country: CountryModel, db: Session = Depends(get_db)):
    country = controller.update_country(country, db)

    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country does not exists")
    return country


@app.delete("/countries/{country_id}")
def delete_country(country_id: int = Path(description="The ID of the Country you'd like to delete", gt=0)
                   , db: Session = Depends(get_db)):
    country = controller.delete_country(country_id, db)
    if country is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country does not exists")
    return country


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)