import tkinter as tk
from tkinter import ttk, filedialog, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import colour_background, colour_label_verse, colour_board, colour_letter_board, colour_letter_comp
import win32print, win32api


class ShoppingList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.schoping_list = {}
        self.list_chack_box_botton = {}
        self.list_spin_box_botton = {}
        self.done_schoping = {}

        self.shop_list_window = tk.Frame(
            self,
            background=colour_background,
            borderwidth=1,
            relief="solid",
            width=691,
            height=450,
            padx=10,
            pady=10,
        )

        self.title_column_end_action = tk.Frame(
            self.shop_list_window,
            background=colour_background,
        )
        self.shoping_is_dane = tk.Frame(
            self.shop_list_window,
            background=colour_background,
        )
        self.shoping_list_todo = tk.Frame(
        self.shop_list_window,
        background=colour_board,
        )

        self.shop_list_window.grid(column=0, row=0)
        self.shop_list_window.pack_propagate(0)
        self.title_column_end_action.grid(column=0, row=1)
        self.shoping_list_todo.grid(column=0, row=3)
        self.shoping_is_dane.grid(column=0, row=2)

        self.done_load_db()
        self.scroll_bar_canvas()
        self.main_frame_title_shopping_list()
        self.name_column_shopping_list()
        self.interactive_shoppnig_list()

    def done_load_db(self):
        self.pantry_db = mysql.connector.connect(
            host="localhost",
            user=user_pantry,
            passwd=passwd,
            database="mypantry",
        )
        self.pantry_cursor = self.pantry_db.cursor()

        self.pantry_cursor.execute("select * from mypantry.home_pantry_products")
        self.all_db_pantry = self.pantry_cursor.fetchall()


    def scroll_bar_canvas(self):
        self.canvas_test = tk.Canvas(
            self.shoping_list_todo,
            background=colour_label_verse,
            width=450,
        )

        self.scrollable_frame = tk.Frame(
            self.canvas_test,
            background=colour_label_verse,
        )

        self.scroll_bar = ttk.Scrollbar(
            self.shoping_list_todo,
            orient="vertical",
            command=self.canvas_test.yview
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas_test.configure(scrollregion=self.canvas_test.bbox("all")))

        self.canvas_test.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas_test.configure(yscrollcommand=self.scroll_bar.set)

        self.scroll_bar.pack(side="right", fill="y")
        self.canvas_test.pack(side="top", fill="both", expand=True)


    def main_frame_title_shopping_list(self):
        len_products_to_shopping_list = 0
        for x in self.all_db_pantry:
            if x[4] > x[3]:

                self.items_products = ttk.Label(
                    self.title_column_end_action,
                    text="Lista Zakupów do zrealizawania",
                    style="title.TLabel",
                    width=40,
                )
                self.items_products.grid(columnspan=3, row=0, sticky="EW")
                len_products_to_shopping_list +=1

        if len_products_to_shopping_list == 0:
            self.no_shopping_list = ttk.Label(
                self.title_column_end_action,
                text="Brak listy zakupów \n - w spiżarni niczego nie brakuje",
                style="title.TLabel",
                width=40,
            )
            self.no_shopping_list.grid(columnspan=3, row=0, sticky="EW")

    def name_column_shopping_list(self):

        for x in self.all_db_pantry:
            if x[4] > x[3]:

                self.description_button = ttk.Label(
                    self.title_column_end_action,
                    text="Czy chcesz wydrukować listę zaków ?  ",
                    style="background.TLabel",
                    padding=(0,7,0,7)
                )

                self.buttom_print = ttk.Button(
                    self.title_column_end_action,
                    text="Drukuj listę zakupów",
                    style="button.TButton",


                )
                self.buttom_print.configure(command=self.pritnt_list)

                self.first_kolumn_list = ttk.Label(
                    self.shoping_is_dane,
                    text="Produkt",
                    style="column.TLabel",
                    width=20,

                )

                self.second_kolumn_list = ttk.Label(
                    self.shoping_is_dane,
                    text="Jednostka",
                    style="column.TLabel",
                    width=10,

                )

                self.third_kolumn_list = ttk.Label(
                    self.shoping_is_dane,
                    text="Ilość",
                    style="column.TLabel",
                    width=15,

                )
                self.description_button.grid(columnspan=2, row=1, sticky="w")
                self.buttom_print.grid(column=2, row=1, sticky="e")
                self.first_kolumn_list.grid(column=0, row=2)
                self.second_kolumn_list.grid(column=1, row=2)
                self.third_kolumn_list.grid(column=2, row=2)

    def interactive_shoppnig_list(self):
        shopping_list_to_do = open('shopping_list.txt', 'w')
        shopping_list_to_do.write("Lista zakupów do zrealizowania \n ")
        shopping_list_to_do.write("Nazwa produktu i ilość szt. \n")

        poz = 1
        num10 = 25
        for x in self.all_db_pantry:

            self.name_product_label = ttk.Label(
                self.scrollable_frame,
                text=x[1],
                style="verse.TLabel",
                width=20,
            )

            self.unit_of_measure = ttk.Label(
                self.scrollable_frame,
                text=x[2],
                style="verse.TLabel",
                width=10,
            )

            self.spin_box = ttk.Label(
                self.scrollable_frame,
                text=x[4] - x[3],
                style="verse.TLabel",
                width=10,
                anchor=CENTER,
            )

            if x[4] > x[3]:

                self.name_product_label.grid(column=0, row=num10)
                self.unit_of_measure.grid(column=1, row=num10)
                self.spin_box.grid(column=2, row=num10)

            num10 += 1
            if x[4] > x[3]:
                shopping_list_to_do.write(f' {poz}  {x[1]} - {x[4]-x[3]} .szt \n')
                poz += 1

        shopping_list_to_do.close()

    def chack_box_print_list(self):

        for name, value in self.list_chack_box_botton.items():
            self.selected_op = value.get()
            self.list_chack_box_botton[name] = self.selected_op

        for name, value in self.list_spin_box_botton.items():
            self.selected_sp = value.get()
            self.list_spin_box_botton[name] = self.selected_sp

        for name_s, volue_s in self.list_chack_box_botton.items():

            if volue_s == 1 and name_s in self.list_spin_box_botton:

                print(f'spełniony warunek dla {name_s} i wartości {volue_s}')

                self.guantity_s = self.list_spin_box_botton[name_s]

                if self.guantity_s > 0:

                    print(f"Kupiono {name_s} ilość {self.guantity_s} rozpoczynamy pętle for dla all_db_pantry")

                    self.schoping_list[name_s] = self.guantity_s

                    for x in self.all_db_pantry:
                        if x[1] == name_s:
                            self.shoping_index = x[0]
                            self.state_s = x[3]
                            self.new_state_s = int(self.state_s) + int(self.guantity_s)

                            if name_s not in self.done_schoping:
                                self.done_schoping[name_s] = self.guantity_s
                            else:
                                self.done_schoping[name_s] += self.guantity_s

                    self.pantry_cursor.execute(
                        f"update home_pantry_products set quantity = {self.new_state_s} where id ={self.shoping_index}")
                    self.pantry_db.commit()

            else:
                print(f"warunek nie spełniony dla {name_s}")

        self.printing_a_completed_shopping_list()
        self.shop_list_window.destroy()
        self.pantry_db.close()
        self.done_load_db()
        self.scroll_bar_canvas()
        self.main_frame_title_shopping_list()
        self.name_column_shopping_list()
        self.interactive_shoppnig_list()


    def printing_a_completed_shopping_list(self):

        self.top_window_shopping = tk.Toplevel()
        self.top_window_shopping.title("Lista zrobionych zokupów")

        print(f' lista wykreawana do print done shoppping {self.done_schoping}')

        self.completed_shopping_list = tk.Frame(
            self.top_window_shopping,
            background=colour_label_verse,
        )
        self.completed_shopping_list.grid(column=2, row=0)

        self.title_done_schoping = ttk.Label(
            self.completed_shopping_list,
            text="Zakupy przeniesione \n z Sklepu do Spiżarni",
            style="title.TLabel",
            width=45,
        )

        self.first_kolumn_done_schoping = ttk.Label(
            self.completed_shopping_list,
            text="Nazwa produktu",
            style="column.TLabel",
        )

        self.second_kolumn_done_schoping = ttk.Label(
            self.completed_shopping_list,
            text="Ilość szt.",
            style="column.TLabel",
        )
        self.title_done_schoping.grid(columnspan=2, row=0, sticky="EW")
        self.first_kolumn_done_schoping.grid(column=0, row=1, sticky="EW")
        self.second_kolumn_done_schoping.grid(column=1, row=1, sticky="EW")

        num1 = 2
        for name, value in self.done_schoping.items():

            self.neme_done_shoping = ttk.Label(
                self.completed_shopping_list,
                text=name,
                style="verse.TLabel",
            )

            self.value_done_shoping = ttk.Label(
                self.completed_shopping_list,
                text=f'{value} szt.',
                style="verse.TLabel",
            )
            self.neme_done_shoping.grid(column=0, row=num1)
            self.value_done_shoping.grid(column=1, row=num1)

            num1 += 1

    def pritnt_list(self):

        printer_name = win32print.GetDefaultPrinter()
        print(printer_name)
        
        file_to_print = filedialog.askopenfilename(
            initialdir="/ shopping_list.txt",
            title="Piękny tutuł dla okna drukowania",
            initialfile="shopping_list.txt"
        )
        if file_to_print:
            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
