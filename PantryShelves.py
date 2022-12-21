import tkinter as tk
from tkinter import ttk
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import colour_label_span, colour_char_hand, colour_paper_hand

class PantryShelvesClass(ttk.Frame):
    def __init__(self, container, *args, **kwargs,):
        super().__init__(container, *args, **kwargs)

        self.list_of_transferred_products = {}
        self.recipe_list = {}
        self.products_taken_to_the_kitchen = {}
        self.set_kategorii = set()

        self.done_load_db()
        self.main_frame_shelves()
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

    def main_frame_shelves(self):

        self.product = tk.Frame(
            self,
            background=colour_label_span,
            width=691,
            height=350,
            borderwidth=1,
            relief="solid",
            padx=10,
            pady=10,
        )
        self.product.pack()
        self.product.pack_propagate(0)

    def scroll_bar_canvas(self):
        self.canvas_test = tk.Canvas(
            self.product,
            background=colour_label_span
        )

        self.scrollable_frame = tk.Frame(
            self.canvas_test,
            background=colour_label_span
        )

        self.croll_bar = ttk.Scrollbar(
            self.product,
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
            self.scrollable_frame,
            text="Stan Spiżarni",
            style="titile_frame_os.TLabel",
            borderwidth=2,
            relief="solid",
            width=45,
        )
        # relief: "flat", "raised","sunken","groove", "ridge".

        self.kategoria = ttk.Label(
            self.scrollable_frame,
            text="wybór kategorii: ",
            style="span_style_os.TLabel",
        )

        self.selected_category = tk.StringVar()
        self.product_select = tk.Spinbox(
            self.scrollable_frame,
            values=self.category_list,
            textvariable=self.selected_category,
            font=("Courier New", 15),
            justify="center",
            background=colour_paper_hand,
            borderwidth=2,
            relief="sunken",
            width=10,
        )

        self.button_choise = ttk.Button(
            self.scrollable_frame,
            style="Button_style_os.TButton",
            text="Pokaż",
            command=self.interactive_shelves_in_the_pantry
        )

        self.shelf.grid(columnspan=4, row=0, sticky="EW")
        self.kategoria.grid(columnspan=2, row=1, sticky="ew")
        self.product_select.grid(column=2, row=1)
        self.button_choise.grid(column=3, row=1)

    def shelf_column_name(self):

        self.first_kolumn = ttk.Label(
            self.scrollable_frame,
            text="Produktu",
            style="column_style_os.TLabel",
        )

        self.second_kolumn = ttk.Label(
            self.scrollable_frame,
            text="Stan",
            style="column_style_os.TLabel",
        )

        self.third_kolumn = ttk.Label(
            self.scrollable_frame,
            text="Jednostka",
            style="column_style_os.TLabel",
        )

        self.fourth_kolumn = ttk.Label(
            self.scrollable_frame,
            text="ile szt.?",
            style="column_style_os.TLabel",
        )

        self.first_kolumn.grid(column=0, row=2, sticky="EW")
        self.second_kolumn.grid(column=1, row=2, sticky="EW")
        self.third_kolumn.grid(column=2, row=2, sticky="EW")
        self.fourth_kolumn.grid(column=3, row=2, sticky="EW")

    def interactive_shelves_in_the_pantry(self):

        self.product_list_by_category = []
        sort = self.selected_category.get()
        print(f"Zdobyta wybrana kategoria : {sort}")

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
            self.article = ttk.Label(
                self.scrollable_frame,
                text=x[1],
                style="span_style_os.TLabel",
            )

            self.article_status = ttk.Label(
                self.scrollable_frame,
                text=x[3],
                style="span_style_os.TLabel",
            )

            self.article_unit_measure = ttk.Label(
                self.scrollable_frame,
                text=x[2],
                style="span_style_os.TLabel",
            )

            self.new_quantity_article = tk.IntVar(value=0)
            self.spin_qty =tk.Spinbox(
                self.scrollable_frame,
                width=5,
                from_=0,
                to=x[3],
                justify="center",
                font=("Ink Free", 15),
                foreground=colour_char_hand,
                background=colour_paper_hand,
                borderwidth=2,
                relief="sunken",
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
            style="Button_style_os.TButton",
        )
        self.one_buttom.pack(side="bottom", fill="x")
        self.one_buttom.configure(command=self.pantry_status_update, )

    def pantry_status_update(self):

        for name, value in self.list_of_transferred_products.items():
            self.selected_val = value.get()
            self.name_product = name
            self.list_of_transferred_products[self.name_product] = self.selected_val
            print(self.name_product, self.selected_val)


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

        self.done_load_db()
        self.main_frame_shelves()
        self.scroll_bar_canvas()
        self.main_frame_title_shelves()
        self.shelf_column_name()
        self.interactive_shelves_in_the_pantry()
        self.list_ingradients_approval_button()

    def list_products_transferred(self):

        self.top_winodw = tk.Toplevel()
        self.top_winodw.title("Lista przeniesionych produktów")

        self.list_freme_transferred = tk.Frame(
            self.top_winodw,
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
            width=45
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
