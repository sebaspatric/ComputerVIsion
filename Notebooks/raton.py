import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = np.zeros((500,500,3), np.int8)

#defines the draw function
def dibujar(event, x, y, etiquetas, parametros):
  if event == cv2.EVENT_LBUTTONDOWN: #mouse click
    cv2.circle(imagen, (x,y), 50, (255,0,0), -1)


#conectamos la imagen con laa funcion

cv2.namedWindow(winname= 'mi_imagen')
cv2.setMouseCallback('mi_imagen', dibujar)

while True:
  cv2.imshow('mi_imagen', imagen)
      # Espera hasta que se presione una tecla durante 10 milisegundos
    # y verifica si la tecla presionada es 'Esc' (27 en el código ASCII)
  if cv2.waitKey(10) & 0xFF == 27:
    break

cv2.destroyAllWindows
