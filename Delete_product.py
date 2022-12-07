import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()


class Delete_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.delete_conteiner()

    def delete_conteiner(self):

        self.delete_conteiner_frame = tk.Frame(self, background= "lightblue")
        self.delete_conteiner_frame.grid()

        self.title_delete_freme = ttk.Label(self.delete_conteiner_frame, text="Okienko do usuwania produktu z Spiżarni :)", style="Main_title_frame_os.TLabel")
        self.title_delete_freme.grid(columnspan=2, row=0, sticky="EW")

        self.name_all_product = name_all_pantry
        print(self.name_all_product)

        self.name_product = ttk.Label(self.delete_conteiner_frame, text="Produkt do usunięcia: ")
        self.name_product.grid(column=0, row=1)

        self.product = tk.StringVar()

        self.product_select = ttk.Spinbox(self.delete_conteiner_frame,
                                         values=self.name_all_product,
                                         textvariable=self.product
                                         )
        self.product_select.grid(column=1, row=1)


        self.delete_buttom = ttk.Button(self.delete_conteiner_frame, text="Usuwanie produktu", command=self.delete_product_from_my_pantry)
        self.delete_buttom.grid(columnspan=2, row=2, sticky="EW")

    def delete_product_from_my_pantry(self):

        self.name_product.destroy()
        self.product_select.destroy()
        self.delete_buttom.destroy()

        self.name_delete_product = self.product.get()

        self.masage_label = ttk.Label(self.delete_conteiner_frame, text= f' Produkt {self.name_delete_product} został usunięty')
        self.masage_label.grid(column=1, row=1)


        print(f"delete{self.product}")

        self.product_to_delete = self.product.get()

        print(self.product_to_delete)

        pantry_cursor.execute(
            f"DELETE FROM mypantry.products_items WHERE name_product='{self.product_to_delete}'")
        pantry_db.commit()

    def delete_del_conteiner(self):
        pass
