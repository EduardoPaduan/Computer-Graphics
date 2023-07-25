from PIL import Image

def converter_para_tons_de_cinza(caminho_imagem):

    imagem = Image.open(caminho_imagem)

    imagem_cinza = imagem.convert('L')

    caminho_imagem_cinza = caminho_imagem.replace('.jpg', '-gray.jpg')

    imagem_cinza.save(caminho_imagem_cinza)

    return caminho_imagem_cinza


caminho_imagem_cinza = converter_para_tons_de_cinza("squirel.jpg")