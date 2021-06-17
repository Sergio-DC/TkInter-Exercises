from tkinter import *
from tkinter.ttk import * #Gives a different appeareance to widgets if we let this line
root = Tk() # Is like a scaffold
label = Label(root, text="Hello World")# Widgets, this widget won't be invoked because it does not invoke pack()
button = Button(root, text="touch me")
entry = Entry(root, text="Write something")
button.pack()# Don't forget to invoke pack() to render the widget
entry.pack()
root.mainloop()



print("Hola :)")
