import tkinter as tk
import ShoppingList, PantryShelves, Addding_product, Delete_product, Editing_product, ShoppingDone
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

        self.manu_app()
        self.all_frames_create()
        self.hello_user = None

        self.pantry_conteiners()
        style_constrakt()

    def manu_app(self):

        self.main_menu = tk.Menu(self)

        self.main_menu.add_command(label="Na Zakupy", command=self.shopping_conteiners)
        self.main_menu.add_command(label="Po Zakupach", command=self.shopping_done)
        self.main_menu.add_command(label="Spiżarnia", command=self.pantry_conteiners)
        self.main_menu.add_command(label="Dodawanie", command=self.addding_conteiner)
        self.main_menu.add_command(label="Usuwanie", command=self.delete_conteiner)
        self.main_menu.add_command(label="Edytowanie", command=self.editing_conteiner)

        self.config(menu=self.main_menu)

    def all_frames_create(self):

        self.pantry_conteiner = tk.Frame(self)
        self.shopping_conteiner = tk.Frame(self)
        self.shopping_done_conteiner = tk.Frame(self)
        self.addding_product_conteiner = tk.Frame(self)
        self.delete_product_conteiner = tk.Frame(self)
        self.editing_product_conteiner = tk.Frame(self)

    def pantry_conteiners(self):

        self.clean_window()
        self.pantry_conteiner.grid(column=0, row=1)

        area_shelves = PantryShelves.PantryShelvesClass(
            self.pantry_conteiner,
        )
        area_shelves.grid(column=0, row=0)

    def shopping_conteiners(self):
        self.clean_window()
        self.shopping_conteiner.grid(column=0, row=1)

        area_shopping = ShoppingList.ShoppingList(
            self.shopping_conteiner,
        )
        area_shopping.grid(column=0, row=0)

    def shopping_done(self):
        self.clean_window()
        self.shopping_done_conteiner.grid(column=0, row=1)

        area_shopping_done = ShoppingDone.ShoppingDone(
            self.shopping_done_conteiner,
        )
        area_shopping_done.grid(column=0, row=0)


    def addding_conteiner(self):
        self.clean_window()

        self.addding_product_conteiner.grid(column=0, row=1)

        addding_action = Addding_product.Adding_action_product(
            self.addding_product_conteiner,
        )
        addding_action.grid(column=0, row=0)

    def delete_conteiner(self):
        self.clean_window()

        self.delete_product_conteiner.grid(column=0, row=1)

        delete_action = Delete_product.Delete_action_product(
            self.delete_product_conteiner,
        )
        delete_action.grid(column=0, row=0)

    def editing_conteiner(self):
        self.clean_window()

        self.editing_product_conteiner.grid(column=0, row=1)

        editing_action = Editing_product.Editing_action_product(self.editing_product_conteiner, padding=(10, 10))
        editing_action.grid(column=0, row=0)

    def clean_window(self):
        self.shopping_conteiner.grid_forget()
        self.shopping_done_conteiner.grid_forget()
        self.pantry_conteiner.grid_forget()
        self.addding_product_conteiner.grid_forget()
        self.delete_product_conteiner.grid_forget()
        self.editing_product_conteiner.grid_forget()

if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()