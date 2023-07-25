from PIL import Image

def convert_to_black_white(image_path, threshold):
    
    img = Image.open(image_path).convert("L")

    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
        
            if pixels[i, j] < threshold:
                pixels[i, j] = 0  # Preto
            
            else:
                pixels[i, j] = 255  # Branco

    img.save("squirel-blackWhite.jpg")

convert_to_black_white("squirel.jpg", 80)