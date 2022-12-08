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

class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.manu_app()
        self.hello_user = None
        self.body_pantry = None
        self.main_container()
        self.stacking_conteiners()
        style_constrakt()


    def manu_app(self):

# tworzenie widżetu menu o nazwie main_menu w głownym oknie aplikacji:

        self.main_menu = tk.Menu(self)

# Tworzenie przycisków w  głównym menu:

        self.main_menu.add_command(label="Dodawanie", command=self.addding_conteiner)
        self.main_menu.add_command(label="Usuwanie", command=self.delete_conteiner)
        self.main_menu.add_command(label="Edytowanie", command=self.editing_conteiner)

# dodawanie do głownego okna menu:

        self.config(menu=self.main_menu)

# tworzony gławne okno, kontener z wiadomością dla użytkownika

    def main_container(self):

        self.title("Domowa Spiżarnia")
        font.nametofont("TkDefaultFont").config(size=12)

        self.body_pantry = tk.Frame(self, borderwidth=2, relief='solid',background="White" )
        self.body_pantry.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.hello_user = ttk.Label(self.body_pantry,
                                    text="Witaj użytkowniku, ten program pomoże ci \n "
                                         "zapanować nad twoją domową spiżarnią. \n "
                                         "Sa dwie drogi: sklep ==> spiżarnia i spiżarnia ==> kuchnia \n Powodzenia :) \n"
                                         "2. uruchomić odświerzanie stanu aplicjajii by nie trzeba było wyłączać i uruchaiać na nawo \n"
                                         "3. ustawić tak dodatki z nemu by otwierały sie zamiast oktualnego fraima",
                                    style="Main_title_frame_os.TLabel"
                                    )
        self.hello_user.pack()
    # wstawiane kolejne kontenery

    def stacking_conteiners(self):

        self.main_start_conteiner = tk.Frame(self)
        self.main_start_conteiner.pack()

        area_shelves = PantryShelves.PantryShelvesClass(self.main_start_conteiner, padding=(10, 10), borderwidth=1, relief='solid')
        area_shelves.pack(side="top", fill="both", expand=True)

        area_shopping = ShoppingList.ShoppingList(self.main_start_conteiner, padding=(10, 10), borderwidth=1, relief='solid')
        area_shopping.pack(side="top", fill="both", expand=True)

    def addding_conteiner(self):

        addding_action = Addding_product.Adding_action_product(self, padding=(10, 10), borderwidth=1, relief='solid')
        addding_action.pack(side="top", fill="both", expand=True)

    def delete_conteiner(self):

        delete_action = Delete_product.Delete_action_product(self, padding=(10, 10), borderwidth=1, relief='solid')
        delete_action.pack(side="top", fill="both", expand=True)

    def editing_conteiner(self):
        editing_action = Editing_product.Editing_action_product(self, padding=(10, 10), borderwidth=1,
                                                                   relief='solid')
        editing_action.pack(side="top", fill="both", expand=True)


if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()