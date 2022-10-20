import tkinter as tk
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from LenList import name_all_pantry, len_all_pantry
import PantryShelves

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

class IngradientsListClass(ttk.Frame):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.main_concruct_diner()
        self.title_contener_diner_list()
        self.list_approval_button()

    def main_concruct_diner(self):

        self.recipe_diner = ttk.Frame(self)
        self.recipe_diner.grid(sticky="ew")

    def title_contener_diner_list(self):

        self.component = ttk.Label(self.recipe_diner, text="Test położenia \n kontenera z przepisem na obiad", background="lightblue")
        self.component.grid(column=0, row=0)

    def all_list_out(self):
        print("dupa funcja z IngradientsList")

        t = tk.Toplevel(self.recipe_diner)
        t.wm_title("Window kacry")

        label_window = tk.Label(t, text="This is window prom all_list_out_method")
        label_window.pack()

        postep = ttk.Label(t, text= "Jest pastęp i to spory")
        postep.pack()

        num6 =11
        for index, x in enumerate(PantryShelves.PantryShelvesClass(self).spin_qty):
            quty = x.get()
            if int(quty) > 0:
                print("działa if !!")

                quty_label_title = ttk.Label(t, text="ilość", background="green")
                quty_label_title.pack()

                quty_name_title = ttk.Label(t, text="nazwa produktu", background="green")
                quty_name_title.pack()


                quty_label = ttk.Label(t, text=quty)
                quty_label.pack()
                quty_name = ttk.Label(t, text=(name_all_pantry[index]))
                quty_name.pack()

            num6 +=1

    def db_pantry_update(self):
        pass
        # stan = all_db_pantry[index][3]
        # new_stan = int(stan) - int(quty)
        # print(f'stan obecny magazynu: {name_all_pantry[index]}   ==> {stan}')
        # print(f'f wyciągnięto z magazynu: {name_all_pantry[index]}  ==>  {quty} ')
        # print(f' stan obecne magazynu {name_all_pantry[index]} ==> {new_stan}')
        # pantry_cursor.execute(f"update products_items set quantity = {new_stan} where id ={index+1}")
        # pantry_db.commit()

    def list_approval_button(self):

        self.buttom_ingra = ttk.Button(self.recipe_diner, text="potwierdzam")
        self.buttom_ingra.grid(column=0, row=2, sticky='ew')
        self.buttom_ingra.configure(command=self.all_list_out)