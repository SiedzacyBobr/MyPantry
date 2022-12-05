import json
from tkinter import ttk, N, S, NS, E, W, CENTER
import tkinter as tk
import mysql.connector
from lokalhost_entry import passwd, user_pantry
import time
from time import strftime


pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

class IngradientsListClass(ttk.Frame):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.main_concruct_diner()
        self.title_contener_diner_list()
        self.list_approval_button()

    def main_concruct_diner(self):

        self.recipe_diner = tk.Frame(self, background="#FFFFFF", borderwidth=1, relief='solid', padx=10, pady=10)
        self.recipe_diner.grid(columnspan=2, row=0, sticky="EW")

    def title_contener_diner_list(self):

        self.component = ttk.Label(self.recipe_diner, text="Lista produktów przeniesionych \n z Spiżarni do Kuchni", style="titile_frame_handwritten.TLabel")
        self.component.grid(columnspan=2, row=0, sticky="EW")

    def all_list_out(self):
        print("Moduł all_list_out został uruchomiony.\n ===== vvv =====")


        #Tytuł tabelek

        self.qty_label_title = ttk.Label(self.recipe_diner, text="nazwa produktu", style="column_style_handwritten.TLabel")
        self.qty_label_title.grid(column=0, row=2, sticky="ew")

        self.qty_name_title = ttk.Label(self.recipe_diner, text="ilość szt.", style="column_style_handwritten.TLabel")
        self.qty_name_title.grid(column=1, row=2, sticky="ew")

# zaciągnięty słownik z pliku json

        with open("list_from_pantry_shelves.json", "r") as list_from_pantry_shelves:
             self.list_from_shelves = json.loads(list_from_pantry_shelves.read())
             print(f"lista drukowana z jsona : {self.list_from_shelves}")

        #Pętla przeszukiwania danych.
        num6 = 3
        for x, y in self.list_from_shelves.items():

            if y != "0":
                self.qty_name = ttk.Label(self.recipe_diner, text=f"{y} szt.", style="span_style_handwritten.TLabel")
                self.qty_name.grid(column=1, row=num6)

                self.qty_label = ttk.Label(self.recipe_diner, text=x, style="span_style_handwritten.TLabel")
                self.qty_label.grid(column=0, row=num6)

                print(f"Został utworzeny wiersz z {x} o wartości {y} i wyświetlony")

                num6 +=1

        else:
            num6 +=1

            self.buttom_update = ttk.Button(self.recipe_diner, text="odświerz bazę danych")
            self.buttom_update.grid(columnspan=3, row=num6, sticky='ew')
            self.buttom_update.configure(command=self.db_pantry_update)

        print("Moduł all_list_out został zakończony.\n ===== ^^^ =====")

    def db_pantry_update(self):
        print("Moduł db_pantry_pudate został uruchomiony.\n ===== vvv =====")


        print(f"Lista z pliku.json została zaciągnięta do modułu")

        self.index_one = 0
        for signature, value in self.list_from_shelves.items():


            if value != "0":
                print(f"Produkt {signature} zostaje zaktualizowany w bazie danych o {value} szt. ")

                self.state = all_db_pantry[self.index_one][3]
                self.new_state = int(self.state) - int(value)

                pantry_cursor.execute(f"update products_items set quantity = {self.new_state} where id ={self.index_one + 1}")
                pantry_db.commit()

                self.index_one += 1

            else:
                self.index_one += 1
        print(f"Zakończone oktualizowanie bazy danych.")
        self.buttom_ingra.destroy()

        print("Moduł db_pantry_pudate został zakończony.\n ===== ^^^ =====")

#przycisk do zaciągania listy produktów na przepis

    def list_approval_button(self):

        self.buttom_ingra = ttk.Button(self.recipe_diner, text="zaciąganie listy")
        self.buttom_ingra.grid(columnspan=3, row=1, sticky='ew')
        self.buttom_ingra.configure(command=self.all_list_out)


