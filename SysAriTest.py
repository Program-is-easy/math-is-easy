import tkinter as tk
from test import *
from SysAriTrain import *
# from
# import

bg_main      = "#555"
fg_main      = "#ccc"
relief_main  = tk.FLAT
font_main    = ('Roboto', 15, 'bold')
font_ex      = ('Arial', 15)


class SysAriTest():
  def __init__(self, master):
    self.slave = tk.Toplevel(master)
    self.slave.geometry('+100+200')
    self.slave.wm_attributes("-topmost", 1)
    
    self.frm_main = tk.Frame(self.slave)
    self.frm_main['bg'] = bg_main
    self.frm_main.grid()

    self.frm_example = tk.Frame(self.frm_main)
    self.frm_example['bg'] = bg_main
    self.frm_example.grid(column=0, row=1)

    self.frm_guides = tk.Frame(self.frm_main, bg=bg_main)
    self.frm_guides['bg'] = bg_main
    self.frm_guides.grid(column=0, row=0)

    self.texts_ex1 = [ex_1[0], ex_1[1], ex_1[2], ]
    for idx, text in enumerate(self.texts_ex1):
      self.lbl = self.create_lbl(text)

      self.lbl.grid(column=0, row=idx, padx=0, pady=0, sticky="w")

    # row 0-2
    row = 0
    
    self.ent_item   = tk.Entry(self.frm_example, relief=tk.SUNKEN, width=15)
    self.lbl_verify = tk.Label(self.frm_example, width=15)

    
    self.ent_item.insert(0, "0")
    self.lbl_verify['text'] = '...'

    self.lbls = [
      self.ent_item,
      self.lbl_verify
    ]

    for item in self.lbls:
      item.configure(relief=relief_main, bg=bg_main, fg=fg_main, font=font_main)

    row = 0
 
    row = 1
    self.ent_item.grid  (column=1, row=row, padx=0, pady=0, sticky="w")
 
    row = 2
    self.lbl_verify.grid(column=1, row=row)
 
    row = 3
    
 
    row = 4
    self.btn_submit = tk.Button(self.frm_example,
                            command=self.submit,
                            text='Проверить',
                            relief=tk.FLAT,
                            fg=fg_main,
                            bg=bg_main,
                            font=('Roboto', 15, 'bold'),
                            width=10,
                            height=1,
                            highlightthickness=0)
    self.btn_submit.grid (column=1, row=row, padx=0, pady=0, sticky="ewsn",)
 
  def submit(self):
    
    ent = [self.ent_item.get(),]
    rez1 = [str(input[0]),]
    rez2 = [rez1[0].replace('.', ','),]# . or , -- replace
    for idx in range(len(rez1)):
      if ent[idx] == rez1[idx] or ent[idx] == rez2[idx]:
        SysAriTrain(self.slave)
        self.lbl_verify = self.create_lbl('  верно  ', 'green')   # Add the rezult
      else:
        self.lbl_verify = self.create_lbl('неверно', 'red')
      self.lbl_verify.grid(column=1, row=2, padx=10, pady=0, sticky="w")

  def create_lbl(self, text, fg=fg_main):
    return tk.Label(self.frm_example, text=text, relief=tk.FLAT,
                    fg=fg, bg=bg_main, font=('Roboto', 15, 'bold'),
                    )

  def create_ent(self):
    return tk.Entry(self.frm_example, relief=tk.FLAT, width=5,
                    fg=fg_main, bg=bg_main, font=('Roboto', 15, 'bold'))