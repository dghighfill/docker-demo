from sqlalchemy.orm import Session
from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional

from models.coffee import Coffee as CoffeeModel
from models.coffee import CoffeeCreate as CoffeeCreateModel
from models.country import Country as CountryModel
from models.country import CountryCreate as CountryCreateModel
from schemas.coffee import Coffee as CoffeeSchema
from schemas.country import Country as CountrySchema
from typing import Dict


class DatabaseController:

    def get_coffees(self, db: Session):
        return db.query(CoffeeSchema).all()

    def get_coffee_by_name(self, name: str, db: Session):
        return db.query(CoffeeSchema).filter(CoffeeSchema.name == name).first()

    def get_coffee_by_id(self, item_id: int, db: Session):
        return db.query(CoffeeSchema).filter(CoffeeSchema.id == item_id).first()

    def create_coffee(self, coffee: CoffeeCreateModel, db: Session):
        response = None
        # Check to see if it already exists
        item = db.query(CoffeeSchema).filter(CoffeeSchema.name == coffee.name).first()

        if item is None:
            db_coffee = CoffeeSchema(name=coffee.name, roast=coffee.roast,
                                     country_id=coffee.country_id)
            db.add(db_coffee)
            db.commit()
            db.refresh(db_coffee)
            response = self.get_coffee_by_id(db_coffee.id, db=db)

        return response

    def update_coffee(self, coffee: CoffeeModel, db: Session):
        response = None
        db_coffee = db.query(CoffeeSchema).filter(CoffeeSchema.id == coffee.id).first()
        if db_coffee is not None:
            db_coffee.name = coffee.name
            db_coffee.roast = coffee.roast
            db_coffee.country_id = coffee.country_id
            db.commit()
            response = self.get_coffee_by_id(db_coffee.id, db=db)

        return response

    def delete_coffee(self, coffee_id: int, db: Session):
        coffee = db.query(CoffeeSchema).filter(CoffeeSchema.id == coffee_id).first()
        if coffee is not None:
            db.delete(coffee)
            db.commit()
        else:
            raise Exception( "Coffee does not exists to delete")
        return {}

    def get_countries(self, db: Session):
        return db.query(CountrySchema).all()

    def get_beans_for_country(self, country_id: int, db: Session):
        country = db.query(CountrySchema).filter(CountrySchema.id == country_id).first()
        return country.coffees

    def get_country_by_id(self, country_id: int, db: Session):
        return db.query(CountrySchema).filter(CountrySchema.id == country_id).first()

    def create_country(self, country: CountryCreateModel, db: Session):
        db_country = CountrySchema(name=country.name)
        db.add(db_country)
        db.commit()
        db.refresh(db_country)
        return self.get_country_by_id(db_country.id, db)

    def update_country(self, country: CountryModel, db: Session):
        response = None
        db_country = db.query(CountrySchema).filter(CountrySchema.id == country.id).first()
        if db_country is not None:
            db_country.name = country.name
            db.commit()
            response = self.get_country_by_id(db_country.id, db)

        return response

    def delete_country(self, country_id: int, db: Session):
        response = {}
        country = db.query(CountrySchema).filter(CountrySchema.id == country_id).first()
        if country is not None:
            db.delete(country)
            db.commit()
        else:
            response = None
        return response