from tkinter import *
from tkinter.ttk import *

# writing code needs to
# create the main window of
# the application creating
# main window object named root
root = Tk()

# giving title to the main window
root.title("Corso Talentform")

# Label is what output will be
# show on the window
label = Label(root, text="Ciao MONDOOOOO !").pack()

# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
root.mainloop()