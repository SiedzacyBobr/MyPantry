from tkinter import *
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector

root = Tk()
root.title("test bazy danych")
root.geometry("600x215")

path = open("lokalhost_entry.txt", "r")
pass_path = path.read()
print(pass_path)

mydb = mysql.connector.connect()

my_cursor = mydb.cursor()

def list_items():
    my_cursor.execute("select quantity from mypantry.products_items where id = 2")
    result = my_cursor.fetchall()
    lookup_label = Label(root, text=result)
    lookup_label.grid(row=4, column=1)




title_label = Label(root, text="Pozystkanie danych")
title_label.grid(row=0, column=1, padx=5, pady=25)

idnum = 3


my_cursor.execute(f"select name_product from mypantry.products_items where id = {idnum}")
name = my_cursor.fetchall()
lookup_label = Label(root, text=name)
lookup_label.grid(row=1, column=1)

my_cursor.execute(f"select quantity from mypantry.products_items where id = {idnum}")
qty = my_cursor.fetchall()
lookup_label = Label(root, text=f"stan w magazynie:  {qty}")
lookup_label.grid(row=1, column=2)

my_cursor.execute(f"select seftystock from mypantry.products_items where id = {idnum}")
sefyt = my_cursor.fetchall()
lookup_label = Label(root, text=f" poziom bezpieczny:  {sefyt}")
lookup_label.grid(row=1, column=3)


name_product = Label(root, text="Stan w magazynie : ")
name_product.grid(row=1, column=0, padx=5)


list_product = Button(root, text="Wyświetl dane ", command=list_items)
list_product.grid(row=5, column=1, pady=15)


root.mainloop()
