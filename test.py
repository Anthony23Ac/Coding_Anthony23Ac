print("Hola")
print("Mundo")

print("\033[2A", end="")  # subir 1 línea
print("\033[5C", end="")  # mover 5 columnas a la derecha
print(" Anthony")
print("\033[2B", end="") 

text = "1. Juan Andres Perezareca Acevendo"
previus_text = "" 
next_text = ""
palabra = 0

palabra_que_es = 0

for i, v in enumerate(text):
    if v == " ":
        palabra += 1 
    
    if i <= 19:
        palabra_que_es = palabra
        previus_text += v
    else:
        next_text += v

print(f"palabras: {palabra} palabras_que_Es: {palabra_que_es}")

new = text.split(" ")
print(new)
print(previus_text + "-")
print(f"   {next_text.strip()}")

print("Prueba babababab")