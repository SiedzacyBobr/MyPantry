import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry


# dostęp do bazy danych

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

# zmienne globalne

schoping_list = {}
list_chack_box_botton = {}
list_spin_box_botton = {}

class ShoppingList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.main_construct_shopping()
        self.title_contener_shopping_lis()
        self.name_column_shopping_list()
        self.chack_button_end_spin_box_constract()
        self.selection_list_approval_button()

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

        self.second_kolumn_list = ttk.Label(self.shop_list, text="Nazwa produktu i jednostka", background="gray", borderwidth=1, relief='solid')
        self.second_kolumn_list.grid(column=1, row=1, sticky="EW")

        self.third_kolumn_list = ttk.Label(self.shop_list, text="Ilość", background="gray", borderwidth=1,
                                      relief='solid')
        self.third_kolumn_list.grid(column=2, row=1, sticky="EW")

    def chack_button_end_spin_box_constract(self):

# tworzenie ekranu w pętli

        num10 = 25
        for index, x in enumerate(all_db_pantry):

            self.name_product = x[1]

# tworzenie checkbotton

            self.selected_option = tk.IntVar(value=None)
            self.testing_chack_buttom = ttk.Checkbutton(self.shop_list,
                                                    variable=self.selected_option,
                                                    onvalue=1,
                                                    offvalue=0,
                                                    text=self.name_product
                                                    )


            if x[4] > x[3]:
                self.testing_chack_buttom.grid(column=0, row=num10)

            list_chack_box_botton[self.name_product] = self.selected_option



# tworzenie spin boxa

            self.quantity_items = tk.IntVar(value=x[4] - x[3])
            self.spin_box = tk.Spinbox(
                self.shop_list,
                from_=0,
                to=30,
                textvariable=self.quantity_items,
                )

            if x[4] > x[3]:
                self.spin_box.grid(column=2, row=num10)

            list_spin_box_botton[x[1]] = self.quantity_items

            num10 +=1


    def chack_box_print_list(self):

# tworzenie labelki z informacją że zmiana została dokonana w bazie danych.

        mylabel = ttk.Label(self.shop_list, text="Lista została zrealizowania i dodana do spiżarni")
        mylabel.grid()

# tworzenie listy nazwa wartość

        for name, value in list_chack_box_botton.items():
            self.selected_op = value.get()
            list_chack_box_botton[name] = self.selected_op

        for name, value in list_spin_box_botton.items():
            self.selected_sp = value.get()
            list_spin_box_botton[name] = self.selected_sp

# tworzenie listy nazwa wartość

        self.shoping_index = 0
        for name_s, volue_s in list_chack_box_botton.items():

            if volue_s == 1 and name_s in list_spin_box_botton:

                print(f'spełniony warunek dla {name_s} i wartości {volue_s}')

                self.guantity_s = list_spin_box_botton[name_s]

                if self.guantity_s > 0:

                    print(f"Kupiono {name_s} ilość {self.guantity_s}")

                    schoping_list[name_s] = self.guantity_s

                    self.state_s = all_db_pantry[self.shoping_index][3]
                    self.new_state_s = int(self.state_s) + int(self.guantity_s)

                    pantry_cursor.execute(
                        f"update products_items set quantity = {self.new_state_s} where id ={self.shoping_index + 1}")
                    pantry_db.commit()

                    self.shoping_index += 1
            else:
                self.shoping_index += 1
                print(f"warunek nie spełniony dla {name_s}")


        print(schoping_list)


    def selection_list_approval_button(self):

        self.action_buttom = ttk.Button(self.shop_list, text="selecektywny wybór przez chackbox")
        self.action_buttom.grid(column=0, columnspan=6, row=51, sticky="EW")
        self.action_buttom.configure(command=self.chack_box_print_list)