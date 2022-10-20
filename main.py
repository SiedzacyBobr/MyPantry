import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import IngradientsList, ShoppingList, PantryShelves
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#================================================ główne okno "Main window" ============================================


class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_container()
        self.stacking_conteiners()
        self.drukowanie()


    def main_container(self):

        self.title("Domowa Spiżarnia")
        font.nametofont("TkDefaultFont").config(size=12)

        self.body_pantry = ttk.Frame(self, borderwidth=1, relief='solid')
        self.body_pantry.pack(side="top", fill="both", expand=True)

        self.hello_usel = ttk.Label(self.body_pantry, text="Witaj użytkowniku, ten program pomoże ci \n zapanować nad twoją domową spiżarnią. :)", padding=(10,10))
        self.hello_usel.pack()

    def stacking_conteiners(self):

        area_Ingredient = IngradientsList.IngradientsListClass(self, padding=(10, 10), borderwidth=1, relief='solid')
        area_Ingredient.pack(side="right", fill="both", expand=True)

        area_shelves = PantryShelves.PantryShelvesClass(self, padding=(10,10), borderwidth=1, relief='solid')
        area_shelves.pack(side="top", fill="both", expand=True)

        area_shopping = ShoppingList.ShoppingList(self, padding=(10,10), borderwidth=1, relief='solid')
        area_shopping.pack(side="top", fill="both", expand=True)

    def drukowanie(self):
        print(f'Drukowanie to świetna zabawa,')

if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()

