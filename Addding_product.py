import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import colour_label_column, colour_label_span, colour_paper_hand, colour_char_hand

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("SELECT kategoria"
                      " FROM mypantry.kategorie"
                      " WHERE kategoria != 'całość'")
all_kategoria = pantry_cursor.fetchall()

class Adding_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.addding_conteiner()

    def addding_conteiner(self):

        self.addding_conteiner_frame = tk.Frame(
            self,
            background=colour_label_span,
            borderwidth=1,
            relief="solid",
            padx=10,
            pady=10,
        )
        self.addding_conteiner_frame.grid()

        self.title_addding_frame = ttk.Label(
            self.addding_conteiner_frame,
            text="Okienko do dodawania produktów do spiżarni",
            style="Title_on_add_del_edit.TLabel",
            borderwidth=2,
            relief="solid",
            width=46,
        )

        self.name_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="nazwa:",
            style="Comment_on_add_del_edit.TLabel",
        )
        self.unit_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="jednostka:",
            style="Comment_on_add_del_edit.TLabel",
        )
        self.qty_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="ilość:",
            style="Comment_on_add_del_edit.TLabel",
        )
        self.sefty_Label = ttk.Label(
            self.addding_conteiner_frame,
            text="żelazny zapas:",
            style="Comment_on_add_del_edit.TLabel",
        )
        self.category_label = ttk.Label(
            self.addding_conteiner_frame,
            text="kategoria:",
            style="Comment_on_add_del_edit.TLabel",
        )
        self.dystans = ttk.Label(
            self.addding_conteiner_frame,
            text=" ",
            style="Comment_on_add_del_edit.TLabel",
        )

        self.name_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_paper_hand,
            width=20,
            justify="center",
            font=("Ink Free", 13),
            borderwidth=2,
            relief="sunken",
            foreground=colour_char_hand,
        )

        self.unit_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_paper_hand,
            justify="center",
            font=("Ink Free", 13),
            borderwidth=2,
            relief="sunken",
            foreground=colour_char_hand,
        )

        self.qty_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_paper_hand,
            justify="center",
            font=("Ink Free", 13),
            borderwidth=2,
            relief="sunken",
            foreground=colour_char_hand,
        )

        self.sefty_Entry = tk.Entry(
            self.addding_conteiner_frame,
            background=colour_paper_hand,
            justify="center",
            font=("Ink Free", 13),
            borderwidth=2,
            relief="sunken",
            foreground=colour_char_hand,
        )

        self.selected_category = tk.StringVar()
        self.category_Entry = tk.Spinbox(
            self.addding_conteiner_frame,
            values=all_kategoria,
            textvariable=self.selected_category,
            font=('Ink Free', 13),
            borderwidth=2,
            relief="sunken",
            justify="center",
        )
        self.insert_buttom = ttk.Button(
            self.addding_conteiner_frame,
            text="dodaj do mojej spiżarni",
            command=self.action_add_product,
            style="Buttom_on_add_del_edit.TButton",
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
        self.insert_buttom.grid(columnspan=2, row=7, sticky="EW")

    def action_add_product(self):

        self.name = self.name_Entry.get()
        self.unit = self.unit_Entry.get()
        self.qty = self.qty_Entry.get()
        self.sefty = self.sefty_Entry.get()
        self.kate = self.category_Entry.get()

        pantry_cursor.execute(
            f"INSERT INTO mypantry.kategorie (kategoria) "
            f"select * from (select '{self.kate}' as kategoria) as new_value "
            f"where not exists (select kategoria from mypantry.kategorie where kategoria = '{self.kate}') limit 1"
        )
        pantry_db.commit()


        pantry_cursor.execute(
            f"INSERT INTO mypantry.products_items"
            f" (name_product, unit_of_measure, quantity, seftystock, id_kategorie)"
            f" VALUES ( '{self.name}','{self.unit}', {self.qty} , {self.sefty}, (select id from mypantry.kategorie where kategoria = '{self.kate}'))"
        )

        pantry_db.commit()

        self.masage_label = ttk.Label(
            self.addding_conteiner_frame,
            text=f' Produkt: {self.name} - został dodany do spiżarni',
            style="Comment_on_add_del_edit.TLabel",
        )
        self.masage_label.grid(columnspan=9, row=3)




