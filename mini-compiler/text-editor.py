import tkinter as tk
from tkinter import ttk, filedialog
import io
import lexer

class MenuBar(tk.Menu):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)
		self.parent = parent
		self.initializeGUI()
	def initializeGUI(self):
		self.add('command', label='Open', command=self.onOpenFile)
		self.add('command', label='Save', command=self.onSaveFile)
		self.add('command', label='Compile', command=self.compile)
		self.add('command', label='Quit', command=self.quit)

		#frameTextEditor = tk.Frame(root)
		#frameTextEditor.config(bg="blue", width="800", height="600")
		#frameTextEditor.pack()

	def onOpenFile(self):    
		"""Handle the file->select action from the menu"""    
		textFile = filedialog.askopenfile(
			title='Select the target file for saving records', 
			defaultextension='.txt',
			filetypes=[('TXT Files', '*.txt')]
			)
		sourceCode = textFile.read()
		self.parent.textEditor.insert(tk.END, sourceCode)

	def onSaveFile(self):
		textFile = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
		sourceCode = self.parent.textEditor.get("1.0", "end")
		print("SourceCode: ", sourceCode)
		textFile.write(sourceCode)
		print("File written")


	def compile(self):
		status = "Success"
		sourceCode = self.parent.textEditor.get("1.0", "end")
		print("Holaaa")
		lexer.test(sourceCode)
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