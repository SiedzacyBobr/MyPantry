import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()


class ShoppingList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.main_construct_shopping()
        self.title_contener_shopping_lis()
        self.name_column_shopping_list()
        self.list_of_items_for_shopping()
        self.chack_button_constract()
        self.list_shopping_approval_button()

    def main_construct_shopping(self):

        self.shop_list = ttk.Frame(self)
        self.shop_list.grid(sticky="ew")

    def title_contener_shopping_lis(self):

        self.items_products = ttk.Label(self.shop_list, text="Testowanie położenia konterena z listą zakupów", background="lightgrey")
        self.items_products.grid(column=0, columnspan= 5, row=0, sticky="EW")

    def name_column_shopping_list(self):

        self.first_kolumn_list = ttk.Label(self.shop_list, text="Czy kupiono?", background="grey", borderwidth=1,
                                      relief='solid')
        self.first_kolumn_list.grid(column=0, row=1, sticky="EW")

        self.second_kolumn_list = ttk.Label(self.shop_list, text="Nazwa produktu", background="gray", borderwidth=1, relief='solid')
        self.second_kolumn_list.grid(column=1, row=1, sticky="EW")

        self.third_kolumn_list = ttk.Label(self.shop_list, text="Ilość", background="gray", borderwidth=1,
                                      relief='solid')
        self.third_kolumn_list.grid(column=2, row=1, sticky="EW")

    def list_of_items_for_shopping(self):
        self.spin_box_list = []
        self.label_list = []

        num9 = 2
        for index, x in enumerate(all_db_pantry):

            if x[3] < x[4]:

                self.items_products1 = ttk.Label(self.shop_list, text=x[1] + " -" +x[2])
                self.items_products1.grid(column=1, row=num9)

                self.label_list.append(index)

                self.quantity_items = tk.IntVar(value=x[4]-x[3])
                self.spin_box = tk.Spinbox(
                    self.shop_list,
                    from_=0,
                    to=30,
                    textvariable=self.quantity_items,
                )
                self.spin_box.grid(column=2, row=num9)
                self.spin_box_list.append(self.spin_box)

                num9 +=1
            else:
                pass

    def chack_button_constract(self):

        self.it_is_bought = [tk.IntVar(value=0) for len_n in len_all_pantry]
        self.chack_button_list = [
            ttk.Checkbutton(self.shop_list, onvalue=1, offvalue=0, variable=self.it_is_bought[len_n]) for len_n in
            len_all_pantry]

        num10 = 2
        for x in self.label_list:
            self.chack_button_list[x].grid(column=0, row=num10)
            num10 +=1

    def list_shopping_approval_button(self):

        self.action_buttom = ttk.Button(self.shop_list, text="Kupione")
        self.action_buttom.grid(column=0, columnspan=6, row=50, sticky="EW")
        self.action_buttom.configure()