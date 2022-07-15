import tkinter as tk
from style import *

input =[20]
answ = [20]
items = ['',]

# function to convert to superscript
def get_fraction(numeration, denominator='1', natural=''):
  normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
  super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
  sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
  res1 = numeration.maketrans("".join(normal), "".join(super_s))
  res2 = numeration.maketrans("".join(normal), "".join(sub_s))
  return natural + numeration.translate(res1) + u'\u2044'+ denominator.translate(res2)

# Example 1
# Тут надо бы доработать функционал добавления новых примеров
s1 = [get_fraction("5", '21','1'),
      get_fraction("169", '48'),
      ]

ex_1 = [['    (7 - 6,35) : 6,5 - 9,9',
        u'\u0C7C' * 25 + ' = ',
        '(1,2 : 36 + 1,2 : 0,25 - ' + s1[0] + ') : ' + s1[1]
        ],
        '20',
        '1'
]


s2 = [get_fraction("7", '9'),
      get_fraction("47", '72'),
      get_fraction("7", '40'),
      get_fraction("19", '25'),
      ]

ex_2 = [['',
        '((' + s2[0] + ' - ' + s2[1] + ') : 1,25 + ' + s2[2] + ') : (0,358 - 0,108) x 1,6 - ' + s2[3] + ' = ',
        ''],
        '1',
        '2'
]

s3 = [get_fraction("7", '5'),
      get_fraction("4", '7', '1'),
      get_fraction("3", '11'),
      get_fraction("1", '4'),
      get_fraction("1", '3', '18'),
      ]

ex_3 = [['    (0,5 : 1,25 + '+ s3[0] +' : '+ s3[1] +' - '+s3[2]+') x 3',
        u'\u0C7C' * 25 + ' = ',
        ' '*11 + '(1,5 + '+s3[3]+') : +'+s3[4]
        ],
        '32',
        '3'
]
s4 = [get_fraction("1", '3', '2'),
      get_fraction("3", '70'),
      get_fraction("1", '2', '2'),
      ]

ex_4 = [['    (2,7 - 0,8) x '+ s3[0],
        '('+u'\u0C7C' * 15 + ') : '+s3[2]+' + 0,43 = ',
        '        (5,2 - 1,4) : '+s3[1]
        ],
        '0.5',
        '4'
]

# Example_5

class Example():
  def __init__(self, frame, str_1, str_2, str_3, answer, row='100', topics=''):
    self.frame = frame
    self.frm_ex = tk.Frame(self.frame)
    self.frm_ex['bg'] = bg_main
    self.frm_ex.grid(column=0, row=int(row), padx=0, pady=0, sticky="w")
    
    self.str_1 = str_1
    self.str_2 = str_2
    self.str_3 = str_3
    self.answer = answer
    self.texts_ex1 = [self.str_1, self.str_2, self.str_3, '...']
    for idx, text in enumerate(self.texts_ex1):
      self.lbl = self.create_lbl(text)
      if text == '...':
        self.lbl_verify = self.lbl
        self.lbl['width'] = 10
        self.lbl_verify.grid(column=1, row=2)
      else:
        self.lbl.grid(column=0, row=idx, padx=0, pady=0, sticky="w")
    
    self.ent_item   = tk.Entry(self.frm_ex, relief=tk.SUNKEN, width=15)
    self.ent_item.insert(0, "0")
    self.ent_item.configure(relief=relief_main, bg=bg_main, fg=fg_main, font=font_main)
    self.ent_item.grid  (column=1, row=1, padx=0, pady=0, sticky="w")
    

    
  def create_lbl(self, text, fg=fg_main, font=font_main):
    return tk.Label(self.frm_ex, text=text, relief=relief_main,
                    fg=fg, bg=bg_main, font=font,
                    )

  def create_ent(self):
    return tk.Entry(self.frm_ex, relief=tk.SUNKEN, width=5,
                    fg=fg_main, bg=bg_main, font=('Roboto', 15, 'bold'))
