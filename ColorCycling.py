#colaboration Statement
#Rene Borr
#R00805596
#On my honor, I have not given, nor received, nor witnessed any unauthorized assistance on this work.

#I worked on this assignment alone, and refered to:
   #https://blog.prototypr.io/color-cycling-in-pixel-art-c8f20e61b4c4
    
#Source images
    #http://pixeljoint.com/pixelart/101623.htm (aurora)
    #http://pixelartmaker.com/art/7e2d218baaa3eb7 (fire)
    #http://piq.codeus.net/picture/69576/escher_s_waterfall (waterfall)
    #http://pixeljoint.com/pixelart/69825.htm (pond)



import numpy as np
import cv2

#load global Variables
image = cv2.imread("pond.png",1)
palate = []

"""
main

The main function does not take any arguments or return anything.
Run the main statement to see the color cycling images while holding space
*uncomment/comment out sections to see all 4 examples
"""
def main():
   
    pointer_array = []
    
    palate = make_palate(image)
    print("palate made")
    
    #pond
    move_to_back(17)
    move_to_back(10)
    move_to_back(9)
    
    rows, cols = image.shape[:2]
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(palate[get_num(image[r][c])])
        pointer_array.append(row)
        
    print("image loaded")
    
    
    while(True):
        
        show = np.asarray(pointer_array)
        
        cv2.imshow('image',show)
        cv2.imshow('palate',convert_palate_to_image(palate))
        
    
        
        #fire
        #shiftPalate(1,3)
        
        #waterfall
        #shiftPalate(14,21)
        #shiftPalate(51,54)
        #shiftPalate(60,63)
        #shiftPalate(30,32)
        #shiftPalate(47,48)
        
        #pond
        shiftPalate(2,8)
        shiftPalate(16,18)
        
        #Aurora
        #shiftPalate(1,3)
         
         
         
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        
    cv2.destroyAllWindows()

    
   
    
"""
make_palate

this function takes an image, and returns a list of all colors found in the images

Args:
        image (numpy.ndarray): A image represented in a numpy array.
        
Returns:
        palate (list of colors in red green and blue)
"""
def make_palate(image):
    
    
    rows, cols = image.shape[:2]
    for r in range(rows):
        for c in range(cols):
            if(is_in(palate,image[r][c]) == False):
                palate.append(image[r][c])
        
    
    return palate

"""
move_to_back

takes the selected value in palate, and moves it to the back

Args:
        i (int): the index of the pixel to move to the back
"""
def move_to_back(i):
    value = palate.pop(i)
    palate.append(value)
    
"""
is_in

returns true if if the color is in the imput image

Args:
        image(np.ndarray): the picture to search for the color in
        color(RGB values): the color to try to find
Returns:
        Boolean (True/False)
"""
def is_in(image,color):
    for r in range(len(image)):
        if(image[r][0] == color[0] and image[r][1] == color[1] and image[r][2] == color[2]):
            return True
    return False

"""
convert_palate_to_image

converts the palate to a comprehensible image

Args:
        palate(list of RGB values): the palate to be converted
Returns:
        comp(np.ndarray): a picture version of the palate
"""
def convert_palate_to_image(palate):
    
    size = len(palate)
    cols = size//5 +1
    comp = np.zeros([cols*50,250,3],dtype=np.uint8)
    comp[:] = (255,255,255)
    row = 0
    col = 0
    for i in range(len(palate)):  
        comp[col*50:col*50+50,row*50:row*50+50] = palate[i]
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(comp, str(i), (row*50, col*50+15), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        
        row = row+1
        if(row==5):
            row = 0
            col = col+1
            
    return comp
    
"""
get_num

gives the index location of the specified color in the palate

Args:
        color(RGB values:the color to find in the palate
Returns:
        int: the current index location of the color
"""
def get_num(color):
    image = palate
    for r in range(len(image)):
        if(image[r][0] == color[0] and image[r][1] == color[1] and image[r][2] == color[2]):
            return r
        
    return 0

"""
shiftPalate

shifts the palates colors one round from the start value to the end value specified

Args:
    start(int): the starting location
    end(int): the ending location
"""
def shiftPalate(start,end):
    last = palate[start].copy()
    for i in range(start,end):
        convert(palate[i],palate[i+1])
        
    convert(palate[end],last)
    
"""
convert
converts the specified pixel to the specified color without changing its location in memory

Args:
        pixel (RGB values): The pixel to be converted
        color (RBG values): the color for the pixel to be converted to
"""
def convert(pixel,color):
    pixel[0] = color[0]
    pixel[1] = color[1]
    pixel[2] = color[2]
      
main()