import tkinter as tk
from tkinter import ttk, N, S, E, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from tkinter import font
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
        # self.pantry_is_safe()

    def main_construct_shopping(self):

        self.shop_list = tk.Frame(self, background="#FFFFFF", borderwidth=1, relief='solid', padx=10, pady=10)
        self.shop_list.grid()

    def title_contener_shopping_lis(self):

        for index, x in enumerate(all_db_pantry):
            if x[4] > x[3]:

                self.items_products = ttk.Label(self.shop_list, text="Lista Zakupów ",style="titile_frame_handwritten.TLabel")
                self.items_products.grid(columnspan=5, row=0, sticky="EW")


    # def pantry_is_safe(self):
    #
    #     self.items_products = ttk.Label(self.shop_list, text="W spiżarni jest bezpieczny satan żywności")
    #     self.items_products.grid(column=0, row=0, sticky="EW")
    #     self.items_products.configure(anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE",
    #                                   font=("Arial", 12))


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
                                                    )

            if x[4] > x[3]:
                self.testing_chack_buttom.grid(column=0, row=num10)

            list_chack_box_botton[self.name_product] = self.selected_option

# nazwa produktu

            self.name_product_label = ttk.Label(self.shop_list, text=x[1], style="span_style_handwritten.TLabel")

            if x[4] > x[3]:
                self.name_product_label.grid(column=1, row=num10)


# nazwa jednostki miary

            self.unit_of_measure = ttk.Label(self.shop_list, text=x[2], style="span_style_handwritten.TLabel")

            if x[4] > x[3]:
                self.unit_of_measure.grid(column=2, row=num10)


# tworzenie spin boxa

            self.quantity_items = tk.IntVar(value=x[4] - x[3])
            self.spin_box = tk.Spinbox(
                self.shop_list,
                from_=0,
                to=30,
                textvariable=self.quantity_items,
                width=15,
                justify="center",
                font=("Ink Free", 12, "bold"),
                foreground="#1E6ADE",
                background="#FFFFFF",
                relief="flat"
                )

            if x[4] > x[3]:
                self.spin_box.grid(column=3, row=num10)

            list_spin_box_botton[x[1]] = self.quantity_items

            num10 +=1


    def chack_box_print_list(self):

# tworzenie labelki z informacją że zmiana została dokonana w bazie danych.

        mylabel = ttk.Label(self.shop_list, text="Lista została zrealizowania i dodana do spiżarni")
        mylabel.grid(columnspan=3)
        mylabel.configure(anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE", font=("Arial", 10))

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
        #self.chack_button_end_spin_box_constract()

    def name_column_shopping_list(self):

        for index, x in enumerate(all_db_pantry):
            if x[4] > x[3]:

                self.first_kolumn_list = ttk.Label(self.shop_list, text="Ptaszek", style="column_style_handwritten.TLabel")
                self.first_kolumn_list.grid(column=0, row=1, sticky="EW")



                self.first_kolumn_list = ttk.Label(self.shop_list, text="Produkt", style="column_style_handwritten.TLabel")
                self.first_kolumn_list.grid(column=1, row=1, sticky="EW")


                self.second_kolumn_list = ttk.Label(self.shop_list, text="Jednostka", style="column_style_handwritten.TLabel")
                self.second_kolumn_list.grid(column=2, row=1, sticky="EW")


                self.third_kolumn_list = ttk.Label(self.shop_list, text="Ilość", style="column_style_handwritten.TLabel")
                self.third_kolumn_list.grid(column=3, row=1, sticky="EW")



    def selection_list_approval_button(self):

        for index, x in enumerate(all_db_pantry):
            if x[4] > x[3]:

                self.action_buttom = ttk.Button(self.shop_list, text="Zakupy zrobione")
                self.action_buttom.grid(column=0, columnspan=6, row=51, sticky="EW")
                self.action_buttom.configure(command=self.chack_box_print_list)