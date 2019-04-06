
import numpy as np
import cv2
no_of_students=int(input("Enter the total no.of students in the class"))
present=[]
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("trainingdata.yml")
id=0
font=cv2.FONT_HERSHEY_SIMPLEX
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if id==1:
            id="first person"
            present.append(id)
        if id==2:
            id="second person"
            present.append(id)
        if id==3:
            id="Third person"
            present.append(id)
        if id==4:
            id="Fourth person"
            present.append(id)
        
        cv2.putText(img,str(id),(x,y+h),font,1,(200,255,00),2,cv2.LINE_AA)
    cv2.imshow('img',img)

    if cv2.waitKey(1) == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()
students=set(present)
file='attendance report.txt'
with open(file,'w') as fp:
    fp.write("student's present {}\n".format(students))
    fp.write('no.of students present ={}\n'.format(len(students)))
    fp.write('no.of students absent = {}\n'.format(no_of_students-len(students)))

    
