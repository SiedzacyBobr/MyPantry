import tkinter as tk
from tkinter import ttk
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import colour_label_verse, colour_background, colour_board, colour_letter_board

class PantryShelvesClass(ttk.Frame):
    def __init__(self, container, *args, **kwargs,):
        super().__init__(container, *args, **kwargs)

        self.list_of_transferred_products = {}
        self.recipe_list = {}
        self.products_taken_to_the_kitchen = {}
        self.set_kategorii = set()
        self.number_of_views = 0

        #======================= główny frame skład ========================================

        self.product = tk.Frame(
            self,
            background=colour_background,
            width=700,
            height=450,
            padx=10,
            pady=10,
        )

        self.select_a_category_to_display = tk.Frame(
            self.product,
            background=colour_background,
        )

        self.list_being_printed = tk.Frame(
            self.product,
            background=colour_board,
        )

        self.Pantry_replenishment = tk.Frame(
            self.product,
            background=colour_background
        )

        self.product.pack()
        self.product.pack_propagate(0)
        self.select_a_category_to_display.grid(column=0, row=0)
        self.list_being_printed.grid(column=0, row=1)
        self.Pantry_replenishment.grid(column=0, row=2)

        # ==================================== uruchamianie poszczególnych elemnótów składowachy ===================

        self.done_load_db()
        self.scroll_bar_canvas()
        self.main_frame_title_shelves()
        self.shelf_column_name()
        self.list_ingradients_approval_button()

    def done_load_db(self):

        self.pantry_db = mysql.connector.connect(
            host="localhost",
            user=user_pantry,
            passwd=passwd,
            database="mypantry"
        )
        self.pantry_cursor = self.pantry_db.cursor()

        self.pantry_cursor.execute(f"SELECT products_items.id, products_items.name_product, "
                                   "products_items.unit_of_measure, products_items.quantity, "
                                   "products_items.seftystock, kategorie.kategoria"
                                   " FROM products_items"
                                   " JOIN kategorie"
                                   " ON products_items.id_kategorie = kategorie.id")

        self.all_db_pantry = self.pantry_cursor.fetchall()

        self.pantry_cursor.execute("SELECT kategoria"
                                   " FROM mypantry.kategorie"
                                   " WHERE kategoria != 'nowa'")
        self.category_list = self.pantry_cursor.fetchall()

    def scroll_bar_canvas(self):
        self.canvas_test = tk.Canvas(
            self.list_being_printed,
            background=colour_label_verse,
            width=630,
        )

        self.scrollable_frame = tk.Frame(
            self.canvas_test,
            background=colour_label_verse,
            width=618,
        )

        self.croll_bar = ttk.Scrollbar(
            self.list_being_printed,
            orient="vertical",
            command=self.canvas_test.yview
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas_test.configure(scrollregion=self.canvas_test.bbox("all")))

        self.canvas_test.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas_test.configure(yscrollcommand=self.croll_bar.set)

        self.croll_bar.pack(side="right", fill="y")
        self.canvas_test.pack(side="top", fill="both", expand=True)

    def main_frame_title_shelves(self):

        self.shelf = ttk.Label(
            self.select_a_category_to_display,
            text="Stan Spiżarni",
            style="title.TLabel",
            width=40,
        )
        # relief: "flat", "raised","sunken","groove", "ridge".

        self.kategoria = ttk.Label(
            self.select_a_category_to_display,
            text="wybór kategorii: ",
            style="background.TLabel",
            padding=7
        )

        self.selected_category = tk.StringVar()
        self.product_select = tk.Spinbox(
            self.select_a_category_to_display,
            values=self.category_list,
            textvariable=self.selected_category,
            font=("Courier New", 13),
            justify="center",
            background=colour_board,
            relief="flat",
            width=10,
        )

        self.button_choise = ttk.Button(
            self.select_a_category_to_display,
            style="button.TButton",
            text="Pokaż",
            command=self.interactive_shelves_in_the_pantry,
        )

        self.shelf.grid(columnspan=4, row=0, sticky="EW")
        self.kategoria.grid(columnspan=2, row=1, sticky="e")
        self.product_select.grid(column=2, row=1, sticky="w")
        self.button_choise.grid(column=3, row=1, sticky="e")

    def shelf_column_name(self):

        self.first_kolumn = ttk.Label(
            self.select_a_category_to_display,
            text="Produktu",
            style="column.TLabel",
            width=15,
        )

        self.second_kolumn = ttk.Label(
            self.select_a_category_to_display,
            text="Stan",
            style="column.TLabel",
            width=7,
        )

        self.third_kolumn = ttk.Label(
            self.select_a_category_to_display,
            text="Jednostka",
            style="column.TLabel",
            width=10,
        )

        self.fourth_kolumn = ttk.Label(
            self.select_a_category_to_display,
            text="ile szt.?",
            style="column.TLabel",
            width=10,
        )

        self.first_kolumn.grid(column=0, row=2, sticky="EW")
        self.second_kolumn.grid(column=1, row=2, sticky="EW")
        self.third_kolumn.grid(column=2, row=2, sticky="EW")
        self.fourth_kolumn.grid(column=3, row=2, sticky="EW")

    def interactive_shelves_in_the_pantry(self):

        self.button_choise["text"] = "Wyczyść"

        if self.number_of_views > 0:
            self.canvas_test.destroy()
            self.scrollable_frame.destroy()

            self.scroll_bar_canvas()

            self.number_of_views = 0
            self.button_choise["text"] = "Pokaż"

        else:

            self.product_list_by_category = []
            sort = self.selected_category.get()

            if sort == "całość":
                self.pantry_cursor.execute(f"SELECT products_items.id, products_items.name_product,"
                                           f" products_items.unit_of_measure, products_items.quantity,"
                                           f" products_items.seftystock"
                                           f" FROM products_items"
                                           f" ORDER BY name_product")
                self.product_list_by_category = self.pantry_cursor.fetchall()

            else:

                self.pantry_cursor.execute(f"SELECT products_items.id, products_items.name_product,"
                                           f" products_items.unit_of_measure, products_items.quantity,"
                                           f" products_items.seftystock"
                                           f" FROM products_items"
                                           f" WHERE id_kategorie = (select kategorie.id"
                                           f" FROM kategorie"
                                           f" WHERE kategoria = '{sort}')"
                                           f" ORDER BY name_product")

                self.product_list_by_category = self.pantry_cursor.fetchall()


            num1 = 3
            for x in self.product_list_by_category:

                self.article_name = x[1]
                self.availability = x[3]
                self.unit_of_measure = x[2]

                self.article = ttk.Label(
                    self.scrollable_frame,
                    text=self.article_name,
                    style="verse.TLabel",
                    width=20,
                )

                self.article_status = ttk.Label(
                    self.scrollable_frame,
                    text=self.availability,
                    style="verse.TLabel",
                    width=11,
                )

                self.article_unit_measure = ttk.Label(
                    self.scrollable_frame,
                    text=self.unit_of_measure,
                    style="verse.TLabel",
                    width=16,
                )

                self.new_quantity_article = tk.IntVar(value=0)
                self.spin_qty =tk.Spinbox(
                    self.scrollable_frame,
                    width=9,
                    from_=0,
                    to=x[3],
                    justify="center",
                    font=("Ink Free", 13),
                    background=colour_board,
                    foreground=colour_letter_board,
                    relief="flat",
                    textvariable=self.new_quantity_article,

                )

                self.article.grid(column=0, row=num1)
                self.article_status.grid(column=1, row=num1)
                self.article_unit_measure.grid(column=2, row=num1, padx=5)
                self.spin_qty.grid(column=3, row=num1)

                self.list_of_transferred_products[x[1]] = self.new_quantity_article
                num1 += 1

            self.number_of_views +=1

    def list_ingradients_approval_button(self):
        self.one_buttom = ttk.Button(
            self.Pantry_replenishment,
            text="Uzupełnij",
            style="button.TButton",
        )
        self.one_buttom.pack(side="top", ipadx=20, pady=5)
        self.one_buttom.configure(command=self.pantry_status_update, )

    def pantry_status_update(self):

        for name, value in self.list_of_transferred_products.items():
            self.selected_val = value.get()
            self.name_product = name
            self.list_of_transferred_products[self.name_product] = self.selected_val

        for name, value in self.list_of_transferred_products.items():
            if value > 0:

                for x in self.all_db_pantry:
                    if x[1] == name:
                        self.index_one = x[0]
                        self.state = x[3]
                        self.new_state = self.state - value

                if name not in self.products_taken_to_the_kitchen:

                    self.products_taken_to_the_kitchen[name] = value
                else:
                    self.products_taken_to_the_kitchen[name] += value

                self.pantry_cursor.execute(
                    f"update products_items set quantity = {self.new_state} where id ={self.index_one}")
                self.pantry_db.commit()

        self.list_products_transferred()
        self.pantry_db.close()
        self.product.destroy()


    def list_products_transferred(self):

        self.top_winodw = tk.Toplevel()
        self.top_winodw.title("Lista przeniesionych produktów")

        self.list_freme_transferred = tk.Frame(
            self.top_winodw,
            background=colour_label_verse,
            padx=20,
        )
        self.list_freme_transferred.grid(column=2, row=0)

        self.title_list = ttk.Label(
            self.list_freme_transferred,
            text="Przeniesione z Spiżarni do Kuchni",
            style="title.TLabel",
            width=45
        )

        self.title_column_name = ttk.Label(
            self.list_freme_transferred,
            text="Nazwa produktu",
            style="column.TLabel",
        )

        self.title_column_valeu = ttk.Label(
            self.list_freme_transferred,
            text="Ilość szt.",
            style="column.TLabel",
        )
        self.title_list.grid(columnspan=2, row=0)
        self.title_column_name.grid(column=0, row=1, sticky="ew")
        self.title_column_valeu.grid(column=1, row=1, sticky="ew")

        num3 = 2
        for name, valu in self.products_taken_to_the_kitchen.items():

            self.row_name = ttk.Label(
                self.list_freme_transferred,
                text=name,
                style="verse.TLabel",
            )

            self.row_value = ttk.Label(
                self.list_freme_transferred,
                text=f'{valu} szt.',
                style="verse.TLabel",
            )

            self.row_name.grid(column=0, row=num3)
            self.row_value.grid(column=1, row=num3)

            num3 += 1
