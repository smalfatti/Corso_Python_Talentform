import tkinter as tk
r = tk.Tk()
r.title('Corso talent')
button = tk.Button(r, text='Talent', width=35, command=r.destroy)
button.pack()
r.mainloop()