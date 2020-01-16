# Funkcja do przetworzenia wartości tak jak zostało to podane w zadaniu
def ChangeContrast(numbers, change):
    newnumbers = []
    global lighter, darker
    lighter, darker = 0,0
    for constrast in numbers:
        constrast = int((constrast - 128) * change) + 128
        if constrast > 255:
            constrast = 255
        elif constrast < 0:
            constrast = 0
        newnumbers.append(constrast)
    print(newnumbers)
    for x, y in zip(numbers, newnumbers):
        if x < y:
            lighter += 1
        elif x > y:
            darker += 1
        else:
            continue

# Funkcja do zmiany z binarnych liczb na decymalne
def ChangeDecToBin(list):
    newlist = []
    for number in list:
        number = int(number, 2)
        newlist.append(number)
    print(newlist)
    return newlist



# Wprowadzanie danych
inputUser = input("Podaj ciąg: ")
changeInt = float(input("Podaj liczbę o ile chcesz zmienić kontrast: "))
inputUser = inputUser.split()

# Wyprowadzanie danych
ChangeContrast(ChangeDecToBin(inputUser), changeInt)
print("Ilość jaśniejszych pikseli to "+str(lighter))
print("Ilość ciemniejszych pikseli to "+str(darker))