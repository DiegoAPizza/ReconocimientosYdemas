import cv2 as cv

imagen=cv.imread('contorno.jpg')

gris=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)

_,umbral=cv.threshold(gris,100,255,cv.THRESH_BINARY)

contorno,jeraquia=cv.findContours(umbral,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(imagen,contorno,-1,(251,60,50),3)

#Mostrar
cv.imshow("Imagen Original ",imagen)
#cv.imshow("Imagen con escala de grises ",gris)
#cv.imshow("Imagen con aplicacion de Umbral",umbral)
cv.waitKey(0)
cv.destroyAllWindows()