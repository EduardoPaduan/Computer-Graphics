from PIL import Image

def girar_imagem_90_graus(image):
    imagem = Image.open(image)

    imagem_girada = imagem.rotate(90, expand=True)

    caminho_imagem_girada = image.replace('.jpg', '_rotate.jpg')

    imagem_girada.save(caminho_imagem_girada)

    return caminho_imagem_girada

image = 'squirel.jpg'
newImage = girar_imagem_90_graus(image)