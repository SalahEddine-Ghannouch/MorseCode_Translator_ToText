import cv2
import time
import os
import HandTrackingModule as htm
import encryp_finger_morse as ciphers
import decryption as deciphers                           
import subprocess
import speech_recognition as sr
import pyttsx3

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "G:/Study/S1/3-Vision.par.Ordinateur/MiniProjet/New Subject/Project_Code/Source_Code_MorseTrans/FingerImages"
myList = os.listdir(folderPath)
# print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
auxiliaryList = []
auxiliaryListJoin =""
text_message_final=""

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)


        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]

        cv2.rectangle(img, (1, 200), (90, 260), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (30, 250), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 5)


        #--------------- fingers detection to morse_code start : ---------------#

        totalFingersNumber = str(totalFingers)
        auxiliaryList.append(totalFingersNumber)
        # auxiliaryList = list(set(auxiliaryList))
        auxiliaryListJoin = "".join(auxiliaryList)

        newStringList = ""
        for c1, c2 in zip(auxiliaryListJoin, auxiliaryListJoin[1:]):
            if c1 != c2:
                newStringList += c1

        print("Final list : "+newStringList+auxiliaryListJoin[-1])
        our_morse_code_finger_detecte =newStringList+auxiliaryListJoin[-1]       

        morse_code_finger = ciphers.encryptor(our_morse_code_finger_detecte)
        text_message_final = deciphers.decryptor(morse_code_finger)

        #put text final in capture
        cv2.putText(img, str(text_message_final), (130, 450), cv2.FONT_HERSHEY_PLAIN,3, (0, 255, 0), 4) 

        #--------------- fingers detection to morse_code end : ---------------#

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.putText(img, f'FPS: {int(fps)}', (520, 40), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    # -------------------------- treatment keys -------------------------- #
    exit_prog = cv2.waitKey(10) & 0xFF
    if exit_prog == 113:  # clic on q to exit 
            print("Close App")
            break

    if exit_prog == 115:  # clic on s to hear message
        if text_message_final !="" and text_message_final != None:
            print("get message heard")
            x=text_message_final
            engine = pyttsx3.init()
            engine.setProperty("rate", 110) ## 2nd parameter sets speed
            engine.say("Your Message is "+x)
            engine.runAndWait()
        else:
            engine = pyttsx3.init()
            engine.setProperty("rate", 120) ## 2nd parameter sets speed
            engine.say("Nothing to say right now")
            engine.runAndWait()
            print("Nothing to say")

    if exit_prog == 100:  # clic on d to go home
            print("Go Home")
            cap.release()
            cv2.destroyAllWindows()
            # Call the other file content
            os.system("python Source_Code_MorseTrans\home_page.py")


    if exit_prog == 102:  # clic on f to reload capture
            print("reload capture")
            cap.release()
            cv2.destroyAllWindows()
            # Call the other file content
            os.system("python Source_Code_MorseTrans\FingerCounter.py")

cv2.destroyAllWindows()
cap.release()    