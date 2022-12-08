import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry


class PantryShelvesClass(ttk.Frame):
    def __init__(self, container, *args, **kwargs,):
        super().__init__(container, *args, **kwargs)

        self.done_load_DB()
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

# DOSTĘP DO BAZY DANYCH

    def done_load_DB(self):
        self.pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
        self.pantry_cursor = self.pantry_db.cursor()

        self.pantry_cursor.execute("select * from mypantry.products_items")
        self.all_db_pantry = self.pantry_cursor.fetchall()

# tworzony frame dla

    def main_construct_shelves(self):

        self.product = tk.Frame(self, background="#FFE918", padx=10, pady=10)
        self.product.grid(sticky="ew")

# tworzeny tytuł dla frame

    def title_contener_shelves(self):
        self.shelf = ttk.Label(self.product, text="Stan Spiżarni", style="titile_frame_os.TLabel")
        self.shelf.grid(column=0, columnspan=6, row=0, sticky="EW")

# scroll dla okna wyświatlania stanu spiżarni

    def scroll_list_shelves(self):
        pass

        # self.product_scroll = ttk.Scrollbar(self.product, orient="vertical")
        # self.product_scroll.grid(row=0, rowspan=10, column=10, sticky="ns")

# tworzone tytułu dla tabeli pokazującej stan spiżarni

    def name_column_shelves_list(self):

        self.first_kolumn = ttk.Label(self.product, text="Produktu", style="column_style_os.TLabel")
        self.first_kolumn.grid(column=0, row=1, sticky="EW")

        self.second_kolumn = ttk.Label(self.product, text="Stan", style="column_style_os.TLabel")
        self.second_kolumn.grid(column=1, row=1, sticky="EW")

        self.third_kolumn = ttk.Label(self.product, text="Jednostka", style="column_style_os.TLabel")
        self.third_kolumn.grid(column=2, row=1, sticky="EW")

        self.fourth_kolumn = ttk.Label(self.product, text="ile szt. do kuchni?", style="column_style_os.TLabel")
        self.fourth_kolumn.grid(column=3, row=1, sticky="EW")

# tworzenie kolenych wierszy dla tabeli stanu spiżarni

    # tworzenie wiersza z nazwą produktu
    def name_article_on_shelves(self):
        num1 = 2
        for x in self.all_db_pantry:
            self.article = ttk.Label(self.product, text=x[1], style="span_style_os.TLabel")
            self.article.grid(column=0, row=num1)
            num1 += 1

    # tworzenie wiersza z stanem ilosciowym produktu
    def quontity_arcicle_on_shelves(self):
        num3 = 2
        for x in self.all_db_pantry:
            self.article_status = ttk.Label(self.product, text=x[3], style="span_style_os.TLabel")
            self.article_status.grid(column=1, row=num3)
            num3 += 1

    # tworzenie wiersza z opisem jednostki miary
    def unit_measure_article_on_shelves(self):
        num5 = 2
        for x in self.all_db_pantry:
            self.article_unit_measure = ttk.Label(self.product, text=x[2], style="span_style_os.TLabel" )
            self.article_unit_measure.grid(column=2, row=num5, padx=5)
            num5 += 1

    # tworzenie wiersza z spinboxom dla wyboru ilości wyjmowanych z spizani produktow.
    def spin_qty_constract(self):

        # lista stanu spiżarni dla poszczególnych produktów
        self.list_product_inventory = [x[3] for x in self.all_db_pantry]

        # lista wartość do ściągnięcia z spin boxa
        self.new_quantity_article = [tk.IntVar(value=0) for wszy in len_all_pantry]

        # lista spinboxa w raz z tworzonym listami potrzebnych ilości do kuchni.
        self.spin_qty =[tk.Spinbox(
            self.product,
            buttondownrelief="flat",
            buttonuprelief="flat",
            from_=0,
            to=self.list_product_inventory[wszy],
            justify="center",
            font=("Courier New", 11, "bold"),
            foreground="#1E6ADE",
            background="#FFE918",
            relief="flat",
            buttonbackground="#FFE918",
            textvariable=self.new_quantity_article[wszy]) for wszy in len_all_pantry]

    #
    def list_of_items_and_measure_constract(self):
        self.name_all_measure = [ttk.Label(
            self.product,
            text=f'{namas}') for namas in name_all_pantry]

    #
    def list_for_ingradients(self):

        num4 = 2
        for x in range(len(self.spin_qty)):
            self.spin_qty[x].grid(column=3, row=num4)
            num4 += 1

    #
    def all_list_in_tab_product(self):
        print("Moduł all_list_in_tab_product został uruchomiony.\n ===== vvv =====")

        self.recipe_list = {}

        for index, x in enumerate(self.spin_qty):
            qty = x.get()
            if int(qty) >= 0:
                self.recipe_list[name_all_pantry[index]] = qty
                print(f"Zmieniona wartosć dla {name_all_pantry[index]} o wartość {qty}")

        else:

            print(f'\nSłownik self.recipe_list utworzony:  {self.recipe_list}')

            # aktualizacja bazy danych

            for signature, value in self.recipe_list.items():

                if value != "0":
                    print(f"Produkt {signature} zostaje zaktualizowany w bazie danych o {value} szt. ")

                    for x in self.all_db_pantry:
                        if x[1] == signature:
                            self.index_one = x[0]

                            self.state = x[3]
                            self.new_state = int(self.state) - int(value)

                    # aktualizacja bazy danych:

                    self.pantry_cursor.execute(
                        f"update products_items set quantity = {self.new_state} where id ={self.index_one}")
                    self.pantry_db.commit()

            self.pantry_db.close()
            self.products_transferred()

    def products_transferred(self):

        self.recipe_diner = tk.Frame(self, background="#FFFFFF", padx=10, pady=10)
        self.recipe_diner.grid(columnspan=2, row=1, sticky="EW")

        self.component = ttk.Label(self.recipe_diner, text="Produkty przeniesione \n z Spiżarni do Kuchni",
                                   style="titile_frame_handwritten.TLabel")
        self.component.grid(columnspan=2, row=0, sticky="EW")

        # Tytuł tabelek

        self.qty_label_title = ttk.Label(self.recipe_diner, text="Nazwa produktu",
                                         style="column_style_handwritten.TLabel")
        self.qty_label_title.grid(column=0, row=2, sticky="ew")

        self.qty_name_title = ttk.Label(self.recipe_diner, text="Ilość szt.", style="column_style_handwritten.TLabel")
        self.qty_name_title.grid(column=1, row=2, sticky="ew")

        num6 = 1
        for x, y in self.recipe_list.items():

            if y != "0":
                self.qty_name = ttk.Label(self.recipe_diner, text=f"{y} szt.", style="span_style_handwritten.TLabel")
                self.qty_name.grid(column=1, row=num6)

                self.qty_label = ttk.Label(self.recipe_diner, text=x, style="span_style_handwritten.TLabel")
                self.qty_label.grid(column=0, row=num6)

                print(f"Został utworzeny wiersz z {x} o wartości {y} i wyświetlony")

                num6 += 1

        else:
            num6 += 1

        self.product.destroy()
        self.done_load_DB()


        print("Moduł all_list_in_tab_product został zokończony. \n =============== ^^^^ =============")


# przycisk do potwierdzenia przesunięcia produktów z spiżarni do kochni

    def list_ingradients_approval_button(self):

        self.one_buttom = ttk.Button(self.product, text="spiżarnia ==> kuchnia", style="button_style_os.TButton", )
        self.one_buttom.grid(columnspan=4, row=50, sticky='ew')
        self.one_buttom.configure(command=self.all_list_in_tab_product,)

