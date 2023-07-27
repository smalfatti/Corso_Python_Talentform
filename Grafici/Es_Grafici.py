import matplotlib.pyplot as plt

# creo una lista di numeri vuoi
numbers = []

# chiedo all'utente con prompt di inserire dei numeri diversi da 0, altrimenti se 0 termino la selezione
while True:
    num = int(input("Enter a number (enter 0 to exit): "))
    if num == 0:
        break
    numbers.append(num)

# plot the input data
plt.plot(numbers)
plt.show()