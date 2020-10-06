length = input("Podaj dlugosc w metrach: ")
length = float(length)
print(f"Podana wartość to {length*10:4.2f} decymetrów")
print(f"Podana wartość to {length/100:4.2f} kilometrów")
print(f"Podana wartość to {length*100:4.2f} centymetrów")
cal = 2.54/100
rin = 0.0303/100
bu = 10*rin
sun = 10*bu
shaku = 10*sun
print("Podana wartość to {:4.2f} cali".format(length/cal))
print(f"Podana wartość to {length/rin:4.2f} rinow")
print(f"Podana wartosc to {length/bu:4.2f} bu")
print("Podana wartosc to {:4.2f} sunow".format(length/sun))
print("Podana wartosc to {:4.2f} shakow".format(length/shaku))