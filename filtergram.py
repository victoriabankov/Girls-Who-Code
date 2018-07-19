import filters
yes = ["yes", "ya", "y"]
no = ["no", "nah", "n"]
def main():
    filename = input("What is the file name of the picture you would like to edit?")
    print(filename)
    img = filters.load_img(filename)
    filters.show_img(filename,img)
    filter = input("Which filter would you like to use? \n Filter 1 \n Filter 2 \n Filter 3 \n Exit")
    if (filter == "filter 1"):
        filters.obamicon(img,filename)
        save = input("Would you like to save your image?")
        if save in yes:
            filters.save_img(filename, img)
        elif save in no:
            quit()
        else:
            save = input("Would you like to save your image?")
    elif (filter == "filter 2"):
#add filter 2
        save = input("Would you like to save your image?")
        if save in yes:
            save_img(filename, img)
        elif save in no:
            quit()
        else:
            save = input("Would you like to save your image?")
    elif (filter == "filter 3"):
#add filter 3
        save = input("Would you like to save your image?")
        if save in yes:
            save_img(filename, img)
        elif save in no:
            quit()
        else:
            save = input("Would you like to save your image?")
    elif (filter == "exit")
        quit()
    else:
        filter = input("Which filter would you like to use? \n Filter 1 \n Filter 2 \n Filter 3 \n Exit")

main()
