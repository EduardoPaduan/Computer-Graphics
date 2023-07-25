import cv2

imagem = cv2.imread("squirel.jpg")

azul, verde, vermelho = cv2.split(imagem)

cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

imagem_unida = cv2.merge((azul,verde,vermelho))

cv2.imshow("Imagem Unida", imagem_unida)

cv2.waitKey(0)
cv2.destroyAllWindows