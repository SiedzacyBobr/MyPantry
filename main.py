import tkinter as tk
import tkinter.font as font
import ShoppingList, PantryShelves, Addding_product, Delete_product, Editing_product
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from tkinter import ttk
from Style_constrakt import style_constrakt

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# startowanie classy
class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

# odpalanie funkcji
        self.manu_app()
        self.all_frames_create()
        self.hello_user = None
        self.body_pantry = None
        self.main_container()
        self.stacking_conteiners()

        style_constrakt()

# tworzenie widżetu menu o nazwie main_menu w głownym oknie aplikacji:
    def manu_app(self):

        self.main_menu = tk.Menu(self)

        # Tworzenie przycisków w  głównym menu:

        self.main_menu.add_command(label="Dodawanie", command=self.addding_conteiner)
        self.main_menu.add_command(label="Usuwanie", command=self.delete_conteiner)
        self.main_menu.add_command(label="Edytowanie", command=self.editing_conteiner)
        self.main_menu.add_command(label="Spiżarnia", command=self.stacking_conteiners)

        # dodawanie do głownego okna menu:

        self.config(menu=self.main_menu)

# tworzony gławne okno, kontener z wiadomością dla użytkownika
    def main_container(self):

        self.title("Domowa Spiżarnia")
        font.nametofont("TkDefaultFont").config(size=12)

        self.body_pantry = tk.Frame(self, background="White")
        self.body_pantry.grid(column=0, row=0)

        self.hello_user = ttk.Label(self.body_pantry,
                                    text="Witaj użytkowniku, ten program pomoże ci \n "
                                         "zapanować nad twoją domową spiżarnią. \n "
                                         "Sa dwie drogi: sklep ==> spiżarnia i spiżarnia ==> kuchnia \n Powodzenia :) \n"
                                         "2. uruchomić odświerzanie stanu aplicjajii by nie trzeba było wyłączać i uruchaiać na nawo \n"
                                         "3. ustawić tak dodatki z nemu by otwierały sie zamiast oktualnego fraima",
                                    style="Main_title_frame_os.TLabel"
                                    )
        self.hello_user.grid(column=0, row=0)

    def all_frames_create(self):
        self.main_start_conteiner = tk.Frame(self)
        self.addding_product_conteiner = tk.Frame(self)
        self.delete_product_conteiner = tk.Frame(self)
        self.editing_product_conteiner = tk.Frame(self)


# wstawiane kolejne kontenery
    def stacking_conteiners(self):

        self.czyszczenie_okna()

        self.main_start_conteiner.grid(column=0, row=1)

        area_shelves = PantryShelves.PantryShelvesClass(self.main_start_conteiner, padding=(10, 10))
        area_shelves.grid(column=0, row=1)

        area_shopping = ShoppingList.ShoppingList(self.main_start_conteiner, padding=(10, 10))
        area_shopping.grid(column=0, row=2)

    def addding_conteiner(self):
        self.czyszczenie_okna()

        self.addding_product_conteiner.grid(column=0, row=1)

        addding_action = Addding_product.Adding_action_product(self.addding_product_conteiner, padding=(10, 10))
        addding_action.grid(column=0, row=0)

    def delete_conteiner(self):

        self.czyszczenie_okna()

        self.delete_product_conteiner.grid(column=0, row=1)

        delete_action = Delete_product.Delete_action_product(self.delete_product_conteiner, padding=(10, 10))
        delete_action.grid(column=0, row=0)

    def editing_conteiner(self):

        self.czyszczenie_okna()

        self.editing_product_conteiner.grid(column=0, row=1)

        editing_action = Editing_product.Editing_action_product(self.editing_product_conteiner, padding=(10, 10))
        editing_action.grid(column=0, row=0)

    def czyszczenie_okna(self):
        self.main_start_conteiner.grid_forget()
        self.addding_product_conteiner.grid_forget()
        self.delete_product_conteiner.grid_forget()
        self.editing_product_conteiner.grid_forget()


if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()