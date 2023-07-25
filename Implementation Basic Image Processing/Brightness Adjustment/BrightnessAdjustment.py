from PIL import Image

imagem = Image.open("squirel.jpg")

brilho = 1.5

pixels = imagem.load()

largura, altura = imagem.size

for i in range(largura):
    for j in range(altura):
        
        cor = pixels[i,j]
        novoBrilho= tuple([int(c * brilho) for c in cor])
        pixels[i,j] = novoBrilho

imagem.save("squirel-BC.jpg")
