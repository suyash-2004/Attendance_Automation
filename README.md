<!DOCTYPE html>
<html>

<head>
    <title>Attendance Automation using Python with Face Recognition</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #007acc;
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        h1 {
            font-size: 36px;
        }

        section {
            padding: 20px;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        .gif {
            text-align: center;
        }

        footer {
            background-color: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
        }
    </style>
</head>

<body>

    <header>
        <h1>Attendance Automation using Python with Face Recognition</h1>
    </header>

    <section>
        <h2>Overview</h2>
        <p>This project leverages the Face Recognition library in Python, along with other essential libraries such as OpenCV, NumPy, and MySQL Connector. It operates in real-time, capturing frames from a webcam, detecting faces, and comparing them to a reference database of individuals stored in the 'ImagesAttendance' folder.</p>
    </section>

    <section>
        <h2>Key Features</h2>
        <ul>
            <li><strong>Real-time Face Recognition:</strong> The program continuously identifies faces in webcam frames.</li>
            <li><strong>Face Encoding Matching:</strong> It matches detected faces with the stored face encodings of registered individuals.</li>
            <li><strong>Attendance Tracking:</strong> Upon a successful match, attendance records are created, including the time of the match, and stored in real-time in an 'attendance.csv' file.</li>
            <li><strong>Data Persistence:</strong> To ensure data permanence, users can press "q" to end the program, triggering the automatic transfer of recorded attendance data to a MySQL database.</li>
        </ul>
    </section>

    <section>
        <h2>Usage</h2>
        <p>Detailed instructions on setting up and running the project can be found in the project documentation.</p>
    </section>

    <section>
        <h2>Future Enhancements</h2>
        <p>Consider adding features such as automatic date and time stamping, a user-friendly graphical interface, and comprehensive logging for improved usability and error handling.</p>
    </section>

    <section class="gif">
        <img src="your-image.png" alt="Project Screenshot">
        <p>GIFs and images can be used to demonstrate your project visually.</p>
    </section>

    <footer>
        <p>Feel free to explore the project, contribute, or adapt it for your own attendance tracking needs. Your feedback and contributions are welcome!</p>
    </footer>

</body>

</html>
