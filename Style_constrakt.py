from tkinter import ttk, N, S, E, NS, CENTER
import tkinter as tk
import tkinter.font as font

def style_constrakt():

    style_main = ttk.Style()
    style_main.theme_use("alt")
# style pisane ręcznie

    colour_paper = "#FFFFFF"
    colour_char_hand = "#1E6ADE"

    style_main.configure("titile_frame_handwritten.TLabel",
                                  anchor=CENTER,
                                  background=colour_paper,
                                  foreground=colour_char_hand,
                                  font=("Ink Free", 17, "bold", "underline"))

    style_main.configure("column_style_handwritten.TLabel",
                                  anchor=CENTER,
                                  background=colour_paper,
                                  foreground=colour_char_hand,
                                  font=("Ink Free", 15, "bold"))

    style_main.configure("span_style_handwritten.TLabel",
                                  anchor=CENTER,
                                  background=colour_paper,
                                  foreground=colour_char_hand,
                                  font=("Ink Free", 20,))
    style_main.configure("button_style_handwritten.TButton",
                                  anchor=CENTER,
                                  background=colour_paper,
                                  foreground=colour_char_hand,
                                  font=("Ink Free", 12))

# style pisane komputerowo

    colour_label = "#FFE918"
    colour_label_title = "#FFB13C"
    colour_char_komp = "#3D2705"

    style_main.configure("column_style_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label_title,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 15))

    style_main.configure("span_style_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 13))

    style_main.configure("button_style_os.TButton",
                                  anchor=CENTER,
                                  background=colour_label_title,
                                  foreground=colour_char_komp,
                                  font=("Courier New", 12))

    style_main.configure("info_style_os.TLabel",
                                  anchor=CENTER,
                                  background=colour_label,
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
                        foreground="black",
                        font=("Courier New", 13))


