from PIL import Image, ImageFilter
import os

def rotate():
    image = Image.open( "Lenna.png" )
    image.rotate(90).save('Lenna_rotated.png')

def blur():
    image = Image.open( "Lenna.png" )
    blurredImage = image.filter(ImageFilter.BLUR)
    blurredImage.show()

def createThumbnail():
    size = (120, 120)
    image = Image.open("Lenna.png")
    image.thumbnail(size)
    image.show()

def convertToPNG():
    for file in os.listdir('.'):
        if file.endswith('.jpg'):
            image = Image.open(file)
            fn, fext = os.path.splitext(file)
            image.save('pngs/{}.png'.format(fn))

def resizeImages():
    size = (300, 300)
    for file in os.listdir('.'):
        if file.endswith('.jpg'):
            image = Image.open(file)
            fn, fext = os.path.splitext(file)
            image.thumbnail( size )
            image.save( 'resized/{}_resized{}'.format( fn, fext ) )


if __name__ == '__main__':
    blur()  # Call functions here