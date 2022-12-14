import tkinter as tk
from tkinter import ttk, filedialog, CENTER
import mysql.connector
from lokalhost_entry import passwd, user_pantry
from Style_constrakt import colour_paper_hand, colour_char_hand
import win32print, win32api



class ShoppingList(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.schoping_list = {}
        self.list_chack_box_botton = {}
        self.list_spin_box_botton = {}
        self.done_schoping = {}

        self.done_load_db()
        self.main_frame_for_the_shopping_list()
        self.scroll_bar_canvas()
        self.main_frame_title_shopping_list()
        self.name_column_shopping_list()
        self.interactive_shoppnig_list()
        self.selection_list_approval_button()


    def done_load_db(self):
        self.pantry_db = mysql.connector.connect(
            host="localhost",
            user=user_pantry,
            passwd=passwd,
            database="mypantry",
        )
        self.pantry_cursor = self.pantry_db.cursor()

        self.pantry_cursor.execute("select * from mypantry.products_items")
        self.all_db_pantry = self.pantry_cursor.fetchall()

    def main_frame_for_the_shopping_list(self):

        self.shop_list = tk.Frame(
            self,
            background=colour_paper_hand,
            borderwidth=1,
            relief="solid",
            width=691,
            height=450,
            padx=10,
            pady=10,
        )
        self.shop_list.pack()
        self.shop_list.pack_propagate(0)

    def scroll_bar_canvas(self):
        self.canvas_test = tk.Canvas(self.shop_list, background=colour_paper_hand)

        self.scrollable_frame = tk.Frame(self.canvas_test, background=colour_paper_hand)

        self.scroll_bar = ttk.Scrollbar(
            self.shop_list,
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
                    self.scrollable_frame,
                    text="Lista Zakup??w ",
                    style="titile_frame_handwritten.TLabel",
                    width=46,
                )
                self.items_products.grid(columnspan=4, row=0, sticky="EW")
                len_products_to_shopping_list +=1

        if len_products_to_shopping_list == 0:
            self.no_shopping_list = ttk.Label(
                self.scrollable_frame,
                text="Brak listy zakup??w \n - w spi??arni niczego nie brakuje",
                style="titile_frame_handwritten.TLabel",
                width=46,
            )
            self.no_shopping_list.grid(columnspan=4, row=0, sticky="EW")

    def name_column_shopping_list(self):

        for x in self.all_db_pantry:
            if x[4] > x[3]:

                self.first_kolumn_list_b = ttk.Label(
                    self.scrollable_frame,
                    text="Zaznacz",
                    style="column_style_handwritten.TLabel",
                )

                self.first_kolumn_list = ttk.Label(
                    self.scrollable_frame,
                    text="Produkt",
                    style="column_style_handwritten.TLabel",
                )

                self.second_kolumn_list = ttk.Label(
                    self.scrollable_frame,
                    text="Jednostka",
                    style="column_style_handwritten.TLabel",
                )

                self.third_kolumn_list = ttk.Label(
                    self.scrollable_frame,
                    text="Ilo????",
                    style="column_style_handwritten.TLabel",
                )
                self.first_kolumn_list_b.grid(column=0, row=1, sticky="EW")
                self.first_kolumn_list.grid(column=1, row=1, sticky="EW")
                self.second_kolumn_list.grid(column=2, row=1, sticky="EW")
                self.third_kolumn_list.grid(column=3, row=1, sticky="EW")

    def interactive_shoppnig_list(self):
        shopping_list_to_do = open('shopping_list.txt', 'w')
        shopping_list_to_do.write("Lista zakup??w do zrealizowania \n ")
        shopping_list_to_do.write("Nazwa produktu i ilo???? szt. \n")

        poz = 1
        num10 = 25
        for x in self.all_db_pantry:

            self.selected_option = tk.IntVar(value=None)
            self.testing_chack_buttom = tk.Checkbutton(
                self.scrollable_frame,
                variable=self.selected_option,
                onvalue=1,
                offvalue=0,
                background=colour_paper_hand,
                relief="flat"

                )

            self.name_product_label = ttk.Label(
                self.scrollable_frame,
                text=x[1],
                style="span_style_handwritten.TLabel",
            )

            self.unit_of_measure = ttk.Label(
                self.scrollable_frame,
                text=x[2],
                style="span_style_handwritten.TLabel",
            )

            self.quantity_items = tk.IntVar(value=x[4] - x[3])
            self.spin_box = tk.Spinbox(
                self.scrollable_frame,
                width=5,
                from_=0,
                to=30,
                textvariable=self.quantity_items,
                justify="center",
                font=("Ink Free", 15),
                foreground=colour_char_hand,
                background=colour_paper_hand,
                borderwidth=2,
                relief="sunken",
            )

            if x[4] > x[3]:
                self.testing_chack_buttom.grid(column=0, row=num10)
                self.name_product_label.grid(column=1, row=num10)
                self.unit_of_measure.grid(column=2, row=num10)
                self.spin_box.grid(column=3, row=num10)

            self.list_spin_box_botton[x[1]] = self.quantity_items
            self.list_chack_box_botton[x[1]] = self.selected_option

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

                print(f'spe??niony warunek dla {name_s} i warto??ci {volue_s}')

                self.guantity_s = self.list_spin_box_botton[name_s]

                if self.guantity_s > 0:

                    print(f"Kupiono {name_s} ilo???? {self.guantity_s} rozpoczynamy p??tle for dla all_db_pantry")

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
                        f"update products_items set quantity = {self.new_state_s} where id ={self.shoping_index}")
                    self.pantry_db.commit()

            else:
                print(f"warunek nie spe??niony dla {name_s}")

        self.printing_a_completed_shopping_list()
        self.shop_list.destroy()
        self.pantry_db.close()
        self.done_load_db()
        self.main_frame_for_the_shopping_list()
        self.scroll_bar_canvas()
        self.main_frame_title_shopping_list()
        self.name_column_shopping_list()
        self.interactive_shoppnig_list()
        self.selection_list_approval_button()


    def selection_list_approval_button(self):
        for x in self.all_db_pantry:
            if x[4] > x[3]:

                self.action_buttom = ttk.Button(
                    self.shop_list,
                    text=f"zakupy zrobione i przyniesione sklep ==> spi??arnia",
                    style="button_style_handwritten.TButton",
                )
                self.action_buttom.pack(side="right", expand=True, fill="x")
                self.action_buttom.configure(command=self.chack_box_print_list)

                self.buttom_print = ttk.Button(
                    self.shop_list,
                    text="Drukuj list?? zakup??w",
                    style="button_style_handwritten.TButton",

                )
                self.buttom_print.pack(side="left", expand=True, fill="x")
                self.buttom_print.configure(command=self.pritnt_list)
                break

    def printing_a_completed_shopping_list(self):

        self.top_window_shopping = tk.Toplevel()
        self.top_window_shopping.title("Lista zrobionych zokup??w")

        print(f' lista wykreawana do print done shoppping {self.done_schoping}')

        self.completed_shopping_list = tk.Frame(
            self.top_window_shopping,
            background=colour_paper_hand,
            borderwidth=1,
            relief="solid",
        )
        self.completed_shopping_list.grid(column=2, row=0)

        self.title_done_schoping = ttk.Label(
            self.completed_shopping_list,
            text="Zakupy przeniesione \n z Sklepu do Spi??arni",
            style="titile_frame_handwritten.TLabel",
            width=45,
        )

        self.first_kolumn_done_schoping = ttk.Label(
            self.completed_shopping_list,
            text="Nazwa produktu",
            style="column_style_handwritten.TLabel",
        )

        self.second_kolumn_done_schoping = ttk.Label(
            self.completed_shopping_list,
            text="Ilo???? szt.",
            style="column_style_handwritten.TLabel",
        )
        self.title_done_schoping.grid(columnspan=2, row=0, sticky="EW")
        self.first_kolumn_done_schoping.grid(column=0, row=1, sticky="EW")
        self.second_kolumn_done_schoping.grid(column=1, row=1, sticky="EW")

        num1 = 2
        for name, value in self.done_schoping.items():

            self.neme_done_shoping = ttk.Label(
                self.completed_shopping_list,
                text=name,
                style="span_style_handwritten.TLabel",
            )

            self.value_done_shoping = ttk.Label(
                self.completed_shopping_list,
                text=f'{value} szt.',
                style="span_style_handwritten.TLabel",
            )
            self.neme_done_shoping.grid(column=0, row=num1)
            self.value_done_shoping.grid(column=1, row=num1)

            num1 += 1

    def pritnt_list(self):

        printer_name = win32print.GetDefaultPrinter()
        print(printer_name)
        
        file_to_print = filedialog.askopenfilename(
            initialdir="/ shopping_list.txt",
            title="Pi??kny tutu?? dla okna drukowania",
            initialfile="shopping_list.txt"
        )
        if file_to_print:
            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
