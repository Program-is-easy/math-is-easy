import tkinter as tk
from test import *
from SysAriTrain import *
from AriTrain import *
from style import *
# from
# import

class SysAriTrain():
  def __init__(self, master):
    # create children window
    self.slave = tk.Toplevel(master)
    self.slave.geometry('+600+50')
    self.slave.wm_attributes("-topmost", 1)
    # create main conteiner
    self.frm_main = tk.Frame(self.slave)
    self.frm_main['bg'] = bg_main
    self.frm_main.grid()
    # create examples conteiner
    self.frm_example = tk.Frame(self.frm_main)
    self.frm_example['bg'] = bg_main
    self.frm_example.grid(column=0, row=1)
    # create guides conteiner
    self.frm_guides = tk.Frame(self.frm_main, bg=bg_main)
    self.frm_guides['bg'] = bg_main
    self.frm_guides.grid(column=0, row=0)

    # create example objects
    self.create_ex_1 = Example(self.frm_example, ex_1[0][0], ex_1[0][1], ex_1[0][2], ex_1[1], ex_1[2])
    self.create_ex_2 = Example(self.frm_example, ex_2[0][0], ex_2[0][1], ex_2[0][2], ex_2[1], ex_2[2])
    self.create_ex_3 = Example(self.frm_example, ex_3[0][0], ex_3[0][1], ex_3[0][2], ex_3[1], ex_3[2])
    self.create_ex_4 = Example(self.frm_example, ex_4[0][0], ex_4[0][1], ex_4[0][2], ex_4[1], ex_4[2])
    
    # create button submit
    self.btn_submit = tk.Button(self.frm_example,
                            command=self.submit,
                            text='Проверить',
                            relief=tk.FLAT,
                            fg=fg_main,
                            bg=bg_main,
                            font=font_main,
                            width=10,
                            height=1,
                            highlightthickness=0)
    self.btn_submit.grid (column=0, row=5, padx=0, pady=0, sticky="ewsn",)

  def submit(self):  # btn_submit
    
    ent = [self.create_ex_1,
          self.create_ex_2,
          self.create_ex_3,
          self.create_ex_4
    ]

    for idx in range(len(ent)):
      if ent[idx].ent_item.get() == str(ent[idx].answer) or ent[idx].ent_item.get() == str(ent[idx].answer.replace('.', ',')):
        # ... add results
        ent[idx].lbl_verify['text'] = '  верно  '# Add the rezult
        ent[idx].lbl_verify['fg'] = '#62be5c'
      else:
        # ... add results
        ent[idx].lbl_verify['text'] = 'неверно'  # Add the rezult
        ent[idx].lbl_verify['fg'] = '#c63b34'
      ent[idx].lbl_verify.grid(column=1, row=2, padx=10, pady=0, sticky="w")
      #Results(self.slave)              # start Application Reults

