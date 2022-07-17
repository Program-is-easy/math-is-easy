import tkinter as tk
from test import *

class App():
  def __init__(self, master):
    # create children window
    self.slave = tk.Toplevel(master)
    self.slave.geometry('+50+150')
    self.slave.wm_attributes("-topmost", 1)

    # create main conteiner
    self.frm_main = tk.Frame(self.slave)
    self.frm_main['bg'] = 'white'
    self.frm_main.grid()
    
    # example
    self.lbl_example = tk.Label(self.frm_main, text='20 + 30 =')
    self.lbl_example.grid(column=0, row=0)

    # Input
    self.entry_example = tk.Entry(self.frm_main)
    self.entry_example.grid(column=1, row=0)


    self.lbl = tk.Label(self.frm_main, text='Нажми на кнопку')
    self.lbl.grid(column=0, row=1)
   
    # create button submit
    self.btn_submit = tk.Button(self.frm_main,
                            command=self.submit,
                            text='Проверить',
                            relief=tk.FLAT,
                            fg='black',
                            bg='green',
                            
                            width=10,
                            height=1,
                            highlightthickness=0)
    self.btn_submit.grid (column=0, row=2)
 
  def submit(self):   # btn_submit
    
    self.lbl['text'] = 'правильно'
