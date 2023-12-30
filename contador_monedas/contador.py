import cv2 

import numpy as np

imagen_Original=cv2.imread('monedas.jpg')

gris=cv2.cvtColor(imagen_Original,cv2.COLOR_BGR2GRAY)

#Proceso de Eliminacion de Imagen 
    #Modelado Gauss
valor_gaus=3
valor_kernel=3
        #Aplica un desenfoque a una Imagen
gauss=cv2.GaussianBlur(gris,(valor_gaus,valor_gaus),0)
        #Eliminar el ruido de la imagen
canny=cv2.Canny(gauss,60,100)

kernel=np.ones((valor_kernel,valor_kernel),np.uint8)
#Aplicamos una clausura para eliminar el ruido interno
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

contornos_monedas,jeraquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print(f"Monedas Encontradas {len(contornos_monedas)}")

cv2.drawContours(imagen_Original,contornos_monedas,-1,(0,0,255),3)
#Mostrar Resultados

#cv2.imshow("Grises",gris)

#cv2.imshow("Gaus",gauss)

cv2.imshow("Canny",canny)

cv2.imshow("Cierre",cierre)

cv2.imshow("Resultado",imagen_Original)

cv2.waitKey(0)
cv2.destroyAllWindows()