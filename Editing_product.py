import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()


class Editing_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.editing_conteiner()

    def editing_conteiner(self):

        self.editing_conteiner_frame = tk.Frame(self,)
        self.editing_conteiner_frame.grid()

        self.title_editing_freme = ttk.Label(self.editing_conteiner_frame, text="Okienko do edytewania produktu w Spiżarni :)", style="Main_title_frame_os.TLabel")
        self.title_editing_freme.grid(columnspan=8, row=0, sticky="EW")

        self.name_all_product = name_all_pantry
        print(self.name_all_product)

        self.name_product = ttk.Label(self.editing_conteiner_frame, text="Produkt do zedytowania: ")
        self.name_product.grid(column=0, row=1)

        self.product = tk.StringVar()
        self.product_select = ttk.Spinbox(self.editing_conteiner_frame,
                                          values=self.name_all_product,
                                          textvariable=self.product
                                          )
        self.product_select.grid(column=1, row=1)


        self.editing_buttom = ttk.Button(self.editing_conteiner_frame, text="Wybierz produkt", command=self.edit_product_in_my_pantry)
        self.editing_buttom.grid(columnspan=8, row=2, sticky="EW")

    def edit_product_in_my_pantry(self):

        self.name_product.destroy()
        self.editing_buttom.destroy()
        self.product_select.destroy()

        print(f"delete{self.product}")

        self.product_to_edit = self.product.get()

        for index, x in enumerate(all_db_pantry):

            if x[1] == self.product_to_edit:

                self.id_product_to_edit = x[0]
                self.name_to_edit = tk.StringVar(value=x[1])
                self.unit_to_edit = tk.StringVar(value=x[2])
                self.qty_to_edit = tk.IntVar(value=x[3])
                self.sefty_to_edit = tk.IntVar(value=x[4])

                self.name_Label = tk.Label(self.editing_conteiner_frame, text="nazwa: ")
                self.name_Label.grid(column=0, row=4)

                self.name_editing = tk.Entry(self.editing_conteiner_frame, textvariable=self.name_to_edit)
                self.name_editing.grid(column=1, row=4)

                self.unit_Label = tk.Label(self.editing_conteiner_frame, text="jednostka: ")
                self.unit_Label.grid(column=2, row=4)

                self.unit_editing = tk.Entry(self.editing_conteiner_frame, textvariable=self.unit_to_edit)
                self.unit_editing.grid(column=3, row=4)

                self.qty_Label = tk.Label(self.editing_conteiner_frame, text="ilość: ")
                self.qty_Label.grid(column=4, row=4)

                self.qty_editing = tk.Entry(self.editing_conteiner_frame, textvariable=self.qty_to_edit)
                self.qty_editing.grid(column=5, row=4)

                self.sefty_Label = tk.Label(self.editing_conteiner_frame, text="żelazny zapas")
                self.sefty_Label.grid(column=6, row=4)

                self.sefty_editing = tk.Entry(self.editing_conteiner_frame, textvariable=self.sefty_to_edit)
                self.sefty_editing.grid(column=7, row=4)

                self.editing_buttom_all = ttk.Button(self.editing_conteiner_frame, text="Edytowanie produktu", command=self.editing_all)
                self.editing_buttom_all.grid(columnspan=8, row=5, sticky="EW")


        print(f'  product do edycki i jego id {self.product_to_edit, self.id_product_to_edit}')

    def editing_all(self):
        self.id = self.id_product_to_edit
        self.name = self.name_to_edit.get()
        self.unit = self.unit_to_edit.get()
        self.qty = self.qty_to_edit.get()
        self.sefty = self.sefty_to_edit.get()

        print(f" nowe dane do edycki {self.id}  {self.name}   {self.unit}  {self.qty}   {self.sefty}")

        pantry_cursor.execute(
            f"UPDATE mypantry.products_items SET name_product = '{self.name}' WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.products_items SET unit_of_measure = '{self.unit}' WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.products_items SET quantity= {int(self.qty)} WHERE id = {self.id}"
        )
        pantry_db.commit()

        pantry_cursor.execute(
            f"UPDATE mypantry.products_items SET seftystock= {int(self.sefty)} WHERE id = {self.id}"
        )
        pantry_db.commit()


        print(f"zakończona udycja produtku {self.name}")




