import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER

#głowe okno "Main window"

class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title("Domowa Spiżarnia")

        self.body_pantry = ttk.Frame(self)
        self.body_pantry.grid(column=0, row=0)

        self.hello_usel = ttk.Label(self.body_pantry, text="Witaj użytkowniku, ten program pomoże ci \n zapanować na twoją domową spiżarnią.")
        self.hello_usel.grid(column=0, row=0)

        # pojedyncze obszary głownego okna

        area_shelves = PantryShelves(self, padding=(10,10))
        area_shelves.grid(column=0, row=1)

        area_shopping = ShoppingList(self, padding=(10,10))
        area_shopping.grid(column=0, row=2)

        area_Ingredient = IngradientsList(self, padding=(10,10))
        area_Ingredient.grid(column=1, row=1, rowspan=2,)



class PantryShelves(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.product = ttk.Frame(self)
        self.product.grid()

        self.shelf = ttk.Label(self.product, text="Testowanie położenia kontenora z zawartością \n pułek spiżarni", background="Yellow")
        self.shelf.grid(column=0, columnspan=6, row=0, sticky="EW")

        self.to_the_garage = ttk.Button(self.product, text="do gara \n ==> ")
        self.to_the_garage.grid(column=5, row=1, rowspan=4, sticky="SN")


# zawartość półek

        #kukudza
        self.corn = ttk.Label(self.product, text="kukurydza",)
        self.corn.grid(column=0, row=1)

        self.status_corn = tk.IntVar(value=0)
        self.corn_quantitiative_status = ttk.Label(
            self.product,
            textvariable=self.status_corn,
        )
        self.corn_quantitiative_status.grid(column=1, row=1)

        #okno spin kukurydza
        self.quantity_corn = tk.IntVar(value=0)
        self.spin_corn = tk.Spinbox(
            self.product,
            from_=0,
            to=30,
            textvariable=self.quantity_corn,
            wrap=False
        )
        self.spin_corn.grid(column=2, row=1)



        #groszek
        self.beens = ttk.Label(self.product, text="kroszek",)
        self.beens.grid(column=0, row=2)

        self.status_beens = tk.IntVar(value=0)
        self.beens_quantitiative_status = ttk.Label(
            self.product,
            textvariable=self.status_beens,
        )
        self.beens_quantitiative_status.grid(column=1, row=2)

        self.quantity_beens = tk.IntVar(value=0)
        self.spin_beens = tk.Spinbox(
            self.product,
            from_=0,
            to=30,
            textvariable=self.quantity_beens,
            wrap=False
        )
        self.spin_beens.grid(column=2, row=2)

        #kasza
        self.groats = ttk.Label(self.product, text="Kasza",)
        self.groats.grid(column=0, row=3)

        self.status_groats = tk.IntVar(value=0)
        self.groats_quantitiative_status = ttk.Label(
            self.product,
            textvariable=self.status_groats,
        )
        self.groats_quantitiative_status.grid(column=1, row=3)

        self.quantity_groats = tk.IntVar(value=0)
        self.spin_groats = tk.Spinbox(
            self.product,
            from_=0,
            to=30,
            textvariable=self.quantity_groats,
            wrap=False
        )
        self.spin_groats.grid(column=2, row=3)


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
        self.component.pack()





if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()

