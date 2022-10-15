import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector

mydb = mysql.connector.connect()
my_cursor = mydb.cursor()

my_cursor.execute("select * from mypantry.products_items")
wszystko = my_cursor.fetchall()


# def to_the_garage(id, index):
#     where_is = id
#     result2 = my_cursor.execute(f"select quantity from mypantry.products_items where id = {where_is}")
#     result2 = my_cursor.fetchall()
#     print(where_is)
#     print(result2)

import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#główne okno "Main window"

class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title("Domowa Spiżarnia")

        self.body_pantry = ttk.Frame(self, borderwidth=1, relief='solid')
        self.body_pantry.pack(side="top", fill="both", expand=True)

        font.nametofont("TkDefaultFont").config(size=12)

        self.hello_usel = ttk.Label(self.body_pantry, text="Witaj użytkowniku, ten program pomoże ci \n zapanować nad twoją domową spiżarnią.", padding=(10,10))
        self.hello_usel.pack()

        # pojedyncze obszary głownego okna

        area_Ingredient = IngradientsList(self, padding=(10, 10), borderwidth=1, relief='solid')
        area_Ingredient.pack(side="right", fill="both", expand=True)

        area_shelves = PantryShelves(self, padding=(10,10), borderwidth=1, relief='solid')
        area_shelves.pack(side="top", fill="both", expand=True)

        area_shopping = ShoppingList(self, padding=(10,10), borderwidth=1, relief='solid')
        area_shopping.pack(side="top", fill="both", expand=True)


class PantryShelves(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        def edit_qty(id, index):
            pass


        self.product = ttk.Frame(self)
        self.product.grid()

        self.shelf = ttk.Label(self.product, text="Testowanie położenia kontenera z zawartością \n półek spiżarni", background="Yellow")
        self.shelf.grid(column=0, columnspan=6, row=0, sticky="EW")


        #Wyświetlanie zawartości bazy danych:

        num1 = 1
        for x in wszystko:

            self.article = ttk.Label(self.product, text=x[1])
            self.article.grid(column=0, row=num1)
            num1 += 1

        num3 = 1
        for x in wszystko:
            self.article_status = ttk.Label(self.product, text=x[3],)
            self.article_status.grid(column=1, row=num3)
            num3 += 1

        #okno spin kukurydza
        num2 = 1
        for index, x in enumerate(wszystko):
            index +=1
            id_reference = x[0]
            self.new_quantity_article = tk.IntVar(value=0,)
            self.spin_corn = tk.Spinbox(
                self.product,
                from_=0,
                to=30,
                textvariable=self.new_quantity_article,
                wrap=False,
            )
            self.spin_corn.grid(column=2, row=num2)
            num2 +=1

        #przycist wysyłający dowary do gara

        num4 = 1
        for index, x in enumerate(wszystko):
            id_reference = str(x[3])
            self.to_the_garage = ttk.Button(self.product, text=f"ID {x[0]} do gara \n ==> ", command=lambda : edit_qty(id_reference, index))
            self.to_the_garage.grid(column=5, row=num4, sticky="SN")
            num4 += 1

class ShoppingList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        self.shop_list = ttk.Frame(self)
        self.shop_list.grid()

        self.items_products = ttk.Label(self.shop_list, text="Testowanie położenia konterena z listą zakupów", background="lightgrey")
        self.items_products.grid(column=0, columnspan= 5, row=0, sticky="EW")


# Lista zakupów do realizacji

        # kukurydza
        self.chack_button = ttk.Checkbutton(self.shop_list, text="zgadza się", onvalue="zgadza sie", offvalue="brak",)
        self.chack_button.grid(column=1, row=1,)

        self.items_products1 = ttk.Label(self.shop_list, text="kukurydza",)
        self.items_products1.grid(column=2, row=1,)

        self.quantity_items = tk.IntVar(value=0)
        self.spin_box = tk.Spinbox(
            self.shop_list,
            from_=0,
            to=30,
            textvariable=self.quantity_items,
            wrap=False
        )
        self.spin_box.grid(column=3, row=1)

        #grosek konserwowo

        self.chack_button = ttk.Checkbutton(self.shop_list, text="zgadza się", onvalue="zgadza sie", offvalue="brak" )
        self.chack_button.grid(column=1, row=2, )

        self.items_products1 = ttk.Label(self.shop_list, text="Groszk")
        self.items_products1.grid(column=2, row=2, )

        self.quantity_items = tk.IntVar(value=0)
        self.spin_box = tk.Spinbox(
            self.shop_list,
            from_=0,
            to=30,
            textvariable=self.quantity_items,
            wrap=False
        )
        self.spin_box.grid(column=3, row=2)

        #Kasza

        self.chack_button = ttk.Checkbutton(self.shop_list, text="zgadza się", onvalue="zgadza sie", offvalue="brak")
        self.chack_button.grid(column=1, row=3, )

        self.items_products1 = ttk.Label(self.shop_list, text="Kasza")
        self.items_products1.grid(column=2, row=3, )

        self.quantity_items = tk.IntVar(value=0)
        self.spin_box = tk.Spinbox(
            self.shop_list,
            from_=0,
            to=30,
            textvariable=self.quantity_items,
            wrap=False
        )
        self.spin_box.grid(column=3, row=3)
# podsumowanie listy

        self.action_buttom = ttk.Button(self.shop_list, text="Kupione")
        self.action_buttom.grid(column=0, columnspan=6, row=10, sticky="EW")



class IngradientsList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.recipe_diner = ttk.Frame(self)
        self.recipe_diner.pack()

        self.component = ttk.Label(self.recipe_diner, text="Test położenia \n kontenera z przepisem na obiad", background="lightblue")
        self.component.pack(side="top")

        self.lista = ttk.Label(self.recipe_diner, text="kukurydza \n groszek \n kasza \n")
        self.lista.pack(side="top")

        self.buttom_ingra = ttk.Button(self.recipe_diner, text="potwierdzam")
        self.buttom_ingra.pack(side="bottom", fill="x", expand=True, anchor="s")





if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()

