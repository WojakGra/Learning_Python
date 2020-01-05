from PIL import Image

# Funkcja do pobrania wartości piksela, przetworzeniu go tak jak zostało to podane w zadaniu
def ChangeContrast(image, change):
    newimagedata = []
    for constrast in image.getdata():
        constrast = int((constrast - 128) * change) + 128
        if constrast > 255:
            constrast = 255
        elif constrast < 0:
            constrast = 0
        newimagedata.append(constrast)
    newimage = Image.new(image.mode, image.size)
    newimage.putdata(newimagedata)
    return newimage

# Wprowadzanie danych
inputUser = input("Podaj nazwę pliku razem z rozszerzeniem bmp: ")
changeInt = float(input("Podaj liczbę o ile chcesz zmienić kontrast: "))
inputUser = inputUser.split('.bmp')
inputImage = Image.open(inputUser[0]+'.bmp')

# Wyprowadzanie danych
ChangeContrast(inputImage, changeInt).save(inputUser[0]+'-wynik.bmp')
print("Plik został zapisany jako: "+inputUser[0]+'-wynik.bmp')