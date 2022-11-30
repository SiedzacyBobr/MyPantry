import tkinter as tk
import tkinter.font as font
import ShoppingList, PantryShelves, IngradientsList
import mysql.connector
from tkinter import ttk
from lokalhost_entry import passwd, user_pantry
from tkinter import ttk, N, S, E, NS, CENTER

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class MainPantryWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.hello_user = None
        self.body_pantry = None
        self.main_container()
        self.stacking_conteiners()
        self.style_constrakt()


    def style_constrakt(self):

        self.style_main = ttk.Style(self)
        self.style_main.theme_use("alt")
# style pisane ręcznie

        self.style_main.configure("titile_frame_handwritten.TLabel",
                                  anchor=CENTER,
                                  background="#FFFFFF",
                                  foreground="#1E6ADE",
                                  font=("Ink Free", 17, "bold", "underline"))

        self.style_main.configure("column_style_handwritten.TLabel",
                                  anchor=CENTER,
                                  background="#FFFFFF",
                                  foreground="#1E6ADE",
                                  font=("Ink Free", 15, "bold"))

        self.style_main.configure("span_style_handwritten.TLabel",
                                  anchor=CENTER,
                                  background="#FFFFFF",
                                  foreground="#1E6ADE",
                                  font=("Ink Free", 15,))

# style pisane komputerowo

        self.style_main.configure("column_style_os.TLabel",  anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE", font=("Courier New", 15))
        self.style_main.configure("span_style_os.TLabel",  anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE", font=("Courier New", 13))

        self.style_main.configure("button_style_os.TLabel",  anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE", font=("Courier New", 12))

        self.style_main.configure("info_style_os.TLabel",  anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE", font=("Courier New", 15))
        self.style_main.configure("titile_frame_os.TLabel", anchor=CENTER, background="#FAFAF1", foreground="#1E6ADE",
                                  font=("Courier New.TLabel", 15))


    def main_container(self):

        self.title("Domowa Spiżarnia")
        font.nametofont("TkDefaultFont").config(size=12)

        self.body_pantry = tk.Frame(self, borderwidth=2, relief='solid',background="White")
        self.body_pantry.pack(side="top", fill="both", expand=True)

        self.hello_user = ttk.Label(self.body_pantry,
                                    text="Witaj użytkowniku, ten program pomoże ci \n zapanować nad twoją domową spiżarnią. :)",
                                    padding=(10,10,5),
                                    background="White"
                                    )
        self.hello_user.pack()

    def stacking_conteiners(self):

        area_ingredient = IngradientsList.IngradientsListClass(self, padding=(10, 10), borderwidth=1, relief='solid')
        area_ingredient.pack(side="right", fill="both", expand=True)

        area_shelves = PantryShelves.PantryShelvesClass(self, padding=(10,10), borderwidth=1, relief='solid')
        area_shelves.pack(side="top", fill="both", expand=True)

        area_shopping = ShoppingList.ShoppingList(self, padding=(10,10), borderwidth=1, relief='solid')
        area_shopping.pack(side="top", fill="both", expand=True)


if __name__ == '__main__':
    root = MainPantryWindow()
    root.mainloop()

