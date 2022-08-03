from asyncore import write
from time import time
import pytesseract
pytesseract.pytesseract.cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os, os.path
from datetime import date, datetime, timedelta,time

imgs = []
path = "./put_here"
valid_images = [".jpg",".png"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append([f,Image.open(os.path.join(path,f))])

print("{0} image files found.".format(str(len(imgs))))

new = open("./outputs/{0}.txt".format(str(datetime.now()).replace(":","_").replace(".","_")),"w");
new.write(str(len(imgs)) + " image files found.\n")
for i in imgs:
    print(i[0],i[1]);
    text = pytesseract.image_to_string(i[1])
    print(text)
    new.write("******************************************\n" + str(i[0]) + "," + str(i[1])+"\n\n\n"+str(text)+"\n")
new.close()