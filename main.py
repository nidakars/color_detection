import numpy as np
import cv2
from gtts import gTTS
import os #for playing mp3 files

cap=cv2.VideoCapture(0) #bilgisayar kamerasından görüntü alır

"""
ARA RENKLERİN TANINMASI İÇİN HSV RENK KODLARI İNCELENMELİ
low_yellow = np.array([20, 80, 80])	 
high_yellow = np.array([30, 255, 255])


low_white = np.array([0,0,168])
high_white = np.array([359,2,255])

low_orange=np.array([0,50,80])
high_orange=np.array([50,255,255])

low_gray = np.array([0,0, 50])
high_gray = np.array([0, 5, 50])

low_black = np.array([0,0,0])
high_black = np.array([350,55,100])
"""

def blue_speech():
    message="Mavi size çok yakışmış"
    tts=gTTS(message, lang='tr', slow=True)
    tts.save('blue.mp3')
    file_b="blue.mp3"    
    os.system(file_b)

def green_speech():
    message="Yeşil size çok yakışmış"
    tts=gTTS(message, lang='tr', slow=True)
    tts.save('green.mp3')
    file_b="green.mp3"    
    os.system(file_b)
    
def red_speech():
    message="Kırmızı size çok yakışmış"
    tts=gTTS(message, lang='tr', slow=True)
    tts.save('red.mp3')
    file_b="red.mp3"    
    os.system(file_b)



while True:
    _,frame=cap.read()
    width=int(cap.get(3)) #görüntünün genişliğini belirler
    height=int(cap.get(4))#görüntünün boyutunu belirler
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #renk kodlarını HSV türüne dönüştürür
    
    
    low_blue = np.array([94,80,2],np.uint8) #en açık mavi tonu
    high_blue = np.array([120,255,255],np.uint8) #en koyu mavi tonu
    blue_mask = cv2.inRange(hsv, low_blue, high_blue) #mavi renkler için maskeleme yapar
    blue_out=cv2.bitwise_and(frame,frame, mask= blue_mask)

    
    low_green = np.array([25, 52, 72],np.uint8)	 
    high_green = np.array([100, 255, 255],np.uint8)
    green_mask = cv2.inRange(hsv, low_green, high_green)
    green_out=cv2.bitwise_and(frame,frame, mask= green_mask)

    
    low_red = np.array([136, 87, 111], np.uint8)
    high_red = np.array([179, 255, 255],np.uint8)
    red_mask = cv2.inRange(hsv, low_red, high_red)
    red_out = cv2.bitwise_and(frame,frame, mask= red_mask) #sadece mavi renkli kısımlar görüntülenir
    
    #kırmızı bölge tespitleri
    red_contours, hierarchy=cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #tespit edilen mavi kısımlar belirlenir 
    if len(red_contours) !=0:           #eğer tespit edilmiş bir mavili
        blue_speech()
        for contour in red_contours:    
            if cv2.contourArea(contour)>2500:    #kontürlenecek alan belli bir orandan büyükse
                x,y,w,h=cv2.boundingRect(contour) #bu kısmın etrafına kare çiz
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0, 255), 3)    #çizilecek karenin detayları
    
    #yeşil bölge tespitleri            
    green_contours, hierarchy=cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #tespit edilen mavi kısımlar belirlenir 
    if len(green_contours) !=0:           #eğer tespit edilmiş bir mavili
        green_speech()
        for contour in green_contours:    
            if cv2.contourArea(contour)>2500:    #kontürlenecek alan belli bir orandan büyükse
                x,y,w,h=cv2.boundingRect(contour) #bu kısmın etrafına kare çiz
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255, 0), 3)    #çizilecek karenin detayları
    
    #mavi bölge tespitleri   
    blue_contours, hierarchy=cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #tespit edilen mavi kısımlar belirlenir 
    if len(blue_contours) !=0:           #eğer tespit edilmiş bir mavili
        red_speech()
        for contour in blue_contours:    
            if cv2.contourArea(contour)>2500:    #kontürlenecek alan belli bir orandan büyükse
                x,y,w,h=cv2.boundingRect(contour) #bu kısmın etrafına kare çiz
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0, 0), 3)    #çizilecek karenin detayları
           
                
                
    """ 
    cv2.imshow('red', red_out) #görüntüleme yapan komut
    cv2.imshow('red_mask', red_mask) #görüntüleme yapan komut
    cv2.imshow('green', green_out) #görüntüleme yapan komut
    cv2.imshow('green_mask', green_mask)
    cv2.imshow('blue', blue_out) #görüntüleme yapan komut
    cv2.imshow('blue_mask', blue_mask)
    """
    cv2.imshow('all',frame)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşuna basınca programı kapat
        break
    
cap.release()
cv2.destroyAllWindows()

