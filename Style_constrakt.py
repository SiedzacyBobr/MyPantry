from tkinter import ttk, N, S, E, NS, CENTER

colour_label_title = "silver"
colour_label_column = "lightblue"
colour_label_span = "lightgray"
colour_char_komp = "Black"

colour_paper_hand = "White"
colour_char_hand = "darkblue"

def style_constrakt():

    style_main = ttk.Style()
    style_main.theme_use("vista")

    style_main.configure("titile_frame_handwritten.TLabel",
                         anchor=CENTER,
                         background=colour_paper_hand,
                         foreground=colour_char_hand,
                         font=("Ink Free", 17, "bold", "underline"))

    style_main.configure("column_style_handwritten.TLabel",
                         anchor=CENTER,
                         background=colour_paper_hand,
                         foreground=colour_char_hand,
                         font=("Ink Free", 15, "bold"))

    style_main.configure("span_style_handwritten.TLabel",
                         anchor=CENTER,
                         background=colour_paper_hand,
                         foreground=colour_char_hand,
                         font=("Ink Free", 13,))
    style_main.configure("button_style_handwritten.TButton",
                         anchor=CENTER,
                         background=colour_paper_hand,
                         foreground=colour_char_hand,
                         font=("Ink Free", 12))

    style_main.configure("checkbutton_style_handwritten.TCheckbutton",
                         background=colour_paper_hand, width=0, )


    style_main.configure("column_style_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label_column,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 15))

    style_main.configure("span_style_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label_span,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 13))

    style_main.configure("button_style_os.TButton",
                                  anchor=CENTER,
                                  background=colour_label_column,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 12))


    style_main.configure("info_style_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label_span,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 15))

    style_main.configure("titile_frame_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label_title,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 17))

    style_main.configure("Main_title_frame_os.TLabel",
                        justify= "center",
                        background="White",
                        foreground="Black",
                        font=("Courier New", 13)
                        )



