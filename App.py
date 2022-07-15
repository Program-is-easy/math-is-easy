import tkinter as tk
from SysAriTest import *

class App():
  def __init__(self, master):
    self.master = master
    self.root = master
    self.master.title('add')
    self.master.geometry('+50+50')
    self.master.wm_attributes("-topmost", 1)

    # button test
    self.btn_test = tk.Button(self.master, text="Test", font=('Roboto', 30, 'bold'), relief=tk.FLAT, bg=bg_main, fg='#F8DE5C')
    self.btn_test.bind('<Button-1>', self.open_SysAriTest)
    self.btn_test.grid(row=0, column=0)

    # button training
    self.btn_training = tk.Button(self.master, text="Train", font=('Roboto', 30, 'bold'), relief=tk.FLAT, bg=bg_main, fg='#225695')
    self.btn_training.bind('<Button-1>', self.open_SysAriTrain)
    self.btn_training.grid(row=0, column=1)

    # start
    self.master.mainloop()

  def open_SysAriTest(self, event):
    SysAriTest(self.master)

  def open_SysAriTrain(self, event):
    SysAriTrain(self.master)

# create a new window
root = tk.Tk()
# start window
App(root)