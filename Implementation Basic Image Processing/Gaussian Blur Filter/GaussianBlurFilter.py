from PIL import Image, ImageFilter

image = Image.open("squirel.jpg")

gaussianBlur = image.filter(ImageFilter.GaussianBlur(radius=2))

gaussianBlur.save("squirel-gaussian.jpg")
