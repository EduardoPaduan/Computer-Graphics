from PIL import Image

imagem = Image.open("squirel.jpg")

flipImageLF = imagem.transpose(Image.FLIP_LEFT_RIGHT)
flipImageTB = imagem.transpose(Image.FLIP_TOP_BOTTOM)


flipImageLF.save("squirel-flip-leftRight.jpg")

flipImageTB.save("squirel-flip-topbottom.jpg")
