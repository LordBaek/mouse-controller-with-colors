#iport das libs
import cv2
import numpy as np
import pyautogui
from pyautogui import moveTo

#abrir camera
cam = cv2.VideoCapture(0)
#variavel para derrubar o programa
finish = 0
#loop
while True:
    #pega o frame da camera
    _, frameInv = cam.read()
    #inverte a camera
    frame = cv2.flip(frameInv, 1)
    #transforma o frame em formato HSV
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    #Variaveis da cor amarela
    lowerYellow = np.array([0, 91, 200])
    upperYellow = np.array([255, 255, 255])
    #mascara para captar somente a cor amarela no frame
    maskYellow = cv2.inRange(frameHsv, lowerYellow, upperYellow)
    #devolve apenas cor desejada
    resultYellow = cv2.bitwise_and(frame, frame, mask=maskYellow)
    #deixa a imagem em tons de cinza
    frameGrayYellow = cv2.cvtColor(resultYellow, cv2.COLOR_BGR2GRAY)
    #limpa "sujeira" da camera
    _, threshYellow = cv2.threshold(frameGrayYellow, 3, 255, cv2.THRESH_BINARY)
    #contorno do objeto
    contoursYellow, _ = cv2.findContours(
        threshYellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contourYellow in contoursYellow:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (xYellow, yYellow, wYellow, hYellow) = cv2.boundingRect(contourYellow)
        #define a variavel "area" com os contornos
        areaYellow = cv2.contourArea(contourYellow)
        #se a area da cor é maior que o valor desejado, a ação é realisada.
        if areaYellow > 1000:       
            pyautogui.moveTo(xYellow,yYellow)
        

    #declarações das variaveis da cor azul
    lowerBlue = np.array([93, 214, 86])
    upperBlue = np.array([255, 255, 255])
    #mascara para captar somente a cor azul
    maskBlue = cv2.inRange(frameHsv, lowerBlue, upperBlue)
    #devolve apenas cor desejada
    resultBlue = cv2.bitwise_and(frame, frame, mask=maskBlue)
    #deixa a imagem em tons de cinza
    frameGrayBlue = cv2.cvtColor(resultBlue, cv2.COLOR_BGR2GRAY)
    #limpa "sujeira" da camera
    _, threshBlue = cv2.threshold(frameGrayBlue, 3, 255, cv2.THRESH_BINARY)
    #contorno do objeto
    contoursBlue, _ = cv2.findContours(
        threshBlue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contourBlue in contoursBlue:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (xBlue, yBlue, wBlue, hBlue) = cv2.boundingRect(contourBlue)
        #define a variavel "area" com os contornos
        areaBlue = cv2.contourArea(contourBlue)
        #se a area da cor é maior que o valor desejado, a ação é realisada.(clique do mouse)
        if areaBlue > 1000:
            pyautogui.click(xYellow,yYellow,button='right')
        
    #declarações das variaveis da cor vermelha
    lowerRed = np.array([0, 182, 124])
    upperRed = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor vermelha no frame
    maskRed = cv2.inRange(frameHsv, lowerRed, upperRed)
    #devolve apenas cor desejada
    resultRed = cv2.bitwise_and(frame, frame, mask=maskRed)
    #deixa a imagem em tons de cinza
    frameGrayRed = cv2.cvtColor(resultRed, cv2.COLOR_BGR2GRAY)
    #deixa a imagem melhor, menos poluida
    _, threshRed = cv2.threshold(frameGrayRed, 3, 255, cv2.THRESH_BINARY)
    #contorno do objeto
    contoursRed, _ = cv2.findContours(
        threshRed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contourRed in contoursRed:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (xRed, yRed, wRed, hRed) = cv2.boundingRect(contourRed)
        #define a variavel "area" com os contornos
        areaRed = cv2.contourArea(contourRed)
        #analisa se a area vermelha é maior que 1000, se for, da um clique com o botão esquerdo nas posições x e y da area amarela, no caso o mouse.
        if areaRed > 1000:
            pyautogui.click(xYellow,yYellow,button='left')

    #declarações das variaveis da cor rosa
    lowerPink = np.array([147, 28, 255])
    upperPink = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor rosa no frame
    maskPink = cv2.inRange(frameHsv, lowerPink, upperPink)
    #devolve apenas cor desejada
    resultPink = cv2.bitwise_and(frame, frame, mask=maskPink)
    #deixa a imagem em tons de cinza
    frameGrayPink = cv2.cvtColor(resultPink, cv2.COLOR_BGR2GRAY)
    #limpa "sujeira" da camera
    _, threshPink = cv2.threshold(frameGrayPink, 3, 255, cv2.THRESH_BINARY)
    #contorno do objeto
    contoursPink, _ = cv2.findContours(
        threshPink, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contourPink in contoursPink:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (xPink, yPink, wPink, hPink) = cv2.boundingRect(contourPink)
        #define a variavel "area" com os contornos
        areaPink = cv2.contourArea(contourPink)
        #caso apareca um objeto com a cor rosa fecha o programa
        if areaPink > 1000:
            finish = 1
            
    #mostra o frame na camera
    cv2.imshow("Camera", frame)
    #seta a camera a 60fps
    key = cv2.waitKey(60)
    #se a variavel acabar for igual a 1, fecha o programa
    if finish == 1:
        break


#acaba com o código
cv2.destroyAllWindows()
#libera a camera
cam.release()
