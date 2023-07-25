from PIL import Image

def apply_average_filter(image, kernel_size):
    filtered_image = image.copy()

    half_kernel = kernel_size // 2

    for x in range(image.width):
        for y in range(image.height):
            pixels = []
            for i in range(-half_kernel, half_kernel + 1):
                for j in range(-half_kernel, half_kernel + 1):
                    px, py = x + i, y + j
                    if px < 0 or px >= image.width or py < 0 or py >= image.height:
                        pixels.append((0, 0, 0))
                    else:
                        pixels.append(image.getpixel((px, py)))

            r = sum([p[0] for p in pixels]) // len(pixels)
            g = sum([p[1] for p in pixels]) // len(pixels)
            b = sum([p[2] for p in pixels]) // len(pixels)

            filtered_image.putpixel((x, y), (r, g, b))

    return filtered_image


imagem = Image.open("squirel.jpg")

tamanho_kernel = 3

imagem_filtrada = apply_average_filter(imagem, tamanho_kernel)

imagem_filtrada.save("squirel-average.jpg")