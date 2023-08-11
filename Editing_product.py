import tkinter as tk
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import *

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute(f"SELECT mypantry.home_pantry_products.id, mypantry.home_pantry_products.name, "
                           "mypantry.home_pantry_products.unit, mypantry.home_pantry_products.quty, "
                           "mypantry.home_pantry_products.sefty, mypantry.home_pantry_kategoria.cate"
                           " FROM mypantry.home_pantry_products"
                           " JOIN mypantry.home_pantry_kategoria"
                           " ON mypantry.home_pantry_products.category_id = mypantry.home_pantry_kategoria.id")

all_db_pantry = pantry_cursor.fetchall()

pantry_cursor.execute("SELECT cate"
                      " FROM mypantry.home_pantry_kategoria"
                      " WHERE cate != 'całość'")
all_category = pantry_cursor.fetchall()

name_all_pantry = []
pantry_cursor.execute("SELECT name"
                      " FROM mypantry.home_pantry_products"
                      )
name_testing = pantry_cursor.fetchall()

for i in name_testing:
    name_all_pantry.append(i[0])


class Editing_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.editing_conteiner()

    def editing_conteiner(self):

        self.editing_conteiner_frame = tk.Frame(
            self,
            background=colour_background,
            relief="flat",
            padx=10,
            pady=10,
        )
        self.editing_conteiner_frame.grid()

        self.title_editing_freme = ttk.Label(
            self.editing_conteiner_frame,
            text="Wybór produktu do edycji",
            style="title.TLabel",
            relief="flat",
            width=46,
        )

        self.name_all_product = name_all_pantry

        # for i in self.name_all_product:
        #     print(type(i), i )

        self.name_product = ttk.Label(
            self.editing_conteiner_frame,
            text="Produkt do edycji: ",
            style="background.TLabel",
        )

        self.product = tk.StringVar()
        self.product_select = tk.Spinbox(
            self.editing_conteiner_frame,
            values=self.name_all_product,
            textvariable=self.product,
            font=("Courier New", 13),
            justify="center",
            background=colour_board,
            relief="flat",
            width=20,
        )

#relief: "flat", "raised","sunken","groove", "ridge".


        self.editing_buttom = ttk.Button(
            self.editing_conteiner_frame,
            text="Edytuj",
            style="button.TButton",
            command=self.edit_product_in_my_pantry,
        )

        self.title_editing_freme.grid(columnspan=3, row=0, sticky="EW")
        self.name_product.grid(column=0, row=1, )
        self.product_select.grid(column=1, row=1, )
        self.editing_buttom.grid(column=2, row=1, sticky="e" )

    def edit_product_in_my_pantry(self,):

        self.name_product.destroy()
        self.editing_buttom.destroy()
        self.product_select.destroy()
        self.title_editing_freme.destroy()

        self.title_editing_freme = ttk.Label(
            self.editing_conteiner_frame,
            text="Edytewanie wybronego produktu w spiżarni",
            style="title.TLabel",
        )

        self.product_to_edit = self.product.get()

        for index, x in enumerate(all_db_pantry):


            if x[1] == self.product_to_edit:

                self.id_product_to_edit = x[0]
                self.name_to_edit = tk.StringVar(value=x[1])
                self.unit_to_edit = tk.StringVar(value=x[2])
                self.qty_to_edit = tk.IntVar(value=x[3])
                self.sefty_to_edit = tk.IntVar(value=x[4])
                self.selected_category= tk.StringVar()

                self.name_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="nazwa:",
                    style="background.TLabel",
                )
                self.unit_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="jednostka:",
                    style="background.TLabel",
                )
                self.qty_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="ilość:",
                    style="background.TLabel",
                )
                self.sefty_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="żelazny zapas:",
                    style="background.TLabel",
                )
                self.category_label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="kategoria:",
                    style="background.TLabel",
                )

                self.dystans = ttk.Label(
                    self.editing_conteiner_frame,
                    text=" ",
                    style="background.TLabel",
                )

                self.name_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.name_to_edit,
                    background=colour_board,
                    justify="center",
                    font=("Ink Free", 13),
                    relief="flat",
                    foreground=colour_letter_board
                )

                self.unit_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.unit_to_edit,
                    background=colour_board,
                    justify="center",
                    font=("Ink Free", 13),
                    relief="flat",
                    foreground=colour_letter_board,
                )
                self.qty_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.qty_to_edit,
                    background=colour_board,
                    justify="center",
                    font=("Ink Free", 13),
                    relief="flat",
                    foreground=colour_letter_board,
                )
                self.sefty_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.sefty_to_edit,
                    background=colour_board,
                    justify="center",
                    font=("Ink Free", 13),
                    relief="flat",
                    foreground=colour_letter_board,
                )

                self.category_entry = tk.Spinbox(
                    self.editing_conteiner_frame,
                    values=all_category,
                    textvariable=self.selected_category,
                    font=('Ink Free', 13),
                    relief="flat",
                    justify="center",
                    background=colour_board,
                    wrap=True,
                )
                self.selected_category.set(x[5])

                self.editing_buttom_all = ttk.Button(
                    self.editing_conteiner_frame,
                    text="Edytowanie produktu",
                    style="button.TButton",
                    command=self.editing_all,
                )
                # self.editing_buttom_all.bind("<Return>", self.editing_all)
                # self.editing_buttom_all.bind("<Button-1>", self.editing_all)

                self.title_editing_freme.grid(columnspan=2, row=0, sticky="EW")
                self.name_Label.grid(column=0, row=4, sticky="e")
                self.name_editing.grid(column=1, row=4, sticky="EW")
                self.unit_Label.grid(column=0, row=5, sticky="e")
                self.unit_editing.grid(column=1, row=5, sticky="EW")
                self.qty_Label.grid(column=0, row=6, sticky="e")
                self.qty_editing.grid(column=1, row=6, sticky="EW")
                self.sefty_Label.grid(column=0, row=7, sticky="e")
                self.sefty_editing.grid(column=1, row=7, sticky="EW")
                self.category_label.grid(column=0, row=8, sticky="e")
                self.category_entry.grid(column=1, row=8, sticky="ew")
                self.dystans.grid(column=0, row=9)
                self.editing_buttom_all.grid(columnspan=2, row=10, sticky="EW")

    def editing_all(self):

        self.title_editing_freme.destroy()
        self.name_Label.destroy()
        self.name_editing.destroy()
        self.unit_Label.destroy()
        self.unit_editing.destroy()
        self.qty_Label.destroy()
        self.qty_editing.destroy()
        self.sefty_Label.destroy()
        self.sefty_editing.destroy()
        self.category_label.destroy()
        self.category_entry.destroy()

        self.dystans.destroy()
        self.editing_buttom_all.destroy()

        self.id = self.id_product_to_edit
        self.name = self.name_to_edit.get()
        self.unit = self.unit_to_edit.get()
        self.qty = self.qty_to_edit.get()
        self.sefty = self.sefty_to_edit.get()
        self.kate = self.selected_category.get()

        pantry_cursor.execute(
            f"UPDATE mypantry.home_pantry_products SET name = '{self.name}' WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.home_pantry_products SET unit = '{self.unit}' WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.home_pantry_products SET quty= {int(self.qty)} WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.home_pantry_products SET sefty= {int(self.sefty)} WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.home_pantry_products SET category_id = (select id from mypantry.home_pantry_kategoria where cate = '{self.kate}') WHERE id = {self.id}"
        )
        pantry_db.commit()

        self.title_editing_freme = ttk.Label(
            self.editing_conteiner_frame,
            text="Wybór produktu do edycji",
            style="title.TLabel",
            width=46,
        )

        self.masage_label = ttk.Label(
            self.editing_conteiner_frame,
            text=f' Produkt: {self.name} - został zedytowany',
            style="background.TLabel",
        )
        self.title_editing_freme.grid(column=0, row=0)
        self.masage_label.grid(column=0, row=1)
