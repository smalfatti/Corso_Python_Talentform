#scrivere una interfaccia grafica che ha due entry, un bottone e una etichetta.
# il programma chiede di inserire due numeri e
# modifica il testo dell'etichetta con la somma dei due numeri.
# Attenzione: il metodo get() delle entry ritorna una stringa quindi è necessario fare il cast
# la som a viene restituita alla pressione del pulsante

import tkinter as tk

def calcola_somma():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    somma = num1 + num2
    etichetta.config(text="La somma è: " + str(somma))

root = tk.Tk()

label1 = tk.Label(root, text="Primo numero:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Secondo numero:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Calcola somma", command=calcola_somma)
button.pack()

etichetta = tk.Label(root, text="")
etichetta.pack()

root.mainloop()