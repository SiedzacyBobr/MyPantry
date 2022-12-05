import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
import IngradientsList
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry
import json

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

class PantryShelvesClass(ttk.Frame):
    def __init__(self, container, *args, **kwargs,):
        super().__init__(container, *args, **kwargs)

        self.test_funkcji = IngradientsList.IngradientsListClass(container)

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

        self.product = tk.Frame(self, background="#FFE918", borderwidth=1, relief='solid', padx=10, pady=10)
        self.product.grid(sticky="ew")

    def title_contener_shelves(self):
        self.shelf = ttk.Label(self.product, text="Stan Spiżarni", style="titile_frame_os.TLabel")
        self.shelf.grid(column=0, columnspan=6, row=0, sticky="EW")

    def scroll_list_shelves(self):
        pass

        # self.product_scroll = ttk.Scrollbar(self.product, orient="vertical")
        # self.product_scroll.grid(row=0, rowspan=10, column=10, sticky="ns")

    def name_column_shelves_list(self):

        self.first_kolumn = ttk.Label(self.product, text="Produktu", style="column_style_os.TLabel")
        self.first_kolumn.grid(column=0, row=1, sticky="EW")

        self.second_kolumn = ttk.Label(self.product, text="Stan", style="column_style_os.TLabel")
        self.second_kolumn.grid(column=1, row=1, sticky="EW")

        self.third_kolumn = ttk.Label(self.product, text="Jednostka", style="column_style_os.TLabel")
        self.third_kolumn.grid(column=2, row=1, sticky="EW")

        self.fourth_kolumn = ttk.Label(self.product, text="ile szt. do kuchni?", style="column_style_os.TLabel")
        self.fourth_kolumn.grid(column=3, row=1, sticky="EW")

    def name_article_on_shelves(self):
        num1 = 2
        for x in all_db_pantry:
            self.article = ttk.Label(self.product, text=x[1], style="span_style_os.TLabel")
            self.article.grid(column=0, row=num1)
            num1 += 1

    def quontity_arcicle_on_shelves(self):
        num3 = 2
        for x in all_db_pantry:
            self.article_status = ttk.Label(self.product, text=x[3], style="span_style_os.TLabel")
            self.article_status.grid(column=1, row=num3)
            num3 += 1

    def unit_measure_article_on_shelves(self):
        num5 = 2
        for x in all_db_pantry:
            self.article_unit_measure = ttk.Label(self.product, text=x[2], style="span_style_os.TLabel" )
            self.article_unit_measure.grid(column=2, row=num5, padx=5)
            num5 += 1

    def spin_qty_constract(self):

        self.zmiena_testowa = [x[3] for x in all_db_pantry]
        self.new_quantity_article = [tk.IntVar(value=0) for wszy in len_all_pantry]
        self.spin_qty =[tk.Spinbox(
            self.product,
            from_=0,
            to=self.zmiena_testowa[wszy],
            justify="center",
            font=("Courier New", 11, "bold"),
            foreground="#1E6ADE",
            background="#FFE918",
            relief="flat",
            textvariable=self.new_quantity_article[wszy]) for wszy in len_all_pantry]

    def list_of_items_and_measure_constract(self):
        self.name_all_measure = [ttk.Label(
            self.product,
            text=f'{namas}') for namas in name_all_pantry]

    def list_for_ingradients(self):

        num4 = 2
        for x in range(len(self.spin_qty)):
            self.spin_qty[x].grid(column=3, row=num4)
            num4 += 1

    def all_list_in_tab_product(self):
        print("Moduł all_list_in_tab_product został uruchomiony.\n ===== vvv =====")

        self.recipe_list = {}

        for index, x in enumerate(self.spin_qty):
            qty = x.get()
            if int(qty) >= 0:
                self.recipe_list[name_all_pantry[index]] = qty
                print(f"Zmieniona wartosć dla {name_all_pantry[index]} o wartość {qty}")

        else:
            confirmation = ttk.Label(self.product, text=f'Wybrane produkuty przeniesione do Kuchni ===>> ', style="span_style_os.TLabel")
            confirmation.grid(columnspan=4,row=51, sticky="ew")
            print(f'\nSłownik self.recipe_list utworzony:  {self.recipe_list}')

# utworzony słownik self.recipe_list i zapisany w pliku json.

            with open("list_from_pantry_shelves.json", "w") as list_from_pantry_shelves:
                json_dict = json.dumps(self.recipe_list, indent=4)
                list_from_pantry_shelves.write(json_dict)
                print("\nZapisany słownik self.recipe_list w pliku json")

        print("Moduł all_list_in_tab_product został zokończony. \n =============== ^^^^ =============")

    def list_ingradients_approval_button(self):

        self.one_buttom = ttk.Button(self.product, text="Zabrałem do Kuchni", style="button_style_os.TButton")
        self.one_buttom.grid(columnspan=4, row=50, sticky='ew')
        self.one_buttom.configure(command=self.all_list_in_tab_product,)
        #self.one_buttom.configure(command=lambda: self.test_funkcji.all_list_out)