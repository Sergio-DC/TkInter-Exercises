import tkinter as tk
from tkinter import ttk, filedialog
import io

class MenuBar(tk.Menu):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)
		self.parent = parent
		self.initializeGUI()
	def initializeGUI(self):
		self.add('command', label='Open', command=self.on_file_select)
		self.add('command', label='Save')
		self.add('command', label='Compile', command=self.compile)
		self.add('command', label='Quit', command=self.quit)

		#frameTextEditor = tk.Frame(root)
		#frameTextEditor.config(bg="blue", width="800", height="600")
		#frameTextEditor.pack()

	def on_file_select(self):    
		"""Handle the file->select action from the menu"""    
		fileText = filedialog.askopenfile(
			title='Select the target file for saving records', 
			defaultextension='.txt',
			filetypes=[('TXT Files', '*.txt')]
			)
		sourceCode = fileText.read()
		print(sourceCode)
		self.parent.textEditor.insert(tk.END, sourceCode)
	
	def compile(self):
		status = "Success"
		self.parent.textOutput.insert(tk.END, status)

class Application(tk.Tk):    
	"""Application root window"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.menuBar = MenuBar(self)
		self.textEditor = tk.Text(self, bg="black", fg="#45f542", insertbackground="#45f542",height=20)
		self.textOutput = tk.Text(self, bg="gray", height=8)
		self.textEditor.grid(row=0, column=0, sticky=tk.E+tk.W)
		self.textEditor.rowconfigure(0, weight=100)
		self.textEditor.columnconfigure(0, weight=100)
		self.textOutput.grid(row=1)
		self.resizable(False, False)
		self.resizable(False, False)
		self.config(menu=self.menuBar)

if __name__ == "__main__":
	app = Application()
	app.mainloop()