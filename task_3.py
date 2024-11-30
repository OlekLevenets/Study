import math
#from fractions import *
#alpha = math.radians(45)
#y = Fraction(math.sin(4*alpha),1 + math.cos(4*alpha))*Fraction(math.cos(2*alpha),1+math.cos(2*alpha))
#print(y)
#Це спосіб який я спробував спочaтку , але fraction я так розумію це лише цілі числа..
alpha = math.radians(30)
y_formula = ((math.sin(4 * alpha)) / (1 + math.cos(4 * alpha))) * ((math.cos(2 * alpha)) / (1 + math.cos(2 * alpha)))
y_cotangent = 1 / math.tan((3 * math.pi / 2) - alpha)
print(y_formula)
print(y_cotangent)
y_formula_rounded = round(y_formula, 5)
y_cotangent_rounded = round(y_cotangent, 5)

if y_formula_rounded == y_cotangent_rounded:
    print("Результати одинакові")
else:
    print("Результати відрізняються")





