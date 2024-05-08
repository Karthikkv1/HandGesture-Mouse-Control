import cv2
import mediapipe
import pyautogui

#Hand capture
capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils

screen_width,screen_height = pyautogui.size()

camera = cv2.VideoCapture(0)

x1 = y1 = x2 = y2 = 0 

while True:
    _ , image = camera.read()

    image_height , image_width, _ = image.shape

    image = cv2.flip(image,1) #Fliping  captured image

    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks

    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks = hand.landmark  #Capture one hand gesture
            for id,lm in enumerate(one_hand_landmarks):
                x=int(lm.x * image_width)
                y=int(lm.y * image_height)
                # print(x,y) #To print landmarks of hand

                if id == 8 : #Forefinger
                    mouse_x = int(screen_width / image_width * x)
                    mmouse_y = int(screen_height / image_height * y)
                    cv2.circle(image,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x,mmouse_y)
                    x1 = x
                    y1 = y

                if id == 4 : #Thumbfinger
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),10,(0,255,255))   
        dist = y2 - y1 #Identifying the vertical distance between two points
        print(dist)

        #If distance less than 20 , then click event occurs , that is if we click some part , then on  that part click event occurs.
        if(dist<20):
            pyautogui.click()
            print("Clicked")

    cv2.imshow("Hand Movement video capture",image)
    key = cv2.waitKey(100)
    if key == 27 : #Escape key
        break
camera.release()
cv2.destroyAllWindows()

