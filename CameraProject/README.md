Camera Project by Jonathan Greenberg and David Furfaro




Description: This project provides a Web Interface that streams video from a Pi Camera Module. The interface allows movement of the camera through the use of two micro servos and allows the user to take and store a picture from the Pi Camera Module. The interface all can display the picture taken.





Required Hardware:

Raspberry Pi 2

Camera Module

Servo Controller Board

2 Micro Servos

Screw, Platic Mounts


Software needed to Install on PI:

ServoBlaster   -------------->  https://www.raspberrypi.org/forums/viewtopic.php?f=44&t=54067

Mjpg-Streamer  -------------->  http://blog.cudmore.io/post/2015/03/15/Installing-mjpg-streamer-on-a-raspberry-pi/

Flask ----------------> https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/












Assuming you have installed the required software, before running the python script a few commands must be made in the terminal:


To start the stream:

mkdir /tmp/stream

raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &


LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"



To enable ServoBlaster:


cd PiBits/ServoBlaster

sudo make

sudo ./servod





To run the script:

Go to the directory containing the "testcam.py" script then run the following command ------>  python testcam.py

The terminal will provied you with information on what port it is using.

Enter your web browser and change the address to localhost:####                       #### ------->(port provided in terminal)










Notes about the project:

The project uses Raspistill and Mjpeg for the camera module. As a result you must "Stop Stream" before taking a picture.

The current python script does not alter the name of the file for the image taken. As a result only one image can be stored.
















