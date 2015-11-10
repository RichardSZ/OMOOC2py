#!/user/bin/env python
from Tkinter import *
import Tkinter as tk
  
class Application(tk.Frame):
    def __init__(self,master=None):
	    tk.Frame.__init__(self,master)
            self.grid()
            self.createWidgets()
		
    def createWidgets(self):
	        Text = StringVar()
		self.quitButton = tk.Button(self,text='Quit',command=self.quit)
		self.quitButton.grid()
		
		self.saveButton = tk.Button(self,text='Save',command=self.textsave)
		self.saveButton.grid()
		self.Textbox = tk.Text(self)
		self.Textbox.grid()
		
		self.quitButton.pack()
		self.saveButton.pack()
		self.Textbox.pack()
		 
    def textsave(self):    
         
         Mydairy=open("dairy",'a+')
         Mydairy.write(self.Textbox.get(1.0,END)+'\n')
         Mydairy.close()
'''	 	
def textsave():    
     tk.self.Textbox.get()
     Mydairy=open("dairy",'a+')
     Mydairy.write("\n")
     Mydairy.write(str(T))
'''
		
		
app = Application()
app.master.title('My Dairy')
app.mainloop()