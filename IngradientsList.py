from tkinter import ttk, N, S, NS, E, W, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from PantryShelves import lista_do_przepisu
from LenList import len_all_pantry, name_all_pantry


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
        self.recipe_diner.grid(columnspan=3, row=0, sticky="ew")

    def title_contener_diner_list(self):

        self.component = ttk.Label(self.recipe_diner, text="Test położenia II \n kontenera z przepisem na obiad", background="lightblue")
        self.component.grid(columnspan=3, row=1, sticky="ew")


    def all_list_out(self):

        #Tytuł tabelki

        quty_label_title = ttk.Label(self.recipe_diner, text="nazwa produktu", background="green")
        quty_label_title.grid(column=1, row=3, sticky="ew")

        quty_name_title = ttk.Label(self.recipe_diner, text="ilość szt", background="green")
        quty_name_title.grid(column=0, row=3, sticky="ew")

        #Pętla przeszukiwania danych.
        num6 = 4
        for x, y in lista_do_przepisu.items():

            if y != "0":
                quty_name = ttk.Label(self.recipe_diner, text=f"{y} szt.")
                quty_name.grid(column=0, row=num6)

                quty_label = ttk.Label(self.recipe_diner, text=x)
                quty_label.grid(column=1, row=num6)

            num6 +=1
        else:
            print(f"działa funkcja all_list_out {lista_do_przepisu}")
            num6 +=1

            self.buttom_update = ttk.Button(self.recipe_diner, text="odświerz bazę danych")
            self.buttom_update.grid(columnspan=3, row=num6, sticky='ew')
            self.buttom_update.configure(command=self.db_pantry_update)




    def db_pantry_update(self):
        print("up date DB")
        print(len_all_pantry)
        print(name_all_pantry)

        for x in len_all_pantry:
            print(x)


        # for x, y in lista_do_przepisu.items():
        #
        #     if y != "0":
        #         print(f"zmiana o {y}")
        #         print(f"dla towaru {x}")

            # self.stan = all_db_pantry[x[3]]
            # print(f"stana magazynu {self.stan}")
            # print(self.stan)
            # self.new_stan = int(self.stan) - int(y)
            # print(f'stan obecny magazynu: {all_db_pantry[x][3]}   ==> {[y]}')
            # print(f'f wyciągnięto z magazynu: {lista_do_przepisu[x]}  ==>  {y} ')
        # print(f' stan obecne magazynu {name_all_pantry[index]} ==> {new_stan}')
        # pantry_cursor.execute(f"update products_items set quantity = {new_stan} where id ={index+1}")
        # pantry_db.commit()


    def list_approval_button(self):

        self.buttom_ingra = ttk.Button(self.recipe_diner, text="zaciąganie listy")
        self.buttom_ingra.grid(columnspan=3, row=2, sticky='ew')
        self.buttom_ingra.configure(command=self.all_list_out)
