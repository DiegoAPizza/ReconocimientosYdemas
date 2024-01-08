import cv2

import numpy as np
from mostarCamara import capturar_Video

#lambda es una funcion anonima lambda x,y:x>y
def ordenar_Puntos(puntos):
    n_puntos = np.concatenate(puntos[0], puntos[1], puntos[2], puntos[3]).tolist()
    #Ordenamiento
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    
    x_order = y_order[:2]
    #Ordenamiento
    x_order = sorted(x_order, key=lambda x_order:x_order[0])
    
    x2_order = y_order[2:4]
    
    x2_order = sorted(x2_order, key=lambda x2_order:x2_order[0])
    
    return [x_order[0], x_order[1], x2_order[0], x2_order[1]]


def alineamento(imagen, ancho, alto):
    
    imagen_alienado = None
    
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    tipoUmbral, umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("Umbral",umbral)
    
    contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    
    contorno=sorted(contorno,key=cv2.contourArea,reverse=True)[:]
    
    for contornPere in contorno:
        epsilon=0.01*cv2.arcLength(contornPere,True)
        approx=cv2.approxPolyDP(contornPere,epsilon=epsilon,closed=True)
        if len(approx)==4:
            puntos=ordenar_Puntos(approx)
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            
            partefija=cv2.getPerspectiveTransform(puntos1,puntos2)
            
            imagen_alienado=cv2.warpPerspective(imagen,partefija,(ancho,alto))
            
        return imagen_alienado
capturar_Video=cv2.VideoCapture(1)

while True:
    tCamara,camara=capturar_Video.read()
    if tCamara==False:
        break
    
    
    
    
