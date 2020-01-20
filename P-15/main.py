import math  # Importowanie fukncji matematycznych


def ChangePositionNumber(n, k):  # n - Cyclists, k - Changes
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def HowManyChangesPossible(n, k, c):  # n - Cyclists, k - Changes, c - ChangePositionNumber
    for ChangePositionNumber in range(k):
        for Cyclists in range(n):
            # Try to implement adding a table with all cyclists

    for ChangePositionNumber in range(c):
        for Cyclists in range(n):
            # Try to implement a finding out that cyclist is where


Cyclists = int(input("Podaj ilość kolarzy: "))
Changes = int(input("Podaj ilość zmiany prowadzącego: "))

if Changes == 0:
    print("Ilość możliwości to " + str(math.factorial(Cyclists - 1)))
    input("\n\nWciśnij Enter, aby kontynuować...")
    exit()

print(HowManyChangesPossible(Cyclists, Changes, ChangePositionNumber(Cyclists - 1, Changes)))

input("\n\nWciśnij Enter, aby kontynuować...")  # Wstrzymanie programu
exit()
