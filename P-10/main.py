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
inputImage = Image.open('koala.bmp')
changeInt = float(input("Podaj liczbę o ile chcesz zmienić kontrast: "))

# Wyprowadzanie danych
ChangeContrast(inputImage, changeInt).save('koala-wynik.bmp')