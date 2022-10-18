import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry


pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#================================================ główne okno "Main window" ============================================


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

#=============================================== Okno stanu spużarni ===================================================


class PantryShelves(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


    # Tytuł dla kontenera stanu spiżarni

        self.product = ttk.Frame(self)
        self.product.grid()

        self.shelf = ttk.Label(self.product, text="Testowanie położenia kontenera z zawartością \n półek spiżarni", background="Yellow", borderwidth=1, relief='solid')
        self.shelf.grid(column=0, columnspan=6, row=0, sticky="EW")

        self.product_scroll = ttk.Scrollbar(self.product, orient="vertical")
        self.product_scroll.grid(row=0, rowspan=10, column=10, sticky="ns")

    #tytuły kolum:

        self.first_kolumn = ttk.Label(self.product, text="Nazwa produktu", background="orange", borderwidth=1, relief='solid')
        self.first_kolumn.grid(column=0, row=1, sticky="EW")

        self.second_kolumn = ttk.Label(self.product, text="Stan", background="orange", borderwidth=1, relief='solid')
        self.second_kolumn.grid(column=1, row=1, sticky="EW")

        self.third_kolumn = ttk.Label(self.product, text="Jednostka", background="orange", borderwidth=1, relief='solid')
        self.third_kolumn.grid(column=2, row=1, sticky="EW")

        self.fourth_kolumn = ttk.Label(self.product, text="do poprania", background="orange", borderwidth=1, relief='solid')
        self.fourth_kolumn.grid(column=3, row=1, sticky="EW")

        # self.fifth_kolumn = ttk.Label(self.product, text="przycisk", background="orange", borderwidth=1, relief='solid')
        # self.fifth_kolumn.grid(column=4, row=1, sticky="EW")

    #Wyświetlanie zawartości bazy danych:

        #nazwa produktu
        num1 = 2
        for x in all_db_pantry:
            self.article = ttk.Label(self.product, text=x[1])
            self.article.grid(column=0, row=num1)
            num1 += 1

        #stan ilościowy w spiżarni
        num3 = 2
        for x in all_db_pantry:
            self.article_status = ttk.Label(self.product, text=x[3],)
            self.article_status.grid(column=1, row=num3)
            num3 += 1

        #jednostka miary
        num5 = 2
        for x in all_db_pantry:
            self.article_unit_measure = ttk.Label(self.product, text=x[2], )
            self.article_unit_measure.grid(column=2, row=num5, padx=5)
            num5 += 1

        # stworzenie listy odpowiadającej ilości rekordów w bazie danych.

        self.len_wszystko =[]

        for wszy in range(len(all_db_pantry)):
            self.len_wszystko.append(wszy)

        # print(self.len_wszystko)

        self.name_wszystko = []
        for index, name in enumerate(all_db_pantry):
            self.name_wszystko.append(name[1] + " " + name[2])

        # print(self.name_wszystko)

        # stworzenie list listy elementów, na podstawie ilości rekortów w basie danych.

        self.new_quantity_article = [tk.IntVar(value=0) for wszy in self.len_wszystko]
        self.spin_qty =[tk.Spinbox(self.product, from_=0, to=30, textvariable=self.new_quantity_article[wszy]) for wszy in self.len_wszystko]
        # self.to_the_garage = [tk.Button(self.product, text=f'{wszy} ==>') for wszy in self.len_wszystko]
        self.name_wszystko_measure = [ttk.Label(self.product, text=f'{namas}') for namas in self.name_wszystko]

        # funkcja dla przycisków

        # def to_the_garage_list(name, quty):
        #     def f():
        #         pokazowa_labelka_ile = ttk.Label(self.product, text="")
        #         pokazowa_labelka_ile.config(text=name)
        #         pokazowa_labelka_ile.grid(column=2)
        #         pokazowa_labelka_name = ttk.Label(self.product, text="")
        #         pokazowa_labelka_name.config(textvariable=quty)
        #         pokazowa_labelka_name.grid(column=1)
        #
        #     return f

        # stworzenie elementow do wyświetlenia na eklanie gdzie każdy elemnet jest indexowany.

        num4 = 2
        for x in range(len(self.spin_qty)):
            self.spin_qty[x].grid(column=3, row=num4)
            num4 += 1

        # num2 = 2
        # for x in range(len(self.to_the_garage)):
        #     self.to_the_garage[x].grid(column=4, row=num2,)
        #     self.to_the_garage[x].configure(command= to_the_garage_list( self.name_wszystko_measure[x]['text'], self.spin_qty[x]['textvariable']))
        #     num2 +=1


        def all_list():
            num6 =11
            for index, x in enumerate(self.spin_qty):
                quty = x.get()
                if int(quty) > 0:

                    quty_label_title = ttk.Label(self.product, text="ilość", background="orange")
                    quty_label_title.grid(column=1, row=10)

                    quty_name_title = ttk.Label(self.product, text="nazwa produktu", background="orange")
                    quty_name_title.grid(column=2, row=10)


                    quty_label = ttk.Label(self.product, text=quty)
                    quty_label.grid(column=1, row=num6)
                    quty_name = ttk.Label(self.product, text=(self.name_wszystko[index]))
                    quty_name.grid(column=2, row=num6)

                num6 +=1

        self.one_buttom = ttk.Button(self.product, text="do gara ==>")
        self.one_buttom.grid(columnspan=4, row=50, sticky='ew')
        self.one_buttom.configure(command=all_list)

#=========================================== Okno Lista zakupów ========================================================


class ShoppingList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        self.shop_list = ttk.Frame(self)
        self.shop_list.grid()

        self.items_products = ttk.Label(self.shop_list, text="Testowanie położenia konterena z listą zakupów", background="lightgrey")
        self.items_products.grid(column=0, columnspan= 5, row=0, sticky="EW")

        self.first_kolumn_list = ttk.Label(self.shop_list, text="Czy kupiono?", background="grey", borderwidth=1,
                                      relief='solid')
        self.first_kolumn_list.grid(column=0, row=1, sticky="EW")

        self.second_kolumn_list = ttk.Label(self.shop_list, text="Nazwa produktu", background="gray", borderwidth=1, relief='solid')
        self.second_kolumn_list.grid(column=1, row=1, sticky="EW")

        self.third_kolumn_list = ttk.Label(self.shop_list, text="Ilość", background="gray", borderwidth=1,
                                      relief='solid')
        self.third_kolumn_list.grid(column=2, row=1, sticky="EW")


        # Lista zakupów do realizacji

        self.czy_kupione = tk.StringVar()

        def drukowanie_listy_zrealizowanej():
            if self.czy_kupione.get() == "on":
                print(self.czy_kupione.get())
                print("hura działa zaznaczania")
            else:
                print(self.czy_kupione.get())
                print("Dupa aktualizacja zakupów")

        num9 = 2
        for index, x in enumerate(all_db_pantry):
            index +=1

            if x[3] < x[4]:

                self.chack_button = ttk.Checkbutton(self.shop_list, text="kupione?", variable=self.czy_kupione, onvalue="on", offvalue='off')
                self.chack_button.grid(column=0, row=index + num9, )

                self.items_products1 = ttk.Label(self.shop_list, text=x[1], )
                self.items_products1.grid(column=1, row=index + num9, )

                self.quantity_items = tk.IntVar(value=x[4]-x[3])
                self.spin_box = tk.Spinbox(
                    self.shop_list,
                    from_=0,
                    to=30,
                    textvariable=self.quantity_items,
                )
                self.spin_box.grid(column=2, row=index + num9)
                num9 +=1
            else:
                num9 +=1

        # przycisk potwierczający realizacja zakupów podsumowanie listy

        self.action_buttom = ttk.Button(self.shop_list, text="Kupione", command=drukowanie_listy_zrealizowanej)
        self.action_buttom.grid(column=0, columnspan=6, row=50, sticky="EW")

#=========================================== Okno Lista produktów do gara===============================================


class IngradientsList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.recipe_diner = ttk.Frame(self)
        self.recipe_diner.pack()

        self.component = ttk.Label(self.recipe_diner, text="Test położenia \n kontenera z przepisem na obiad", background="lightblue")
        self.component.pack(side="top")

        self.lista = ttk.Label(self.recipe_diner, text="")
        self.lista.pack(side="top")

        self.buttom_ingra = ttk.Button(self.recipe_diner, text="potwierdzam")
        self.buttom_ingra.pack(side="bottom", fill="x", expand=True, anchor="s")


if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()

