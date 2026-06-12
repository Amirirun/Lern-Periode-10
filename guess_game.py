import random

zahl = random.randint(1, 100)
versuche = 0

print(" ZahlenRatespiel")
print("Ich denke an eine Zahl zwischen 1 und 100.")

while True:
    tipp = int(input("Dein Tipp: "))
    versuche += 1

    if tipp < zahl:
        print("Zu klein ")
    elif tipp > zahl:
        print("Zu gross ")
    else:
        print(f"Richtig!  Du hast {versuche} Versuche gebraucht.")
        break