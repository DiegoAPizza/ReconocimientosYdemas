import cv2

imagen=cv2.imread('contorno.jpg')

gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

_,umbral=cv2.threshold(gris,100,255,cv2.THRESH_BINARY)

contorno,jeraquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)



#Mostrar
cv2.imshow("Imagen Original ",imagen)
cv2.imshow("Imagen con escala de grises ",gris)
cv2.imshow("Imagen con aplicacion de Umbral",umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()