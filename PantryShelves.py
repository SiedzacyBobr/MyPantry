import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry


pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

lista_do_przepisu = {}

class PantryShelvesClass(ttk.Frame):
    def __init__(self, container, *args, **kwargs,):
        super().__init__(container, *args, **kwargs)

        self.main_construct_shelves()
        self.title_contener_shelves()
        self.scroll_list_shelves()
        self.name_column_shelves_list()
        self.name_article_on_shelves()
        self.quontity_arcicle_on_shelves()
        self.unit_measure_article_on_shelves()
        self.spin_qty_constract()
        self.list_of_items_and_measure_constract()
        self.list_for_ingradients()
        self.list_ingradients_approval_button()


    def main_construct_shelves(self):

        self.product = ttk.Frame(self)
        self.product.grid(sticky="ew")

    def title_contener_shelves(self):
        self.shelf = ttk.Label(self.product, text="Testowanie położenia kontenera z zawartością \n półek spiżarni", background="Yellow", borderwidth=1, relief='solid')
        self.shelf.grid(column=0, columnspan=6, row=0, sticky="EW")

    def scroll_list_shelves(self):

        self.product_scroll = ttk.Scrollbar(self.product, orient="vertical")
        self.product_scroll.grid(row=0, rowspan=10, column=10, sticky="ns")

    def name_column_shelves_list(self):

        self.first_kolumn = ttk.Label(self.product, text="Nazwa produktu", background="orange", borderwidth=1, relief='solid')
        self.first_kolumn.grid(column=0, row=1, sticky="EW")

        self.second_kolumn = ttk.Label(self.product, text="Stan", background="orange", borderwidth=1, relief='solid')
        self.second_kolumn.grid(column=1, row=1, sticky="EW")

        self.third_kolumn = ttk.Label(self.product, text="Jednostka", background="orange", borderwidth=1, relief='solid')
        self.third_kolumn.grid(column=2, row=1, sticky="EW")

        self.fourth_kolumn = ttk.Label(self.product, text="do poprania", background="orange", borderwidth=1, relief='solid')
        self.fourth_kolumn.grid(column=3, row=1, sticky="EW")

    def name_article_on_shelves(self):
        num1 = 2
        for x in all_db_pantry:
            self.article = ttk.Label(self.product, text=x[1])
            self.article.grid(column=0, row=num1)
            num1 += 1

    def quontity_arcicle_on_shelves(self):
        num3 = 2
        for x in all_db_pantry:
            self.article_status = ttk.Label(self.product, text=x[3],)
            self.article_status.grid(column=1, row=num3)
            num3 += 1

    def unit_measure_article_on_shelves(self):
        num5 = 2
        for x in all_db_pantry:
            self.article_unit_measure = ttk.Label(self.product, text=x[2], )
            self.article_unit_measure.grid(column=2, row=num5, padx=5)
            num5 += 1

    def spin_qty_constract(self):
        self.new_quantity_article = [tk.IntVar(value=0) for wszy in len_all_pantry]
        self.spin_qty =[tk.Spinbox(self.product, from_=0, to=30, textvariable=self.new_quantity_article[wszy]) for wszy in len_all_pantry]

    def list_of_items_and_measure_constract(self):
        self.name_wszystko_measure = [ttk.Label(self.product, text=f'{namas}') for namas in name_all_pantry]

    def list_for_ingradients(self):  # stworzenie elementow do wyświetlenia na eklanie gdzie każdy elemnet jest indexowany.

        num4 = 2
        for x in range(len(self.spin_qty)):
            self.spin_qty[x].grid(column=3, row=num4)
            num4 += 1

    def all_list_in_tab_product(self):
        print("Działa inicjalizacjka funkcja all_list_in_tab_product - jeśli warunk jest spełniony wyświetli się lista")


        #num6 = 16
        for index, x in enumerate(self.spin_qty):
            quty = x.get()
            if int(quty) >= 0:
                lista_do_przepisu[name_all_pantry[index]] = quty
                print(f"zmieniona wartosć dla {name_all_pantry[index]} o wartość {quty}")

        else:
            print("Działa cała funkcja all_list_in i nastąpiło podsumowanie")
            potwierdzenie = ttk.Label(self.product, text=f'Lista została utworzona')
            potwierdzenie.grid(columnspan=4,row=51, sticky="ew")

            print(lista_do_przepisu)
            return lista_do_przepisu

    def sprawdzenie_listy(self):
        print("funkcja działa")
        print(f'W słowniku jest {lista_do_przepisu}')

    def list_ingradients_approval_button(self):

        self.one_buttom = ttk.Button(self.product, text="utwórz liste")
        self.one_buttom.grid(columnspan=4, row=50, sticky='ew')
        self.one_buttom.configure(command=self.all_list_in_tab_product)



