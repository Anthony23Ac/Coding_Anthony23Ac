###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print(5 > 3) # TRUE
print(5 < 3) # False
print(5 == 5) # True
print(5 != 3) # True
print(5 >= 5) # True
print(5 <= 3) # False

# Valores Strings

print("Manzana" < "pera") # True 
# a b c d e f g h i j k l m n o p
#                         ↑      ↑
#                         m      p

print("A" > "a") # True
#UniCode:
# "A" → 65
# "a" → 97

print("Apple".casefold() == "apple".casefold()) # True --> False
# True

print("hola" == "Hola") # False

print("hola" >= "Hola") # True

# h -> 0068
# H -> 0048

print("Ship" <= "ship") # True 

# S -> 0053
# s -> 0073

print("cHase" >= "chase") # false -> True