'''
===============================================================================
Interactive Manga Colorization.
USAGE:
    python main.py <filename>
README FIRST:
    Two windows will show up, one for input and one for output.
    At first, in input window, draw a rectangle around the object using
mouse right button. Then press 'n' to segment the object (once or a few times)
For any finer touch-ups, you can press any of the keys below and draw lines on
the areas you want. Then again press 'n' for updating the output.
Key '0' - To do intensity continuous colorization
Key '1' - To do pattern continuous colorization
Key ctrl + 'c' - To stop level set method
===============================================================================
'''
# from scipy.misc.pilutil import imread
# from scipy.misc import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import webcolors
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as filters
from skimage.draw import polygon, polygon_perimeter
from skimage import measure
import cv2
import level_set
import pattern_continuous
import numpy as np
import sys

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
current_former_x,current_former_y = -1,-1
ix, iy = -1, -1
img = 0
r = 0
g = 0
b = 0

def nothing(x):
    pass

# mouse callback function
def paint_draw(event,former_x,former_y,flags,param):
    global current_former_x,current_former_y,drawing, mode, r, g, b
    #to see when the user starts scribbling
    if event==cv2.EVENT_LBUTTONDOWN:
        # means that he has started to draw
        drawing=True
        current_former_x,current_former_y=former_x,former_y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.line(img,(current_former_x,current_former_y),(former_x,former_y),(b,g,r),5)
                current_former_x = former_x
                current_former_y = former_y
    elif event==cv2.EVENT_LBUTTONUP:
        #we see the last point where the user has stopped the scribbling and take that as the starting point
        drawing=False
        if mode==True:
            cv2.line(img,(current_former_x,current_former_y),(former_x,former_y),(b,g,r),5)
            current_former_x = former_x
            current_former_y = former_y
    return former_x,former_y

def run():
    global current_former_x,current_former_y,drawing, mode, r, g, b, img

	# iter_inner, iter_outer, lamda, alpha, epsilon, sigma, dt, potential_function
	# potential_function="single-well"
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    colimg = cv2.imread(filename)
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    # output = image.copy()
    output = cv2.imread(filename)
    img = output.copy()
	# plt.imshow(image)
	# plt.show()
	# print(image.shape)
    color = np.zeros((10,10,3), np.uint8)
    #create three windows and name them
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('output', cv2.WINDOW_NORMAL)
    cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)
	#cv2.namedWindow('trackbar')
	#cv2.resizeWindow('trackbar', (10,10))
    #this attaches the mouse callback to paint_draw function so that we know when the user scribbles and where 
    # he scribbles 
    cv2.setMouseCallback('image', paint_draw)
    #create trackbar in order to select color
    cv2.createTrackbar('R','trackbar',0,255, nothing)
    cv2.createTrackbar('G','trackbar',0,255, nothing)
    cv2.createTrackbar('B','trackbar',0,255, nothing)
    # while(1):
    #     cv2.imshow('image',image)
    #     if cv2.waitKey(20) & 0xFF == 27:
    #         break
    #     r = cv2.getTrackbarPos('R','image')
    #     g = cv2.getTrackbarPos('G','image')
    #     b = cv2.getTrackbarPos('B','image')
    # cv2.destroyAllWindows()

	# #image1 = np.array(image1,dtype='float32')
    # LS = levelSet(4,50,2,-9,2.0,0.8)
    # print(current_former_x, current_former_y)
    # boundary, F= LS.gradientDescent(image1[:,:,0],current_former_y,current_former_x)
	#print(boundary)
	# img_yuv = cv2.cvtColor(image1, cv2.COLOR_BGR2YUV)
	# yuv = RGB2YUV(np.asarray([r,g,b]).reshape((3,1)))
	# print(yuv, F.shape)
	# #F= LS.calculateF(img_yuv)
	# xyz = cv2.filter2D(np.square(1-F),-1,yuv[0])
	# img_yuv[:,:,0] = xyz
	# cv2.imshow("sdjkfnskj",cv2.cvtColor(img_yuv, cv2.COLOR_LUV2RGB))
	# cv2.waitKey(0)
    # LS.fillColor(image1,boundary,(b,g,r))
    sys.stdin.flush()
    alpha = None
    while(1):
        cv2.imshow('output', output)
        cv2.imshow('image',img)
        cv2.imshow('trackbar', color)
        r = cv2.getTrackbarPos('R','trackbar')
        g = cv2.getTrackbarPos('G','trackbar')
        b = cv2.getTrackbarPos('B','trackbar')
        color[:] = b, g, r
        k = cv2.waitKey(10)
#         print("hello1")
        # print(k)
        # key bindings
        if k == 27:         # esc to exit
#             print("debug")
            break

        elif k == ord('0'):
            if alpha == None:
                LS = level_set.levelSet(4,10000,2,-90,2.0,0.8)
            else:
                LS = level_set.levelSet(4,10000,2,alpha,2.0,0.8)
            curcolor = (b,g,r)
#             print("start gd")
            boundary, F,out = LS.gradientDescent(image,current_former_y,current_former_x)
#             print("ctrlc pressed")
#             plt.imshow(out)
#             print(image.shape)
#             print(out.shape)
#             fin = np.zeros((image.shape[0],image.shape[1],3))
#             fin = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
            dup = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
            colimg = cv2.cvtColor(colimg,cv2.COLOR_BGR2RGB)
            colimg[out != 0] = (r,g,b)
            colimg[image < 40] = (2,2,2)
            cv2.imshow('output', cv2.cvtColor(colimg,cv2.COLOR_RGB2BGR))
            cv2.imwrite("res.png", cv2.cvtColor(colimg,cv2.COLOR_RGB2BGR))
            plt.figure()
            plt.imshow(colimg)
            plt.show()
#             print("debug")
#             output = LS.fillColor(output,boundary,(curcolor))

#             print("saved")
        elif k == ord('1'):
#             print("debug1")
            if alpha == None:
                LS = pattern_continuous.levelSet_pattern(10,10000,2,-5000000,2,1)
            else:
                LS = pattern_continuous.levelSet_pattern(10,10000,2,alpha,2,1)
            curcolor = (b,g,r)
#             print("hello")
            phi, F = LS.gradientDescent(image,current_former_y,current_former_x)
            while(1):
                colortype = input("Enter 1 for pattern to shading and 2 for stroke preserving colorization:")
                if colortype == '1':
                    output = LS.pattern2shading(output,(curcolor))
                    break
                elif colortype == '2':
                    output = LS.strokepreserving(output,(curcolor))
                    break
#                 elif colortype == '3':
                else:
                    print("Wrong Input, Enter Again!")
            cv2.imwrite("res.png", output)
    print('Done')

if __name__ == '__main__':
    print(__doc__)
    run()
    cv2.destroyAllWindows()