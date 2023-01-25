import mysql.connector
from lokalhost_entry import passwd, user_pantry


class Products():
    def __init__(self, name, unit, quantity, safestock, kategory ):
        self.name_product = name
        self.unit_of_measure = unit
        self.quantity = quantity
        self.safestock = safestock
        self.category = kategory

    def database_connection(self):

        self.pantry_db = mysql.connector.connect(
            host="localhost",
            user=user_pantry,
            passwd=passwd,
            database="mypantry",
        )

        self.pantry_cursor = self.pantry_db.cursor()

    def adding_to_the_pantry(self):

        self.pantry_cursor.execute(
            f"INSERT INTO mypantry.kategorie (kategoria) "
            f"select * from (select '{self.category}' as kategoria) as new_value "
            f"where not exists (select kategoria from mypantry.kategorie where kategoria = '{self.category}') limit 1"
        )
        self.pantry_db.commit()

        self.pantry_cursor.execute(
            f"INSERT INTO mypantry.products_items"
            f" (name_product, unit_of_measure, quantity, seftystock, id_kategorie)"
            f" VALUES ( '{self.name_product}','{self.unit_of_measure}', {self.quantity} , {self.safestock},"
            f" (select id from mypantry.kategorie where kategoria = '{self.category}'))"
        )
        self.pantry_db.commit()

        return "Product dodany do bazy danych"

    # utworzyć obiekt products

    # pomlać dane do utworzenia nowej pozycji (obiektu)

    # zwraca informacje

    def deletion_from_the_pantry(self):
        pass
    def editing_in_the_pantry(self):
        pass
    def pantry_status_display(self):
        pass
    def displaying_the_shopping_list(self):
        pass
    def adding_purchased_products_to_the_pantry(self):
        pass
    def moving_products_from_the_pantry_to_the_kitchen(self):
        pass

class CategoryProduct():
    def __init__(self, name):
        self.name_category = name

