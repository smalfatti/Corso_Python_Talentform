#scrivere una interfaccia grafica che ha due entry, un bottone e una etichetta.
# il programma chiede di inserire due numeri e
# modifica il testo dell'etichetta con la somma dei due numeri.
# Attenzione: il metodo get() delle entry ritorna una stringa quindi è necessario fare il cast
# la som a viene restituita alla pressione del pulsante

from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Esercizio somma")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text="Per favore inserisci due numeri")
lbl.grid()
Label(root, text='1° numero').grid(row=1)
Label(root, text='2° numero').grid(row=2)
lbl3 = Label(root)

lbl3.grid()

# adding Entry Field
txt1 = Entry(root, width=10)
txt1.grid(column=1, row=1)

txt2 = Entry(root, width=10)
txt2.grid(column=1, row=2)

lbl3.grid(column=1, row=5)



# function to display user text when
# button is clicked
def clicked():
    res = f"La somma è:  {int(txt1.get()) + int(txt2.get())}"
    lbl3.configure(text=res)


# button widget with red color text inside
btn = Button(root, text="Premi per sommare",
             fg="red", command=clicked)
# Set Button Grid
btn.grid(column=1, row=3)

# Execute Tkinter
root.mainloop()