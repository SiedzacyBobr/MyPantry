import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()


class Adding_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.addding_conteiner()

    def addding_conteiner(self):

        self.addding_conteiner_frame = tk.Frame(self)
        self.addding_conteiner_frame.grid()

        self.title_addding_frame = ttk.Label(self.addding_conteiner_frame, text="Okienko do dodawanria produktów do spiżarni", style="Main_title_frame_os.TLabel")
        self.title_addding_frame.grid(columnspan=7, row=0)

        self.name_Entry = tk.Entry(self.addding_conteiner_frame, )
        self.name_Entry.grid(column=1, row=1)

        self.name_Label = tk.Label(self.addding_conteiner_frame, text="nazwa: ")
        self.name_Label.grid(column=0, row=1)

        self.unit_Entry = tk.Entry(self.addding_conteiner_frame, )
        self.unit_Entry.grid(column=3, row=1)

        self.unit_Label = tk.Label(self.addding_conteiner_frame, text="jednostka: ")
        self.unit_Label.grid(column=2, row=1)

        self.qty_Entry = tk.Entry(self.addding_conteiner_frame, )
        self.qty_Entry.grid(column=5, row=1)

        self.qty_Label = tk.Label(self.addding_conteiner_frame, text="ilość: " )
        self.qty_Label.grid(column=4, row=1)

        self.sefty_Entry = tk.Entry(self.addding_conteiner_frame,)
        self.sefty_Entry.grid(column=7, row=1)

        self.sefty_Label = tk.Label(self.addding_conteiner_frame, text="żelazny zapas")
        self.sefty_Label.grid(column=6, row=1)

        self.insert_buttom = tk.Button(self.addding_conteiner_frame, text="dodaj do mojej spiżarni", command=self.action_add_product)
        self.insert_buttom.grid(columnspan=8, sticky="EW")



    def action_add_product(self):

        self.name = self.name_Entry.get()
        self.unit = self.unit_Entry.get()
        self.qty = self.qty_Entry.get()
        self.sefty = self.sefty_Entry.get()
        print(f" uruchomienie action_add_product {self.name, self.unit, self.qty, self.sefty}")

        pantry_cursor.execute(
                f"INSERT INTO mypantry.products_items (name_product, unit_of_measure, quantity, seftystock) VALUES ( '{self.name}','{self.unit}', {self.qty}, {self.sefty})"
        )
        pantry_db.commit()

        print("Moduł action add_product zakończył swoje działanie. \n ===== ^^^^^ =====")





