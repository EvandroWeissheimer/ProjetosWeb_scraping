from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk

from main import get_product_ml

def montaTela():
    global selected_var

    root = tk.Tk()

    root.title("Web Scraping")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (731 / 2)
    y = (screen_height / 2) - (600 / 2)

    root.geometry('%dx%d+%d+%d' % (731, 600, x, y))

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, font=("Arial", 14, "bold"), text="Mandar WhatsApp\n", anchor="center").grid(column=1, row=1, sticky=tk.W)
    # ttk.Label(mainframe, font=("Arial", 10),  text="Informe ás empresas separadas por vírgula ','\n").grid(column=1, row=2, sticky=tk.W)

    global produto
    produto = ttk.Entry(mainframe)
    produto.grid(column=1, row=4, sticky=tk.EW)
    # ttk.Button(mainframe, text="Criar Contado",  command=telaCadastro).grid(column=1, row=7, sticky=tk.W)
    ttk.Button(mainframe, text="Merca Livre", command=get_product_ml).grid(column=1, row=5, sticky=tk.W)
    # ttk.Button(mainframe, text="Aliexpress",  command=enviarMensagem).grid(column=1, row=6, sticky=tk.W)
    ttk.Button(mainframe, text="Sair", command=root.destroy).grid(column=1, row=7, sticky=tk.W)

    root.mainloop()


def mercadoLivre():
    teste = produto.get()
    return teste
