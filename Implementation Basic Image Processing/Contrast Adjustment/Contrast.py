from PIL import Image

imagem = Image.open("squirel.jpg")

contraste = 1.3

pixels = imagem.load()

largura, altura = imagem.size

for i in range(largura):
    for j in range(altura):
        
        cor = pixels[i,j]
        novoContraste = tuple([int((c - 128) * contraste + 128) for c in cor])
        pixels[i,j] = novoContraste

imagem.save("squirel-BC.jpg")