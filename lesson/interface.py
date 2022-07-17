import tkinter as tk
from app import *

class Interface():
  def __init__(self, master):
    self.master = master
    self.root = master
    self.master.title('add')
    self.master.geometry('+50+50')
    self.master.wm_attributes("-topmost", 1)

    # button start
    self.btn_test = tk.Button(self.master, text="Start", font=('Roboto', 30, 'bold'), relief=tk.FLAT, bg='white', fg='#F8DE5C')
    self.btn_test.bind('<Button-1>', self.start_app)
    self.btn_test.grid(row=0, column=0)

    # start
    self.master.mainloop()

  def start_app(self, event):
    App(self.master)


# create a new window
root = tk.Tk()
# start window
Interface(root)