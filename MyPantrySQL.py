import select

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path_to_host = "lokalhost_entry.txt"
path = open(path_to_host, "r")
dane = path.read(71)

db = create_engine(f'{dane}')
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()


class MyPantry(Base):
    __tablename__ = "products_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_product = Column(String(50), nullable=False)
    unit_of_measure = Column(String(10))
    quantity = Column(Integer)
    seftystock = Column(Integer, nullable=False)

    def __init__(self, id, name_product, unit_of_measure, quantity,seftystock):
        self.id = id
        self.name_product = name_product
        self.unit_of_measure = unit_of_measure
        self.quantity = quantity
        self.seftystock = seftystock

    def __repr__(self):
        return self.name_product


wynik = session.execute("select name_product from products_items WHERE id=2")
wynik_dvzialania = wynik.fetchall()
# wynik_dvzialania = wynik.fetchone()

print(wynik)
print(wynik_dvzialania)

for x in wynik_dvzialania:
    print(x)