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
  
  <iframe src="main_execution_code.html" width="100%" height="350px" style="border: none;"></iframe>


## Usage

Detailed instructions on setting up and running the project can be found in the project documentation.

## Future Enhancements

Future enhancements may include features such as automatic date and time stamping, a user-friendly graphical interface, and comprehensive logging for improved usability and error handling.


## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE) - see the [LICENSE.txt](LICENSE) file for details.

Feel free to explore the project, contribute, or adapt it for your own attendance tracking needs. Your feedback and contributions are welcome!
