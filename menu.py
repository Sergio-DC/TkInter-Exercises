import tkinter as tk

root = tk.Tk()
font_bold = tk.BooleanVar(root)
font_size = tk.IntVar()

def set_font(*args):
	font_spec = 'TkDefaultFont {size} {bold}'.format(size=font_size.get(), bold='bold' if font_bold.get() else '')
	label.config(font=font_spec)

font_bold.trace('w', set_font)
font_size.trace('w', set_font)



main_text = tk.StringVar(value='Hi')
label = tk.Label(root, textvariable=main_text)
label.pack()
main_menu = tk.Menu(root) # Main menu toolbar
root.config(menu=main_menu)
main_menu.add('command', label='Quit', command=root.quit)
text_menu = tk.Menu(main_menu, tearoff=False) # Sub-menu, pre attaching the submenu to Main menu
text_menu.add_command(label='Set to "Hi"', command=lambda: main_text.set('Hi')) # Menu items
text_menu.add_command(label='Set to "There"', command=lambda: main_text.set('There'))# Menu items

main_menu.add_cascade(label="Text", menu=text_menu)# Attaching the submenu to Main Menu 

# appearance menu
appearance_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Appearance", menu=appearance_menu)
# bold text button
appearance_menu.add_checkbutton(label="Bold", variable=font_bold)

root.mainloop()
