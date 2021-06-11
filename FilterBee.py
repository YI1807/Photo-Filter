from tkinter import*
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk

root = Tk()
filename1 = ''
image1=''
gray_image=''
inverted_image=''
blurred=''
bllurred=''
inverted_blurred=''
pencil_sketch=''
imgCanny=''
imgDial=''
def browsefunc():
    global filename1
    global image1
    global gray_image
    global inverted_image
    global blurred
    global bllurred
    global inverted_blurred
    global pencil_sketch
    global imgCanny
    global imgDial
    filename1 = filedialog.askopenfilename()
    root.filename = filename1
    filename1=filename1.replace('/','\\\\')
    image1 = cv2.imread(filename1)
    gray_image=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    inverted_image=255-gray_image
    blurred=cv2.GaussianBlur(image1,(21,21),0)
    bllurred=cv2.GaussianBlur(inverted_image,(21,21),0)
    inverted_blurred=255-bllurred
    pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
    imgCanny = cv2.Canny(image1, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)

canvas = Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

root.geometry("1000x600")
root.title("Filter Bee")
root.resizable(False,False)

#Login Frame
Frame_Login=Frame(root,bg="White")
Frame_Login.place(x=155,y=150,height=1000,width=1000)
#logo
logo = Image.open('Y:\\College\\Python\\Project\\logo.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.place(x=0, y=0)
# Label
PELbl=Label(text='Select the Filter',fg='Black',font=('Times New Roman','20')).place(x=400,y=200)
#instructions
instructions = Label(root, text="Photo Editor", font=('Raleway','28'))
instructions.place(x=400, y=50)


def image():
    cv2.imshow("Original", image1)
    cv2.waitKey(0)
def gray():
    cv2.imshow("Gray",gray_image)
    cv2.waitKey(0)
def invertedd():
    cv2.imshow("Inverted",inverted_image)
    cv2.waitKey(0)
def blurredd():
    cv2.imshow("Blurred", blurred)
    cv2.waitKey(0)
def sketch():
    cv2.imshow("pencil sketch", pencil_sketch)
    cv2.waitKey(0)
def canny():
    cv2.imshow("Canny",imgCanny)
def Dilate():
    cv2.imshow("dilate",imgDial)
def Invert_blur():
    cv2.imshow("Invert_Blur",inverted_blurred)

browsebutton = Button(root, text="Browse", command=browsefunc).place(x = 160, y = 120)
button_image= Button(root, text='Original',command=image).place(x=250,y=300,width=100)
button_gray= Button(root, text='Gray',command=gray).place(x=250,y=340,width=100)
button_invert= Button(root, text='Invert',command=invertedd).place(x=550,y=300,width=100)
button_blur=Button(root, text='blur',command=blurredd).place(x=550,y=340,width=100)
button_sketch=Button(root,text='Sketch',command=sketch).place(x=250,y=380,width=100)
button_dilute=Button(root,text='Dilate',command=Dilate).place(x=550,y=380,width=100)
button_canny=Button(root,text='Canny',command=canny).place(x=250,y=420,width=100)
button_canny=Button(root,text='Inverted_Blurred',command=Invert_blur).place(x=550,y=420,width=100)

root.mainloop()