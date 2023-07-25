import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Arquivos de programas\Tesseract-OCR\tesseract' 


imagem = cv2.imread("Images\carro2.jpg")
lista_imagens = []

#original
cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)

#gray
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem cinza", imagem_gray)
cv2.waitKey(0)

#Blur
imagem_suavizada = cv2.blur(imagem_gray, (9,9))
cv2.imshow("Imagem suavizada", imagem_suavizada)
cv2.waitKey(0)

#Binary
_, imagem_binaria = cv2.threshold(imagem_suavizada, 140, 255, cv2.THRESH_BINARY)
cv2.imshow("Imagem binária", imagem_binaria)
cv2.waitKey(0)

#Contours
contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Contornos encontrados "+str(len(contornos)))
imagem_contornos = imagem.copy()
cv2.drawContours(imagem_contornos, contornos, -1, (0,255,0), 3)
cv2.imshow('Contours', imagem_contornos)
cv2.waitKey(0)


lista_imagens = []

for contorno in contornos:
    (x, y, w, h) = cv2.boundingRect(contorno)    
    area = int(w) * int(h)
    print("area=" + str(area))

    if area > 9000:
        if w > h:
            lista_imagens.append(contorno)
        

print("Possiveis placas identificadas: " + str(len(lista_imagens)))


for item in lista_imagens:
    (x, y, w, h) = cv2.boundingRect(item)
    img1 = imagem[y:y+h, x:x+w] 
    img2 = imagem_binaria[y:y+h, x:x+w] 

    placaEscrito = pytesseract.image_to_string(img2, lang = 'eng')

    if  len(placaEscrito) >= 7:

        cv2.imshow("Placa Extraída", img1)
        cv2.waitKey(0)   

        cv2.imshow("Placa Extraída binária", img2)
        cv2.waitKey(0)

        if "_" or "."or "," in placaEscrito:

            placaEscrito = placaEscrito.replace("_", "")
            placaEscrito = placaEscrito.replace(".", "")
            placaEscrito = placaEscrito.replace(",", "")
            print('A placa Detectado eh: ', placaEscrito)
            cv2.imwrite("Placa.jpg",img1)
        else:
            print('A placa Detectada: ', placaEscrito)
            cv2.imwrite("Placa.jpg",img1)
