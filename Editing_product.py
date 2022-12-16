import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry
from Style_constrakt import colour_label_column, colour_label_span, colour_paper_hand, colour_char_hand

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()


class Editing_action_product(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.editing_conteiner()

    def editing_conteiner(self):

        self.editing_conteiner_frame = tk.Frame(
            self,
            background=colour_label_span,
            borderwidth=1,
            relief="solid",
            padx=10,
            pady=10,
        )
        self.editing_conteiner_frame.grid()

        self.title_editing_freme = ttk.Label(
            self.editing_conteiner_frame,
            text="Wybór produktu do edycji",
            style="Title_on_add_del_edit.TLabel",
            borderwidth=2,
            relief="solid",
            width=46,
        )

        self.name_all_product = name_all_pantry

        self.name_product = ttk.Label(
            self.editing_conteiner_frame,
            text="Produkt do zedytowania: ",
            style="Comment_on_add_del_edit.TLabel",
        )

        self.product = tk.StringVar()
        self.product_select = tk.Spinbox(
            self.editing_conteiner_frame,
            values=self.name_all_product,
            textvariable=self.product,
            font=("Courier New", 15),
            justify="center",
            background=colour_paper_hand,
            borderwidth=2,
            relief="sunken",
        )
#relief: "flat", "raised","sunken","groove", "ridge".


        self.editing_buttom = ttk.Button(
            self.editing_conteiner_frame,
            text="Edytowanie produktu",
            style="Buttom_on_add_del_edit.TButton",
            command=self.edit_product_in_my_pantry,
        )

        self.title_editing_freme.grid(columnspan=2, row=0, sticky="EW")
        self.name_product.grid(column=0, row=1, sticky="ew")
        self.product_select.grid(column=1, row=1,)
        self.editing_buttom.grid(columnspan=2, row=2, sticky="EW")

    def edit_product_in_my_pantry(self):

        self.name_product.destroy()
        self.editing_buttom.destroy()
        self.product_select.destroy()
        self.title_editing_freme.destroy()

        self.title_editing_freme = ttk.Label(
            self.editing_conteiner_frame,
            text="Edytewanie wybronego produktu w spiżarni",
            style="Title_on_add_del_edit.TLabel",
        )

        self.product_to_edit = self.product.get()

        for index, x in enumerate(all_db_pantry):

            if x[1] == self.product_to_edit:

                self.id_product_to_edit = x[0]
                self.name_to_edit = tk.StringVar(value=x[1])
                self.unit_to_edit = tk.StringVar(value=x[2])
                self.qty_to_edit = tk.IntVar(value=x[3])
                self.sefty_to_edit = tk.IntVar(value=x[4])

                self.name_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="nazwa:",
                    style="Comment_on_add_del_edit.TLabel",
                )
                self.unit_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="jednostka:",
                    style="Comment_on_add_del_edit.TLabel",
                )
                self.qty_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="ilość:",
                    style="Comment_on_add_del_edit.TLabel",
                )
                self.sefty_Label = ttk.Label(
                    self.editing_conteiner_frame,
                    text="żelazny zapas:",
                    style="Comment_on_add_del_edit.TLabel",
                )
                self.dystans = ttk.Label(
                    self.editing_conteiner_frame,
                    text=" ",
                    style="Comment_on_add_del_edit.TLabel",
                )

                self.name_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.name_to_edit,
                    background=colour_paper_hand,
                    #width=20,
                    justify="center",
                    font=("Ink Free", 13),
                    borderwidth=2,
                    relief="sunken",
                    foreground=colour_char_hand,
                )
                self.unit_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.unit_to_edit,
                    background=colour_paper_hand,
                    width=7,
                    justify="center",
                    font=("Ink Free", 13),
                    borderwidth=2,
                    relief="sunken",
                    foreground=colour_char_hand,
                )
                self.qty_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.qty_to_edit,
                    background=colour_paper_hand,
                    width=5,
                    justify="center",
                    font=("Ink Free", 13),
                    borderwidth=2,
                    relief="sunken",
                    foreground=colour_char_hand,
                )
                self.sefty_editing = tk.Entry(
                    self.editing_conteiner_frame,
                    textvariable=self.sefty_to_edit,
                    background=colour_paper_hand,
                    width=5,
                    justify="center",
                    font=("Ink Free", 13),
                    borderwidth=2,
                    relief="sunken",
                    foreground=colour_char_hand,
                )

                self.editing_buttom_all = ttk.Button(
                    self.editing_conteiner_frame,
                    text="Edytowanie produktu",
                    command=self.editing_all,
                    style="Buttom_on_add_del_edit.TButton",
                )

                self.title_editing_freme.grid(columnspan=9, row=0, sticky="EW")
                self.name_Label.grid(column=0, row=4)
                self.name_editing.grid(column=1, row=4)
                self.unit_Label.grid(column=2, row=4)
                self.unit_editing.grid(column=3, row=4)
                self.qty_Label.grid(column=4, row=4)
                self.qty_editing.grid(column=5, row=4)
                self.sefty_Label.grid(column=6, row=4)
                self.sefty_editing.grid(column=7, row=4)
                self.dystans.grid(column=8, row=4)
                self.editing_buttom_all.grid(columnspan=9, row=5, sticky="EW")

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
        self.dystans.destroy()
        self.editing_buttom_all.destroy()

        self.id = self.id_product_to_edit
        self.name = self.name_to_edit.get()
        self.unit = self.unit_to_edit.get()
        self.qty = self.qty_to_edit.get()
        self.sefty = self.sefty_to_edit.get()

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

        self.title_editing_freme = ttk.Label(
            self.editing_conteiner_frame,
            text="Wybór produktu do edycji",
            style="Title_on_add_del_edit.TLabel",
            width=46,
        )


        self.masage_label = ttk.Label(
            self.editing_conteiner_frame,
            text=f' Produkt: {self.name} - został zedytowany',
            style="Comment_on_add_del_edit.TLabel",
        )
        self.title_editing_freme.grid(column=0, row=0)
        self.masage_label.grid(column=0, row=1)
