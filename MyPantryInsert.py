from tkinter import *
from tkinter import ttk, N, S, NS, CENTER
import mysql.connector

root = Tk()
root.title("test bazy danych")
root.geometry("400x215")

path = open("lokalhost_entry.txt", "r")
pass_path = path.read()
print(pass_path)

mydb = mysql.connector.connect(pass_path)

my_cursor = mydb.cursor()

def clear_filed():
    name_product_box.delete(0,END)
    unit_of_measure_box.delete(0,END)
    quantity_box.delete(0,END)
    seftystock_box.delete(0,END)

def insert_product():
    sql_command = "INSERT INTO mypantry.products_items (name_product, unit_of_measure, quantity, seftystock) VALUES (%s, %s, %s, %s)"
    values = (name_product_box.get(), unit_of_measure_box.get(), quantity_box.get(), seftystock_box.get())
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear_filed()


title_label = Label(root, text="Baza danych produktów")
title_label.grid(row=0, column=1, padx=5, pady=25)

name_product = Label(root, text="Nazwa produktu : ")
name_product.grid(row=1, column=0, padx=5)

name_product_box = Entry(root)
name_product_box.grid(row=1, column=1, padx=5)

unit_of_measure = Label(root, text="Jednostka miary : ")
unit_of_measure.grid(row=2, column=0, padx=5)

unit_of_measure_box = Entry(root)
unit_of_measure_box.grid(row=2, column=1, padx=5)

quantity = Label(root, text="Ilość wprowadzana : ")
quantity.grid(row=3, column=0, padx=5)

quantity_box = Entry(root)
quantity_box.grid(row=3, column=1, padx=5)

seftystock = Label(root, text="Bezpieczna ilość : ")
seftystock.grid(row=4, column=0, padx=5)

seftystock_box = Entry(root)
seftystock_box.grid(row=4, column=1, padx=5)

button_insert = Button(root, text="Insert product", command=insert_product)
button_insert.grid(row=5, column=1, pady=15)


clear_filds_buttom = Button(root, text="clean firld", command=clear_filed)
clear_filds_buttom.grid(row=5, column=2, padx=15, pady=15)


my_cursor.execute("select name_product from mypantry.products_items where id = 4")
result = my_cursor.fetchall()

print(result)

for x in result:
    print(x)


root.mainloop()
