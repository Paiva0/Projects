import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.title("To Do List")
window.geometry("300x400")

tasks = []

def atualizar_label():
    total = sum(var.get() for var, cb in tasks)
    label.config(text=f"fizeste {total} coisas")

def adicionar():
    texto = simpledialog.askstring("Nova tarefa", "Escreve a tarefa:")
    if texto:
        var = tk.IntVar()
        cb = tk.Checkbutton(window, text=texto, variable=var,
                            command=atualizar_label)
        cb.pack(anchor="w")
        tasks.append((var, cb))

def remover():
    for var, cb in tasks[:]:
        if var.get() == 1:
            cb.destroy()
            tasks.remove((var, cb))
    atualizar_label()

label = tk.Label(window, text="fizeste 0 coisas", bg="white", width=25)
label.pack(pady=10)

btn_add = tk.Button(window, text="Criar", command=adicionar)
btn_add.pack(pady=5)

btn_del = tk.Button(window, text="Delete", command=remover)
btn_del.pack(pady=5)

window.mainloop()