import tkinter as tk
from tkinter import ttk, PhotoImage


root = tk.Tk()

# PNG image path
img_canada_flag = PhotoImage(file=r"ProyectoFinalProgramacion1/imagen/estrella.png")

# Define columns
column_names = ("country_column", "capital_city_column")

# Pass the column names when we make the treeview.
treeview_country = ttk.Treeview(columns=column_names)

# Create the column texts that the user will see.
treeview_country.heading("country_column", text="Country")
treeview_country.heading("capital_city_column", text="Capital")

treeview_country.insert(parent="",
                        index="end",
                        image=img_canada_flag,
                        values=("Canada", "Ottawa"))
treeview_country.column("#0", width=75)
treeview_country.pack(expand=True, fill=tk.BOTH)

root.mainloop()
