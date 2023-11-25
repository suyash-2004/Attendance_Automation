# Attendance Automation using Python with Face Recognition

Welcome to the Attendance Automation project! This is a mini project for my 2nd year (3rd semester) coursework, focusing on automating attendance tracking through the power of Python with face recognition.


<div align="center"> 
  <img src="https://media.giphy.com/media/3o7abnQiguzMTaYlOM/giphy.gif" alt="Face Recognition Animation">
</div>

## Overview

This project leverages the Face Recognition library in Python, along with other essential libraries such as OpenCV, NumPy, and MySQL Connector. It operates in real-time, capturing frames from a webcam, detecting faces, and comparing them to a reference database of individuals stored in the 'ImagesAttendance' folder.

## Key Features

- **Real-time Face Recognition:** The program continuously identifies faces in webcam frames.

- **Face Encoding Matching:** It matches detected faces with the stored face encodings of registered individuals.

- **Attendance Tracking:** Upon a successful match, attendance records are created, including the time of the match, and stored in real-time in an 'attendance.csv' file.

- **Data Persistence:** To ensure data permanence, users can press "q" to end the program, triggering the automatic transfer of recorded attendance data to a MySQL database.
![Project Screenshot](https://github.com/suyash-2004/Attendance_Automation/assets/61971096/62481c20-54a0-466a-b2fd-b237c13b672b)

# Methodology
## Retrieving Images and Generating Face Encodings:
  ### 1.)Loading Images:
  
<img src="https://github.com/suyash-2004/Attendance_Automation/assets/61971096/15a8fe56-cedf-4ccd-a053-20d8ecfc5ee5" alt="Screenshot" width="600"/>
  
  -The **getimages** function reads the CSV file **Attendance_Database.csv** and retrieves the image file names from the **"ImagesAttendance"** folder.
  -Images are loaded using OpenCV (**cv2.imread**) and appended to the **images** list.
  -Corresponding class names (student names) are added to the **classnames** list.

  ### 2.)Encoding Faces:
  
<img src="https://github.com/suyash-2004/Attendance_Automation/assets/61971096/80786a4b-a94c-4662-bd83-0627eca32176" alt="Screenshot" width="600"/>

  -The **find_encodings** function takes a list of images as input and encodes the faces in each image using the **face_recognition** library.
  -The encoding is performed in RGB format (**cv2.cvtColor(image, cv2.COLOR_BGR2RGB)**), and the encodings are added to the **encodlist**.

## Marking Attendance:

  ### 1.)Marking Attendance:

<img src="https://github.com/suyash-2004/Attendance_Automation/assets/61971096/356c5629-9f0f-4897-bc37-e7c2d6b3e2ca" alt="Screenshot" width="600"/>

  -The **mark_attendance** function is responsible for marking attendance in the CSV file (**attendance.csv**).
  -It reads the existing attendance data, checks if the current name is already in the list and if not, appends a new entry to the file with the corresponding details.

  ### 2.)Main Execution:
  -The main loop captures frames from the webcam, performs face recognition, and marks attendance when a recognized face matches a known face.
    
```
getimages()

print("Encoding Images")
time.sleep(0.5)
knownencodings = find_encodings(images)
print("Encoding Complete!")

default_table()
clear_attendance_file()

print("Opening WebCam")

time.sleep(0.3)

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
```
## Saving Attendance to Database:
  -Inside the while loop, the script checks if the user has pressed the 'q' key, If the condition is true, the following actions are taken:
      __Read Attendance Data from CSV:__
            -The script reads the attendance data from the CSV file ('**attendance.csv**'):
            
            <img src="https://github.com/suyash-2004/Attendance_Automation/assets/61971096/639dd3ab-08b8-4569-afa9-f770dd28b611" alt="Screenshot" width="600"/>
      __Update Database with Attendance Data:__
            -It processes each line of attendance data and updates the MySQL database:
            
            <img src="https://github.com/suyash-2004/Attendance_Automation/assets/61971096/da36580c-1ca7-4a89-b4f0-8d5fdfc36948" alt="Screenshot" width="600"/>
      __Commit Changes and Close Database Connection:__
            -After updating the database, it commits the changes and closes the database connection:
            
            <img src="https://github.com/suyash-2004/Attendance_Automation/assets/61971096/559750cc-0cbc-4b41-9a6d-1e88639c0f46" alt="Screenshot" width="600"/>

## Usage

Detailed instructions on setting up and running the project can be found in the project documentation.

## Future Enhancements

Future enhancements may include features such as automatic date and time stamping, a user-friendly graphical interface, and comprehensive logging for improved usability and error handling.


## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE) - see the [LICENSE.txt](LICENSE) file for details.

Feel free to explore the project, contribute, or adapt it for your own attendance tracking needs. Your feedback and contributions are welcome!
