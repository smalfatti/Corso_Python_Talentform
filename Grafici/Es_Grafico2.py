import matplotlib.pyplot as plt

# Dati da visualizzare
x = []
y = []

while True:
    num1 = int(input("Inserisci un numero per x (o 0 per terminare): "))
    if num1 == 0:
        break
    x.append(num1)

    num2 = int(input("Inserisci un numero per y (o 0 per terminare): "))
    if num2 == 0:
        break
    y.append(num2)

# Creazione del grafico a linee
plt.plot(x, y)

# Personalizzazione dell'aspetto del grafico
plt.title("Grafico a linee")
plt.xlabel("X")
plt.ylabel("Y")

# Mostra il grafico
plt.show()