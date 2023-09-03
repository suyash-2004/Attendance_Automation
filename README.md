# Attendance Automation using Python with Face Recognition

Welcome to the Attendance Automation project! This is a mini project for my 2nd year (3rd semester) coursework, focusing on automating attendance tracking through the power of Python with face recognition.

![Face Recognition Animation](https://media.giphy.com/media/3o7abnQiguzMTaYlOM/giphy.gif)

## Overview

This project leverages the Face Recognition library in Python, along with other essential libraries such as OpenCV, NumPy, and MySQL Connector. It operates in real-time, capturing frames from a webcam, detecting faces, and comparing them to a reference database of individuals stored in the 'ImagesAttendance' folder.

## Key Features

- **Real-time Face Recognition:** The program continuously identifies faces in webcam frames.

- **Face Encoding Matching:** It matches detected faces with the stored face encodings of registered individuals.

- **Attendance Tracking:** Upon a successful match, attendance records are created, including the time of the match, and stored in real-time in an 'attendance.csv' file.

- **Data Persistence:** To ensure data permanence, users can press "q" to end the program, triggering the automatic transfer of recorded attendance data to a MySQL database.
![Project Screenshot](https://github.com/suyash-2004/Attendance_Automation/assets/61971096/62481c20-54a0-466a-b2fd-b237c13b672b)

## Usage

Detailed instructions on setting up and running the project can be found in the project documentation.

## Future Enhancements

Consider adding features such as automatic date and time stamping, a user-friendly graphical interface, and comprehensive logging for improved usability and error handling.





GIFs and images can be used to demonstrate your project visually.

Feel free to explore the project, contribute, or adapt it for your own attendance tracking needs. Your feedback and contributions are welcome!
