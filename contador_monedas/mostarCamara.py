import cv2 as cv

capturar_Video = cv.VideoCapture(1)

if not capturar_Video.isOpened():
    print("No se encontro la camara")
    exit()
while True:
    Tcamara,frame = capturar_Video.read()
    
    grises=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    cv.imshow("Camara", grises)
    
    if cv.waitKey(1) == ord("q"):
        break
capturar_Video.release()
cv.destroyAllWindows()
