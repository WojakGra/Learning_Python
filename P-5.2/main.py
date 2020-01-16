# Słownik
Characters = {
    'A':0,
    'Ą':1,
    'B':2,
    'C':3,
    'Ć':4,
    'D':5,
    'E':6,
    'Ę':7,
    'F':8,
    'G':9,
    'H':10,
    'I':11,
    'J':12,
    'K':13,
    'L':14,
    'Ł':15,
    'M':16,
    'N':17,
    'Ń':18,
    'O':19,
    'Ó':20,
    'P':21,
    'Q':22,
    'R':23,
    'S':24,
    'Ś':25,
    'T':26,
    'U':27,
    'W':28,
    'V':29,
    'X':30,
    'Y':31,
    'Z':32,
    'Ź':33,
    'Ż':34
}

# Funkcja do pobierania value z key w słowniku
def GetKey(val):
    for key, value in Characters.items():
        if val == value:
            return key

# Wczytanie danych
inputList = list(input("Podaj ciąg: "))
inputNumber = int(input("Podaj przesuniecie: "))

# Przesuwanie znaków
outputList = []
for x in range(len(inputList)):
    characterNumber = Characters.get(inputList[x]) + inputNumber
    if(characterNumber > 34):
        characterNumber -= 35
        outputList.append(GetKey(characterNumber))
    elif(characterNumber < 0):
        characterNumber += 35
        outputList.append(GetKey(characterNumber))
    else:
        outputList.append(GetKey(characterNumber))

# Wypisanie wyniku
for i in outputList:
    print(i, end="")
