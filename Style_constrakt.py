from tkinter import ttk, CENTER
# docelowy zestaw kolorów

colour_label_title = "#DAA520" #złoty pręt
colour_label_column = "#B8860B" #ciemnozłoty pręt
colour_label_verse = "#EEE8AA" # bladozłoty pręt

colour_background = "#DCDCDC" # Gainsboro
colour_board = "#F5F5DC" #beżowy
colour_buttom = "#FFFFE0" #asny zółty

colour_letter_comp = "#556B2F" #ciemnozielony oliwkowy
colour_letter_board = "#191970"

def style_constrakt():

    style_main = ttk.Style()
    style_main.theme_use("alt")

    style_main.configure(
        "title.TLabel",
        anchor=CENTER,
        background=colour_label_title,
        foreground=colour_letter_board,
        padding=(2, 2),
        font=("Courier New", 20),
    )

    style_main.configure(
        "column.TLabel",
        anchor=CENTER,
        background=colour_label_column,
        foreground="white",
        font=("Courier New", 13),
        padding=2,
    )

    # relief: "flat", "raised","sunken","groove", "ridge".
    style_main.configure(
        "verse.TLabel",
        anchor=CENTER,
        background=colour_label_verse,
        foreground=colour_letter_board,
        font=("Courier New", 13),
        padding=2,
    )

    style_main.configure(
        "background.TLabel",
        anchor=CENTER,
        background=colour_background,
        foreground=colour_letter_board,
        font=("Courier New", 13),
        padding=(0,3,0,3),
    )

    style_main.configure(
        "button.TButton",
        anchor=CENTER,
        background=colour_buttom,
        font=("Courier New", 12),
        relief="flat",
    )
    style_main.map(
        "button.TButton",
        background=[('active', colour_buttom), ('pressed', 'read')],
        foreground=[('active', colour_letter_board), ('pressed', 'yellow')],
    )



