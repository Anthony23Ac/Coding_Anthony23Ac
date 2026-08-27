
from os import system
if system("clear") != 0: system("cls")


print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.

edad = 17
nombre = "z"

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades tienes cedula")

if edad <= 18:
    print("usted es muchachillo, aun no puedes votar por bot")
    if nombre != "z":
        print("Eres de los grupos de z")

# de loc contrario > else , de lo contrario si -> else if

# else

mom_chore = "Wipe off the table"
enter = input("Did children wipe off the table? (Yes/No): ") #   -> yes
did_he_wipe_off_it = enter.replace(" ", "").lower() == "yes" # TRUE


if not did_he_wipe_off_it: # No es una condicción.
    print("the booger didnt wipe off the table. ")
elif did_he_wipe_off_it == None:
    print("We dont know if the children wiped off! ")    
else:
    print("the cleaver child wipe off the table. ")


#Clasificar notas
nota = 5

if nota >= 9: # False
  print("¡Sobresaliente!")
elif nota >= 7: # false
  print("Notable!")
elif nota >= 5: # true
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

age = 17 
own_money = 70000

if not (age >= 18): # No lo imprimiria.
    print("No eres mayor de edad.")
    if not (own_money <= 60000):
      print("te puedes comprar el nuevo pone 17! Osi")
    else:
      print("No puedes, solo es para gente platuda, de")
else:
   print("Si eres mayor de edad.")


