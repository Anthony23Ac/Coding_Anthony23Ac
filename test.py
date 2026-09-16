text = "1. Juan Andres Perez Acevendo"
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
print(previus_text)
print(f"   {next_text.strip()}")

previus_l = ""
vowels = "aeiou"
silabas = []

letras = new[palabra_que_es].replace(" ", "").split("")

for i, l in enumerate(new[palabra_que_es]):
    if i == 0:
        if not letras[i + 1].lower() in vowels and l.lower() in vowels:
            silabas.append(l)
    else:
        if not previus_l.lower() in vowels and l.lower() in vowels:
            silabas.append(previus_l + l)
    previus_l = l