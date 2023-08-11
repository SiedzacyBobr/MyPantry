import tkinter as tk
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import *

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("SELECT cate"
                      " FROM mypantry.home_pantry_kategoria"
                      " WHERE cate != 'całość'")
all_kategoria = pantry_cursor.fetchall()

class Adding_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.addding_conteiner()

    def addding_conteiner(self):

        self.addding_conteiner_frame = tk.Frame(
            self,
            background=colour_background,
            # borderwidth=2,
            relief="flat",
            padx=10,
            pady=10,
        )
        self.addding_conteiner_frame.grid()

        self.title_addding_frame = ttk.Label(
            self.addding_conteiner_frame,
            text="Okienko do dodawania produktów do spiżarni",
            style="title.TLabel",
            # borderwidth=2,
            relief="flat",
            width=46,
        )

        self.name_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="nazwa:",
            style="background.TLabel",
        )
        self.unit_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="jednostka:",
            style="background.TLabel",
        )
        self.qty_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="ilość:",
            style="background.TLabel",
        )
        self.sefty_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="żelazny zapas:",
            style="background.TLabel",
        )
        self.category_label = ttk.Label(
            self.addding_conteiner_frame,
            text="kategoria:",
            style="background.TLabel",
        )
        self.dystans = ttk.Label(
            self.addding_conteiner_frame,
            text=" ",
            style="background.TLabel",
        )

        self.name_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_board,
            width=20,
            justify="center",
            font=("Ink Free", 13),
            # borderwidth=2,
            relief="flat",
            foreground=colour_letter_board,
        )

        self.unit_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_board,
            justify="center",
            font=("Ink Free", 13),
            # borderwidth=2,
            relief="flat",
            foreground=colour_letter_board,
        )

        self.qty_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_board,
            justify="center",
            font=("Ink Free", 13),
            # borderwidth=2,
            relief="flat",
            foreground=colour_letter_board,
        )

        self.sefty_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_board,
            justify="center",
            font=("Ink Free", 13),
            #borderwidth=2,
            relief="flat",
            foreground=colour_letter_board,
        )

        self.selected_category = tk.StringVar()
        self.category_Entry = tk.Spinbox(
            self.addding_conteiner_frame,
            values=all_kategoria,
            textvariable=self.selected_category,
            font=('Ink Free', 13),
            background=colour_board,
            relief="flat",
            justify="center",
        )
        self.insert_buttom = ttk.Button(
            self.addding_conteiner_frame,
            text="Dodaj",
            command=self.action_add_product,
            style="button.TButton",
        )

        self.title_addding_frame.grid(columnspan=2, row=0, sticky="ew")
        self.name_Label.grid(column=0, row=1, sticky="e")
        self.name_Entry.grid(column=1, row=1, sticky="ew")
        self.unit_Label.grid(column=0, row=2, sticky="e")
        self.unit_Entry.grid(column=1, row=2, sticky="ew")
        self.qty_Label.grid(column=0, row=3, sticky="e")
        self.qty_Entry.grid(column=1, row=3, sticky="ew")
        self.sefty_Label.grid(column=0, row=4, sticky="e")
        self.sefty_Entry.grid(column=1, row=4, sticky="ew")
        self.category_label.grid(column=0, row=5, sticky="e")
        self.category_Entry.grid(column=1, row=5, sticky="ew")
        self.dystans.grid(column=0, row=6)
        self.insert_buttom.grid(column=1, row=7, sticky="E")

    def action_add_product(self):

        self.name = self.name_Entry.get()
        self.unit = self.unit_Entry.get()
        self.qty = self.qty_Entry.get()
        self.sefty = self.sefty_Entry.get()
        self.kate = self.category_Entry.get()

        pantry_cursor.execute(
            f"INSERT INTO mypantry.home_pantry_kategoria (cate) "
            f"select * from (select '{self.kate}' as cate) as new_value "
            f"where not exists (select cate from mypantry.home_pantry_kategoria where cate = '{self.kate}') limit 1"
        )
        pantry_db.commit()


        pantry_cursor.execute(
            f"INSERT INTO mypantry.home_pantry_products"
            f" (name, unit, quty, sefty, category_id)"
            f" VALUES ( '{self.name}','{self.unit}', {self.qty} , {self.sefty}, (select id from mypantry.home_pantry_kategoria where cate = '{self.kate}'))"
        )

        pantry_db.commit()

        self.name_Label.destroy()
        self.name_Entry.destroy()
        self.unit_Label.destroy()
        self.unit_Entry.destroy()
        self.qty_Label.destroy()
        self.qty_Entry.destroy()
        self.sefty_Label.destroy()
        self.sefty_Entry.destroy()
        self.category_label.destroy()
        self.category_Entry.destroy()
        self.dystans.destroy()
        self.insert_buttom.destroy()

        self.masage_label = ttk.Label(
            self.addding_conteiner_frame,
            text=f' Produkt: {self.name} - został dodany do spiżarni',
            style="background.TLabel",
        )
        self.masage_label.grid(columnspan=9, row=3)




