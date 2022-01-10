"""
A camera class

This is a module for camera on the laptop

Author: Zhaoliang (zhz03@g.ucla.edu)

Notes
_____
Running this code require cv2:

link: https://pypi.org/project/opencv-python/
$ pip install opencv-python

"""


import cv2

class camera:
	def __init__(self):
		pass

	def getPicture(self,index,path):
		"""
	    Take a picture and save the images
	    
	    Parameters
	    ----------
	    index: int
	    	the index of the camera that we need to use 
	    path: string
	    	the path that we want to store our capture images

	    Returns
	    -------
	    Out: show a picture that we took from the index camera
	    """

	    cv2.namedWindow('camera',1) # "1" means that windows can't be dragged easily
	   	# call the index camera
	   	cap = cv2.VideoCapture(index) 
	   	ret,frame = cap.read() # read the camera frame
	   	cv2.imwrite(path+".jpg",frame) # save to the path

	   	# release the camera
	   	cap.release()
	   	# shot down the windows()
	   	cv2.destroyWindow("camera")
	   	

if __name__ == '__main__':
	cam = camera()
	index = 0
	path = "./"
	cam.getPicture(index,path)