#!/user/bin/env python
from Tkinter import *
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
	    tk.Frame.__init__(self,master)
            self.grid()
            self.createWidgets()
		
    def createWidgets(self):
	    self.quitButton = tk.Button(self,text='Quit',command=self.quit)
	    self.quitButton.grid()
		
	    self.Textbox = tk.Text(self)
	    self.Textbox.grid()
            Text = (self.Textbox.get(1.0))
	    
	    self.saveButton = tk.Button(self,text='Save',command=textsave)
	    self.saveButton.grid()
		
	      		
            
def textsave():
     T = str(Text)
     Mydairy=open("dairy",'a+')
     Mydairy.write("\n")
     Mydairy.write(T)
	 
		
		
app = Application()
app.master.title('My Dairy')
app.mainloop()