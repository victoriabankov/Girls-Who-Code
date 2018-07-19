from PIL import Image

# Add commands to import modules here.
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    img = Image.open(filename)
    show_img(filename,img)
    return img

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(filename,img):
    img.show()
    save_img(filename,img)

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(filename,img):
    img.save(filename, "jpeg")

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img,filename):
    pixels = img.getdata()
    newpixels = []
    darkblue = (0,51,76)
    red = (217,26,33)
    lightblue = (112,150,158)
    yellow = (252,227,166)
    for p in pixels:
        intensity = p[0]+p[1]+p[2]
        if intensity < 182:
            newpixels.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            newpixels.append(red)
        elif intensity >= 364 and intensity < 546:
            newpixels.append(lightblue)
        elif intensity >=546:
            newpixels.append(yellow)
    newim = Image.new("RGB", img.size)
    newim.putdata(newpixels)
    show_img(filename,newim)
    return newim
