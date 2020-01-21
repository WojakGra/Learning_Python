import math  # Importowanie fukncji matematycznych


def ChangePositionNumber(n, k):  # n - Cyclists, k - Changes
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def HowManyChanges(n, k, c):  # n - Cyclists, k - Changes, c - ChangePositionNumber
    CyclistsList = []

    TempList = [1]
    for Changes in range(k):
        for Cyclists in range(2, n + 1):
            if Cyclists > TempList[0]:
                TempList.insert(0, Cyclists)
                break
    CyclistsList.append(TempList)

    for ChangePositionNumber in range(1, c):
        TempList = CyclistsList[ChangePositionNumber-1]
        TempList[][] = Cyclist
        CyclistsList.append(TempList)

    return CyclistsList


"""
    for ChangePositionNumber in range(c):
        for Cyclists in range(n):
            # Try to implement a finding out that cyclist is where
"""

Cyclists = int(input("Podaj ilość kolarzy: "))
Changes = int(input("Podaj ilość zmiany prowadzącego: "))

if Changes == 0:  # Wypisywanie wyniku jeżeli zmiana prowadzącego to 0
    print("Ilość możliwości to " + str(math.factorial(Cyclists - 1)))
    input("\n\nWciśnij Enter, aby kontynuować...")
    exit()

print(HowManyChanges(Cyclists, Changes, ChangePositionNumber(Cyclists - 1, Changes)))

input("\n\nWciśnij Enter, aby kontynuować...")  # Wstrzymanie programu
exit()
