import tkinter as tk
from SysAriTest import *



class App():
  def __init__(self, master):
    self.master = master
    self.root = master
    self.master.title('add')
    self.master.geometry('+50+50')
    self.master.wm_attributes("-topmost", 1)

    self.lbl = tk.Label(self.master, font=15)

    # button ADD
    self.btn_add = tk.Button(self.master, text="Test", font=('Roboto', 30, 'bold'), relief=tk.FLAT, bg=bg_main, fg='blue')
    self.btn_add.bind('<Button-1>', self.open_SysAriTest)
    self.btn_add.grid(row=0, column=0)

    # start
    self.master.mainloop()

  def open_SysAriTest(self, event):
    SysAriTest(self.master)

# create a new window
root = tk.Tk()
# start window
App(root)