import tkinter as tk
import ShoppingList, PantryShelves, Addding_product, Delete_product, Editing_product
from tkinter import ttk
from Style_constrakt import style_constrakt

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.title("Domowa Spiżarnia")

        self.body_pantry = tk.Frame(
            self,
            pady=10,
            padx=10,
            width=691,
            height=150,
            borderwidth=1,
            relief="solid"
        )
        self.body_pantry.grid(column=0, row=0)
        self.body_pantry.grid_propagate(0)

        self.manu_app()
        self.info_for_user()
        self.all_frames_create()
        self.hello_user = None

        self.pantry_conteiners()
        style_constrakt()

    def manu_app(self):

        self.main_menu = tk.Menu(self)

        self.main_menu.add_command(label="Zakupy", command=self.shopping_conteiners)
        self.main_menu.add_command(label="Spiżarnia", command=self.pantry_conteiners)
        self.main_menu.add_command(label="Dodawanie", command=self.addding_conteiner)
        self.main_menu.add_command(label="Usuwanie", command=self.delete_conteiner)
        self.main_menu.add_command(label="Edytowanie", command=self.editing_conteiner)

        self.config(menu=self.main_menu)

    def info_for_user(self):

        self.hello_user = ttk.Label(
            self.body_pantry,
            text="Witaj użytkowniku, ten program pomoże ci \n "
             "zapanować nad twoją domową spiżarnią. \n "
             "Sa dwie drogi: sklep ==> spiżarnia i spiżarnia ==> kuchnia \n Powodzenia :) \n",
             style="Main_title_frame_os.TLabel",
            borderwidth=1,
            relief="solid",
            width=66
        )

        self.reload_buttom = ttk.Button(
            self.body_pantry,
            text="odświeżenie",
            command=self.update_main
        )

        self.hello_user.grid(column=0, row=0, sticky="ew")
        self.reload_buttom.grid(column=0, row=1)

    def update_main(self):
        self.destroy()
        root = MainPantryWindow()
        root.mainloop()

    def all_frames_create(self):

        self.pantry_conteiner = tk.Frame(self)
        self.shopping_conteiner = tk.Frame(self)
        self.addding_product_conteiner = tk.Frame(self)
        self.delete_product_conteiner = tk.Frame(self)
        self.editing_product_conteiner = tk.Frame(self)

    def pantry_conteiners(self):

        self.clean_window()
        self.pantry_conteiner.grid(column=0, row=1)

        area_shelves = PantryShelves.PantryShelvesClass(
            self.pantry_conteiner,
            padding=10,
        )
        area_shelves.grid()

    def shopping_conteiners(self):
        self.clean_window()
        self.shopping_conteiner.grid(column=0, row=1)

        area_shopping = ShoppingList.ShoppingList(
            self.shopping_conteiner,
            padding=10,
        )
        area_shopping.grid()

    def addding_conteiner(self):
        self.clean_window()

        self.addding_product_conteiner.grid(column=0, row=1)

        addding_action = Addding_product.Adding_action_product(
            self.addding_product_conteiner,
            padding=(10, 10),
        )
        addding_action.grid()

    def delete_conteiner(self):
        self.clean_window()

        self.delete_product_conteiner.grid(column=0, row=1)

        delete_action = Delete_product.Delete_action_product(
            self.delete_product_conteiner,
            padding=(10, 10),
        )
        delete_action.grid()

    def editing_conteiner(self):
        self.clean_window()

        self.editing_product_conteiner.grid(column=0, row=1)

        editing_action = Editing_product.Editing_action_product(self.editing_product_conteiner, padding=(10, 10))
        editing_action.grid()

    def clean_window(self):
        self.shopping_conteiner.grid_forget()
        self.pantry_conteiner.grid_forget()
        self.addding_product_conteiner.grid_forget()
        self.delete_product_conteiner.grid_forget()
        self.editing_product_conteiner.grid_forget()


if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()