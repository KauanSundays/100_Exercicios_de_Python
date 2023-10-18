tupla = (
    "Galadriel", "Luthien Tinuviel", "Erik Killmonger", 
    "Kendrick Lamar", "Charlotte Galves", "Roberta Pires", "Amanda"
)

vogais = ["a", "e", "i", "o", "u"]

for palavra in tupla:
    vogais_palavra = [letra for letra in palavra if letra.lower() in vogais]
    print(f"{palavra}: {vogais_palavra} - {len(vogais_palavra)} vogais")
