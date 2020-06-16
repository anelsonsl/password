import tkinter as tk

janela = tk.Tk() #Cria uma window

#Mensagems na Janela
m1 = tk.Label(text="Texto normal")
m1.pack()

#Botoes
b1 = tk.Button(
    text="Clica",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
b1.pack()

#Inserir valores
t_val1 = tk.Label(text="Nome")
ent1 = tk.Entry()
t_val1.pack()
ent1.pack()

janela.mainloop()