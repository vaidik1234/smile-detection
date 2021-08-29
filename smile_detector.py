import cv2

path='smile/i3.jpg'


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
 
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(

    gray,1.1,5)

for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  #for making rectangle on detected face i.e it drown from (x,y) to (x+w,y+h), (250,0,0) is color of box, 2 stand for thickness of box
        roi_gray = gray[y:y+h, x:x+w] #we have only focus on rectangled box area so we passed it to our classifier
        roi_color=img[y:y+h,x:x+w]
        smile = smileCascade.detectMultiScale(

            roi_gray,1.2,20)


        for (xx,yy,ww,hh) in smile:
            cv2.rectangle(roi_color,(xx,yy),(xx+ww,yy+hh),(0,255,0),2)

        for i in smile:
            if len(smile)>0.1:
                cv2.putText(img,"SMILE DETECTED",(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,(0,255,0),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()