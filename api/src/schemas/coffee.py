from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Coffee(Base):
    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    roast = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="coffees")