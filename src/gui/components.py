import tkinter as tk

def create_text_box(parent, height, width):
  return tk.Text(parent, height=height, width=width)

def create_button(parent, text, command):
  return tk.Button(parent, text=text, command=command).pack()

def create_radio_buttons(parent, label_text, options, variable):
  tk.Label(parent, text=label_text).pack()
  for option in options:
      tk.Radiobutton(parent, text=option, variable=variable, value=option.split()[0]).pack()