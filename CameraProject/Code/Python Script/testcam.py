from flask import Flask, render_template, request, redirect, send_from_directory
from time import sleep
import datetime
import os
import subprocess
import sys



app = Flask(__name__, static_folder='static',static_url_path='/static')

position = 0


################################ This is routes you to the main page when running the script#################
@app.route('/')
def TakeStill():
	#global position
	position = 120
	return render_template('takepic.html')

##############################################################################################################


######################################################## This function takes a picture and stores it in specified directory#######################
@app.route('/takepic', methods = ['GET','POST'])
def TakePic():
	path = "raspistill -o /home/pi/CameraProject/images/1pic.jpg"
	os.system(path)
	return render_template('takepic.html')



###################################################################################################################################################




######################################################################## Both below functions below restart the stream (never fully worked due to a problem wit the server)#######################

@app.route('/restartstream', methods = ['GET','POST'])
def Restart():
	os.system("LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i 'input_file.so -f /tmp/stream -n pic.jpg' -o 'output_http.so -w /usr/local/www'")
	os.wait()
	return render_template('takepic.html')


@app.route('/prepstream', methods = ['GET','POST'])
def PrepStream():
	os.system("raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &")
	return render_template('takepic.html')

###########################################################################################################################################################################







############################################################## Theses functions reroute the client to a template containing the pictures taken in the directory in the TakePic function   ################################
@app.route('/showpic', methods = ['GET','POST'])
def ShowPics():
	image_names= os.listdir('./images')
	return render_template('showpic.html',image_names=image_names)

@app.route('/LearningPython/<filename>')
def send_image(filename):
	return send_from_directory("images", filename)

#########################################################################################################################################################################################	









####################################################### The below function kills the stream so the user can take a picture ################################


@app.route('/stopstream', methods = ['GET','POST'])
def StopStream():
	os.system("pkill raspistill")
	os.system("pkill mjpg_streamer")
	return render_template('takepic.html')


#######################################################################################################################################################################






#-------------------------------------------------------Buttons for pointing the camera-----------
@app.route('/80', methods = ['GET','POST'])
def Eighty():
	os.system("echo 5=80 > /dev/servoblaster")
	return render_template('takepic.html')

@app.route('/90', methods = ['GET','POST'])
def Ninety():
	os.system("echo 5=90 > /dev/servoblaster")
	return render_template('takepic.html')

@app.route('/100', methods = ['GET','POST'])
def Hundred():
	os.system("echo 5=100 > /dev/servoblaster")
	return render_template('takepic.html')

@app.route('/110', methods = ['GET','POST'])
def Hundred10():
	os.system("echo 5=110 > /dev/servoblaster")
	return render_template('takepic.html')


@app.route('/center', methods = ['GET','POST'])
def CenterCam():
	os.system("echo 5=120 > /dev/servoblaster")
	return render_template('takepic.html')
 

@app.route('/130', methods = ['GET','POST'])
def HundredThirty():
	os.system("echo 5=130 > /dev/servoblaster")
	return render_template('takepic.html')


@app.route('/140', methods = ['GET','POST'])
def HundrdFourty():
	os.system("echo 5=140 > /dev/servoblaster")
	return render_template('takepic.html')

@app.route('/150', methods = ['GET','POST'])
def HundredFifty():
	os.system("echo 5=150 > /dev/servoblaster")
	return render_template('takepic.html')

@app.route('/160', methods = ['GET','POST'])
def HundredSixty():
	os.system("echo 5=160 > /dev/servoblaster")
	return render_template('takepic.html')

#---------------------------------------------------------------------------
















if __name__ == '__main__':
    app.run()
