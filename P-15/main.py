import math  # Importowanie fukncji matematycznych


def ChangePositionNumber(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


Cyclists = int(input("Podaj ilość kolarzy: "))
Changes = int(input("Podaj ilość zmiany prowadzącego: "))

if Changes == 0:
    print("Ilość możliwości to " + str(math.factorial(Cyclists-1)))
    input("\n\nWciśnij Enter, aby kontynuować...")
    exit()

number = ChangePositionNumber(Cyclists - 1, Changes)

print(number)

# Wstrzymanie programu
input("\n\nWciśnij Enter, aby kontynuować...")
exit()