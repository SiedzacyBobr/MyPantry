import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry
from Style_constrakt import colour_label_span, colour_char_hand, colour_paper_hand

class PantryShelvesClass(ttk.Frame):
    def __init__(self, container, *args, **kwargs,):
        super().__init__(container, *args, **kwargs)

        self.list_of_transferred_products = {}
        self.recipe_list = {}
        self.products_taken_to_the_kitchen = {}

        self.done_load_db()
        self.main_frame_shelves()
        self.main_frame_title_shelves()
        self.shelf_column_name()
        self.interactive_shelves_in_the_pantry()
        self.list_ingradients_approval_button()

# dostęp do bazy danych i tworzenie all_db_pantry
    def done_load_db(self):

        self.pantry_db = mysql.connector.connect(
            host="localhost",
            user=user_pantry,
            passwd=passwd,
            database="mypantry"
        )
        self.pantry_cursor = self.pantry_db.cursor()

        self.pantry_cursor.execute("select * from mypantry.products_items")
        self.all_db_pantry = self.pantry_cursor.fetchall()

        print(f'lista all_db_pantry jest świągnięta i wstawiona w PantryShelves')

# tworzony frame dla productów, głównego okna spiżarni

    def main_frame_shelves(self):

        self.product = tk.Frame(
            self,
            background=colour_label_span,
            borderwidth=1,
            relief="solid",
            padx=10,
            pady=10,
        )
        self.product.grid(column=0, row=0)

# tworzeny tytuł dla frame

    def main_frame_title_shelves(self):

        self.shelf = ttk.Label(
            self.product,
            text="Stan Spiżarni",
            style="titile_frame_os.TLabel",
            borderwidth=1,
            relief="solid",
            padding=5,
        )
        self.shelf.grid(columnspan=6, row=0, sticky="EW")

    def shelf_column_name(self):

        self.first_kolumn = ttk.Label(
            self.product,
            text="Produktu",
            style="column_style_os.TLabel",
            borderwidth=1,
            relief="solid",
            padding=2
        )

        self.second_kolumn = ttk.Label(
            self.product,
            text="Stan",
            style="column_style_os.TLabel",
            borderwidth=1,
            relief="solid",
            padding=2
        )

        self.third_kolumn = ttk.Label(
            self.product,
            text="Jednostka",
            style="column_style_os.TLabel",
            borderwidth=1,
            relief="solid",
            padding=2
        )

        self.fourth_kolumn = ttk.Label(
            self.product,
            text="ile szt. do kuchni?",
            style="column_style_os.TLabel",
            borderwidth=1,
            relief="solid",
            padding=2
        )

        self.first_kolumn.grid(column=0, row=1, sticky="EW")
        self.second_kolumn.grid(column=1, row=1, sticky="EW")
        self.third_kolumn.grid(column=2, row=1, sticky="EW")
        self.fourth_kolumn.grid(column=3, row=1, sticky="EW")


    def interactive_shelves_in_the_pantry(self):

        num1 = 2
        for x in self.all_db_pantry:

            self.article = ttk.Label(
                self.product,
                text=x[1],
                style="span_style_os.TLabel",
            )

            self.article_status = ttk.Label(
                self.product,
                text=x[3],
                style="span_style_os.TLabel",
            )

            self.article_unit_measure = ttk.Label(
                self.product,
                text=x[2],
                style="span_style_os.TLabel",
            )

            self.new_quantity_article = tk.IntVar(value=0)
            self.spin_qty =tk.Spinbox(
                self.product,
                from_=0,
                to=x[3],
                width=15,
                justify="center",
                font=("Courier New", 15),
                foreground=colour_char_hand,
                background=colour_label_span,
                relief="flat",
                buttonbackground=colour_label_span,
                textvariable=self.new_quantity_article,
            )

            self.article.grid(column=0, row=num1)
            self.article_status.grid(column=1, row=num1)
            self.article_unit_measure.grid(column=2, row=num1, padx=5)
            self.spin_qty.grid(column=3, row=num1)

            self.list_of_transferred_products[x[1]] = self.new_quantity_article

            num1 += 1

    def list_ingradients_approval_button(self):
        self.one_buttom = ttk.Button(
            self.product,
            text="spiżarnia ==> kuchnia",
            style="button_style_os.TButton",
        )
        self.one_buttom.grid(columnspan=4, row=50, sticky='ew')
        self.one_buttom.configure(command=self.pantry_status_update, )

    def pantry_status_update(self):
        print("Moduł pantry_status_update został uruchomiony.\n ===== vvv =====")

        for name, value in self.list_of_transferred_products.items():
            self.selected_val = value.get()
            self.name_product = name
            self.list_of_transferred_products[self.name_product] = self.selected_val
            print(self.name_product, self.selected_val)

        for name, value in self.list_of_transferred_products.items():
            if value > 0:
                print(f'drukowanie warunek if spełniane value =  {value}')

                for x in self.all_db_pantry:
                    if x[1] == name:
                        self.index_one = x[0]
                        self.state = x[3]
                        self.new_state = self.state - value

                if name not in self.products_taken_to_the_kitchen:
                    print("Działa")
                    self.products_taken_to_the_kitchen[name] = value
                else:
                    self.products_taken_to_the_kitchen[name] += value

                self.pantry_cursor.execute(
                    f"update products_items set quantity = {self.new_state} where id ={self.index_one}")
                self.pantry_db.commit()


        print(self.products_taken_to_the_kitchen)
        self.list_products_transferred()
        self.pantry_db.close()
        self.product.destroy()

        self.done_load_db()
        self.main_frame_shelves()
        self.main_frame_title_shelves()
        self.shelf_column_name()
        self.interactive_shelves_in_the_pantry()
        self.list_ingradients_approval_button()

    def list_products_transferred(self):

        self.list_freme_transferred = tk.Frame(
            self,
            background=colour_paper_hand,
            borderwidth=1,
            relief="solid",
            padx=20,
        )
        self.list_freme_transferred.grid(column=2, row=0)

        self.title_list = ttk.Label(
            self.list_freme_transferred,
            text="Przeniesione z Spiżarni do Kuchni",
            style="titile_frame_handwritten.TLabel",
        )

        self.title_column_name = ttk.Label(
            self.list_freme_transferred,
            text="Nazwa produktu",
            style="column_style_handwritten.TLabel",
        )

        self.title_column_valeu = ttk.Label(
            self.list_freme_transferred,
            text="Ilość szt.",
            style="column_style_handwritten.TLabel",
        )
        self.title_list.grid(columnspan=2, row=0)
        self.title_column_name.grid(column=0, row=1, sticky="ew")
        self.title_column_valeu.grid(column=1, row=1, sticky="ew")

        num3 = 2
        for name, valu in self.products_taken_to_the_kitchen.items():

            self.row_name = ttk.Label(
                self.list_freme_transferred,
                text=name,
                style="span_style_handwritten.TLabel",
            )

            self.row_value = ttk.Label(
                self.list_freme_transferred,
                text=f'{valu} szt.',
                style="span_style_handwritten.TLabel",
            )

            self.row_name.grid(column=0, row=num3)
            self.row_value.grid(column=1, row=num3)

            num3 += 1




