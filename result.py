import PIL.Image
import PIL.ImageDraw
import face_recognition as fr
import matplotlib.pyplot as plt
import os

filename = "./Images/3.jpeg"
image1 =fr.load_image_file(filename)
 
face_loc = fr.face_locations(image1)

if (len(face_loc) == 0):
	os.remove(filename)