from PIL import Image
from statistics import median

def aplicar_filtro_mediana(imagem, imagem_filtrada, tamanho_janela):
    largura, altura = imagem.size
    for x in range(largura):
        for y in range(altura):
            if x > 0 and y > 0 and x < imagem.width - 1 and y < imagem.height - 1:
                pixels_janela = []
                
                for i in range(-tamanho_janela//2, tamanho_janela//2+1):
                    for j in range(-tamanho_janela//2, tamanho_janela//2+1):
                        pixels_janela.append(imagem.getpixel((x+i, y+j)))
                pixels_janela.sort()
                pixel_mediano = pixels_janela[len(pixels_janela)//2]
                imagem_filtrada.putpixel((x, y), pixel_mediano)


imagem = Image.open("squirel.jpg")
imagem_filtrada = Image.new(imagem.mode, imagem.size)
tamanho_janela = 3
aplicar_filtro_mediana(imagem, imagem_filtrada, tamanho_janela)
imagem_filtrada.save("squirel-median.jpg")