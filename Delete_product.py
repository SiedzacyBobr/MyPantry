import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry
from Style_constrakt import colour_paper_hand, colour_label_span

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()


class Delete_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.delete_conteiner()

    def delete_conteiner(self):

        self.delete_conteiner_frame = tk.Frame(
            self,
            background=colour_label_span,
            borderwidth=1,
            relief="solid",
            padx=10,
            pady=10,
        )
        self.delete_conteiner_frame.grid()

        self.title_delete_freme = ttk.Label(
            self.delete_conteiner_frame,
            text="Wybór produktu do usunięcia",
            style="Title_on_add_del_edit.TLabel",
            borderwidth=2,
            relief="solid",
            width=46,
        )

        self.name_all_product = name_all_pantry

        self.name_product = ttk.Label(
            self.delete_conteiner_frame,
            text="Produkt do usunięcia: ",
            style="Comment_on_add_del_edit.TLabel",
        )

        self.product = tk.StringVar()
        self.product_select = tk.Spinbox(
            self.delete_conteiner_frame,
            values=self.name_all_product,
            textvariable=self.product,
            font=("Courier New", 15),
            justify="center",
            background=colour_paper_hand,
            borderwidth=2,
            relief="sunken",
        )
        self.delete_buttom = ttk.Button(
            self.delete_conteiner_frame,
            text="Usuwanie produktu",
            style="Buttom_on_add_del_edit.TButton",
            command=self.delete_product_from_my_pantry,
        )

        self.title_delete_freme.grid(columnspan=2, row=0, sticky="EW")
        self.name_product.grid(column=0, row=1)
        self.product_select.grid(column=1, row=1)
        self.delete_buttom.grid(columnspan=2, row=2, sticky="EW")

    def delete_product_from_my_pantry(self):

        self.name_product.destroy()
        self.product_select.destroy()
        self.delete_buttom.destroy()

        self.name_delete_product = self.product.get()

        self.masage_label = ttk.Label(
            self.delete_conteiner_frame,
            text=f' Produkt: {self.name_delete_product} - został usunięty z spiżarni',
            style="Comment_on_add_del_edit.TLabel",
        )

        self.masage_label.grid(column=1, row=1)

        self.product_to_delete = self.product.get()

        pantry_cursor.execute(
            f"DELETE FROM mypantry.products_items WHERE name_product='{self.product_to_delete}'")
        pantry_db.commit()
