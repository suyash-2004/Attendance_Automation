import cv2
import face_recognition
import numpy as np
import csv
from _datetime import datetime
import mysql.connector as sqlc

con = sqlc.connect(host='localhost', user='root', password='suyash2004', database='attendance', auth_plugin='mysql_native_password')
cursor = con.cursor()


sno_ = 1
images = []
classnames = []
query_default = "INSERT INTO `attendance`.`class_att` (`S.No.`,`NAME`, `ROLL.NO`, `PHONE NO.`, `P/A`, `TIME`) VALUES (%s, %s, %s, %s, 'A', '-');"
query_update = "UPDATE `attendance`.`class_att` SET `P/A` = %s, `TIME` = %s WHERE `ROLL.NO` = %s;"


def getimages():
    path = "ImagesAttendance"
    global images, classnames
    with open('Attendance_Database.csv', 'r') as att_db:
        reader = csv.reader(att_db)
        next(att_db)
        for row in reader:
            curimg = cv2.imread(f'{path}/{row[5]}')
            images.append(curimg)
            classnames.append(row[1].upper())



def find_encodings(images):
    encodlist = []
    for image in images:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image, model='cnn')
        encodlist.append(encode[0])
    return encodlist


def default_table():
    global sno_
    with open('Attendance_Database.csv','r') as att_db:
        data_db = att_db.readlines()
        cursor.execute("SELECT * FROM attendance.class_att")
        data = cursor.fetchall()
        if len(data) == 0:
            for line in data_db[1:]:
                entry = line.split(",")
                val = (sno_, entry[1], entry[2], entry[3])
                cursor.execute(query_default, val)
                sno_ += 1
            con.commit()


def getstd_details_db(nm):
    with open('Attendance_Database.csv','r') as att_db:
        data_db = att_db.readlines()
        for line in data_db[1:]:
            entry_db = line.strip().split(",")
            if entry_db[1].upper() == nm:
                roll_ = int(entry_db[2])
                phn_ = entry_db[3]
                break
        curtime_ = datetime.now().strftime("%H:%M:%S")
        result = [roll_,phn_,curtime_]
    return result


def mark_attendance(name_, roll_, pn_, dtstring_):
    entry_att = []
    global sno_
    with open('attendance.csv', 'r+') as att:
        data_attnd = att.readlines()
        names_att = []
        for line in data_attnd[1:]:
            entry_att = line.strip().split(",")
            names_att.append(entry_att[1].upper())
        if name_ not in names_att:
            sno_ = len(data_attnd) - 1
            sno_ += 1
            att.writelines(f'\n{sno_},{name_},{roll_},{pn_},P,{dtstring_}')

getimages()
knownencodings = find_encodings(images)
default_table()
print("Encoding Complete!")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facelocCurrframe = list(face_recognition.face_locations(imgs))
    encodCurrframe = face_recognition.face_encodings(imgs, facelocCurrframe)

    for faceEncode, faceloc in zip(encodCurrframe, facelocCurrframe):
        matches = face_recognition.compare_faces(knownencodings, faceEncode, tolerance=0.6)
        facedist = face_recognition.face_distance(knownencodings, faceEncode)
        matchindex = np.argmin(facedist)
        if matches[matchindex]:
            name = classnames[matchindex].upper()
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (faceloc[0], faceloc[2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            results = getstd_details_db(name)
            roll = results[0]
            phn = results[1]
            curtime = results[2]
            mark_attendance(name, roll, phn, curtime)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            with open('attendance.csv', 'r') as att:
                data_att = att.readlines()
                for line_att in data_att[1:]:
                    spt_data_att = line_att.strip().split(",")
                    dtstring = spt_data_att[5]
                    roll = spt_data_att[2]
                    presentval = ('P', dtstring, roll)
                    cursor.execute(query_update, presentval)
            con.commit()
            con.close()
            break

cv2.destroyAllWindows()