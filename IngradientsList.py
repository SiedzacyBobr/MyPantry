from tkinter import ttk, N, S, NS, E, W, CENTER
import tkinter as tk
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from PantryShelves import recipe_list
from LenList import len_all_pantry, name_all_pantry


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

        self.component = ttk.Label(self.recipe_diner, text="Lista produktów wyjętych z spiżarni", style="titile_frame_handwritten.TLabel")
        self.component.grid(columnspan=2, row=1, sticky="EW")


    def all_list_out(self):

        #Tytuł tabelki

        qty_label_title = ttk.Label(self.recipe_diner, text="nazwa produktu", style="column_style_handwritten.TLabel")
        qty_label_title.grid(column=0, row=3, sticky="ew")

        qty_name_title = ttk.Label(self.recipe_diner, text="ilość szt.", style="column_style_handwritten.TLabel")
        qty_name_title.grid(column=1, row=3, sticky="ew")


#Pętla przeszukiwania danych.
        num6 = 4
        for x, y in recipe_list.items():

            if y != "0":
                qty_name = ttk.Label(self.recipe_diner, text=f"{y} szt.", style="span_style_handwritten.TLabel")
                qty_name.grid(column=1, row=num6)

                qty_label = ttk.Label(self.recipe_diner, text=x, style="span_style_handwritten.TLabel")
                qty_label.grid(column=0, row=num6)

            num6 +=1
        else:
            print(f"działa funkcja all_list_out {recipe_list}")
            num6 +=1

            self.buttom_update = ttk.Button(self.recipe_diner, text="odświerz bazę danych")
            self.buttom_update.grid(columnspan=3, row=num6, sticky='ew')
            self.buttom_update.configure(command=self.db_pantry_update)

    def db_pantry_update(self):
        print("up date DB")
        print(len_all_pantry)
        print(name_all_pantry)
        print(recipe_list)

        self.index_one = 0
        for signature, value in recipe_list.items():


            if value != "0":
                print(f"produkt {signature} o indeksie {self.index_one} zostaje zmieniony o {value} szt. ")

                self.state = all_db_pantry[self.index_one][3]
                print(self.state)
                self.new_state = int(self.state) - int(value)
                print(self.new_state)
                pantry_cursor.execute(f"update products_items set quantity = {self.new_state} where id ={self.index_one + 1}")
                pantry_db.commit()

                self.index_one += 1

            else:
                self.index_one += 1

#przycisk do zaciągania listy produktów na przepis

    def list_approval_button(self):

        self.buttom_ingra = ttk.Button(self.recipe_diner, text="zaciąganie listy")
        self.buttom_ingra.grid(columnspan=3, row=2, sticky='ew')
        self.buttom_ingra.configure(command=self.all_list_out)
