import fractions
import math

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
s1 = get_fraction("5", '21','1')
s2 = get_fraction("169", '48')

ex_1 = ['    (7 - 6,35) : 6,5 - 9,9',
        u'\u0C7C' * 25 + ' = ',
        '(1,2 : 36 + 1,2 : 0,25 - ' + s1 + ') : ' + s2
]

# Example 2
