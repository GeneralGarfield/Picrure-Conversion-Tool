


#Fixed
# Libraries
import tkinter as tk

import tkinter.font as font

from tkinter import Menu, filedialog, messagebox

from tkinter import *

from tkinter import ttk

import os

import webbrowser

from PIL import Image, ImageTk


import subprocess








# Functions for the Menu




def file_opener():
    # Open the file dialog and return the selected file path
    try:
        
        file = filedialog.askopenfile(mode="r", filetypes=[("All Files", "*.jpeg *.png *.ico")])
    
        if file:

            return file.name
    
        return None

    except:


        tk.messagebox.showerror(title= "Error", message= "File May be Corrupted or File name is too large to read.")

def link_to_source():
    
    webbrowser.open_new_tab("https://github.com/GeneralGarfield/Image-Conversion-Tool/tree/main")

def link_to_github():
    
    webbrowser.open_new_tab("https://github.com/GeneralGarfield")

def radiobuttons():
   
   selection = int(var.get())


   return selection

def imageopener_and_Conversion():



    
    def Conversion1():

        
        try:

            user_input = str(entry1.get())



        
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Path to the "output" folder inside the script directory
            output_path = os.path.join(script_dir, "Conversions")

            if not os.path.exists(output_path):

                tk.messagebox.showwarning(title="No Folder Found", message="The Conversions folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path)

        
            script_dir = os.path.dirname(os.path.abspath(__file__))

                # Path to the "output" folder inside the script directory
            output_path1 = os.path.join(script_dir, "Conversions/PDF")

            if not os.path.exists(output_path1):

                tk.messagebox.showwarning(title="No Folder Found", message="The PDF folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path1)

            output_path2 = os.path.join(script_dir, "Conversions/JPEG")

            if not os.path.exists(output_path2):

                tk.messagebox.showwarning(title="No Folder Found", message="The JPEG folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path2)

            output_path3 = os.path.join(script_dir, "Conversions/ICO")

            if not os.path.exists(output_path3):

                tk.messagebox.showwarning(title="No Folder Found", message="The ICON folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path3)

            output_path4 = os.path.join(script_dir, "Conversions/PNG")

            if not os.path.exists(output_path4):

                tk.messagebox.showwarning(title="No Folder Found", message="The PNG folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path4)

            output_path5 = os.path.join(script_dir, "Conversions/PPM")

            if not os.path.exists(output_path5):

                tk.messagebox.showwarning(title="No Folder Found", message="The PPM folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path5)
            output_path6 = os.path.join(script_dir, "Conversions/PGM")

            if not os.path.exists(output_path6):

                tk.messagebox.showwarning(title="No Folder Found", message="The PGM folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path6)
            output_path7 = os.path.join(script_dir, "Conversions/PBM")

            if not os.path.exists(output_path7):

                tk.messagebox.showwarning(title="No Folder Found", message="The PBM folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path7)
            output_path8 = os.path.join(script_dir, "Conversions/BMP")

            if not os.path.exists(output_path8):

                tk.messagebox.showwarning(title="No Folder Found", message="The BMP folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path8)

            output_path9 = os.path.join(script_dir, "Conversions/TIFF")

            if not os.path.exists(output_path9):

                tk.messagebox.showwarning(title="No Folder Found", message="The TIFF folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path9)
            output_path10 = os.path.join(script_dir, "Conversions/Webp")
            if not os.path.exists(output_path10):

                tk.messagebox.showwarning(title="No Folder Found", message="The Webp folder was not found. The Conversion folder will be Created")

                os.makedirs(output_path10)




        

        
        
            value = radiobuttons()

            output1 = "Conversions/PDF"

            output2 = "Conversions/JPEG"

            output3 = "Conversions/ICO"

            output4 = "Conversions/PNG"

            output5 = "Conversions/PPM"

            output6 = "Conversions/PGM"

            output7 = "Conversions/PBM"

            output8 = "Conversions/BMP"

            output9 = "Conversions/TIFF"

            output10 = "Conversions/Webp"

            file_path_to_output_pdf = f"{output1}/{user_input}.pdf"

            file_path_to_output_Jpeg = f"{output2}/{user_input}.jpeg"

            file_path_to_output_ico = f"{output3}/{user_input}.ico"

            file_path_to_output_png = f"{output4}/{user_input}.png"

            file_path_to_output_ppm = f"{output5}/{user_input}.ppm"

            file_path_to_output_pgm = f"{output6}/{user_input}.pgm"

            file_path_to_output_pbm = f"{output7}/{user_input}.pbm"

            file_path_to_output_bmp = f"{output8}/{user_input}.bmp"

            file_path_to_output_tiff = f"{output9}/{user_input}.tiff"

            file_path_to_output_webp = f"{output10}/{user_input}.webp"

        
            if value == 1:

                def this_sucks_balls1():

                    try:


                        if os.path.exists(file_path_to_output_pdf):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                               
                                image = Image.open(file_path)


                                image.save(f"{output1}/{user_input}.pdf")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            
                            image = Image.open(file_path)

                            image.save(f"{output1}/{user_input}.pdf")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls1()
                

# -----------------------------------------------------
            elif value == 2:

                def this_sucks_balls2():


                    try:


                        if os.path.exists(file_path_to_output_Jpeg):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path).convert("RGB")

                                image.save(f"{output2}/{user_input}.jpeg")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            image = Image.open(file_path).convert("RGB")

                            image.save(f"{output2}/{user_input}.jpeg")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                
                    except:

                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls2()


# -----------------------------------------------------


            elif value == 3:

                def this_sucks_balls3():

                    try:


                        if os.path.exists(file_path_to_output_ico):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path)

                                image.save(f"{output3}/{user_input}.ico")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            image = Image.open(file_path)

                            image.save(f"{output3}/{user_input}.ico")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls3()
# -----------------------------------------------------

            elif value == 4:

                def this_sucks_balls4():

                    try:


                        if os.path.exists(file_path_to_output_png):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path)

                                image.save(f"{output4}/{user_input}.png")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            image = Image.open(file_path)

                            image.save(f"{output4}/{user_input}.png")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls4()
# -----------------------------------------------------

            elif value == 5:

                def this_sucks_balls5():

                    try:


                        if os.path.exists(file_path_to_output_ppm):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path).convert("L")

                            

                                image.save(f"{output5}/{user_input}.ppm")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:
                            image = Image.open(file_path).convert("L")
                            image.save(f"{output5}/{user_input}.ppm")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls5()
# -----------------------------------------------------

            elif value == 6:
                def this_sucks_balls6():

                    try:

                        if os.path.exists(file_path_to_output_pgm):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path).convert("L")

                                image.save(f"{output6}/{user_input}.pgm")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            image = Image.open(file_path).convert("L")

                            image.convert("L")

                            image.save(f"{output6}/{user_input}.pgm")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls6()
# -----------------------------------------------------

            elif value == 7:

                def this_sucks_balls7():

                    try:

                        if os.path.exists(file_path_to_output_pbm):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:
                                
                                image = Image.open(file_path).convert("L")
                            

                                image.save(f"{output7}/{user_input}.pbm")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            image = Image.open(file_path).convert("L")

                            image.save(f"{output7}/{user_input}.pbm")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")

                this_sucks_balls7()

# -----------------------------------------------------

            elif value == 8:
                def this_sucks_balls8():

                    try:
                        if os.path.exists(file_path_to_output_bmp):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path)

                                image.save(f"{output8}/{user_input}.bmp")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:
                            image = Image.open(file_path)
                            image.save(f"{output8}/{user_input}.bmp")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls8()
# -----------------------------------------------------

            elif value == 9:
                def this_sucks_balls9():

                    try:

                        if os.path.exists(file_path_to_output_tiff):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path)

                                image.save(f"{output9}/{user_input}.tiff")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")
                
                        else:
                            image = Image.open(file_path)
                            image.save(f"{output9}/{user_input}.tiff")

        
                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls9()

# -----------------------------------------------------

            elif value == 10:
                def this_sucks_balls_number_fucking_10():
                
                    try:

                        if os.path.exists(file_path_to_output_webp):

                            yesorno = tk.messagebox.askyesno(title = "Overwrite", message = "A file with that name exists already. Would you like to overwrite your file?")

                            if yesorno == True:

                                image = Image.open(file_path)

                                image.save(f"{output10}/{user_input}.webp")

                                tk.messagebox.showinfo(title= "Success", message= "File Converted successfully!")

                            elif yesorno == False:

                                tk.messagebox.showinfo(title= "Name Error", message = "File was not converted. Change the file name into a new name.")

                        else:

                            image = Image.open(file_path)
                    
                            image.save(f"{output10}/{user_input}.webp")

                            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
                    
                    except:
                        tk.messagebox.showerror(title = "ERROR", message= "An error has occured. The file may have not been named. If that's not the case please Report!")
                this_sucks_balls_number_fucking_10()

        except:
                tk.messagebox.showerror(title= "CRITICAL ERROR", message= "A CRITICAL ERROR HAS OCCURED! PLEASE RESTART!")
                

# -----------------------------------------------------        

#-------------------------------------------------------------End of Function

    file_path = file_opener() # Get the file path from file_opener
    

    try:
        if file_path:

            image = Image.open(file_path)

        # Resize the image to desired size
            resized_image = image.resize((100, 100))  # Make sure to use a tuple

        # Convert to a PhotoImage object
            image_tk = ImageTk.PhotoImage(resized_image)

        # Display in label
            label = tk.Label(root, image=image_tk)

            label.image = image_tk  # Keep reference

            label.place(x= 15, y=150)

        # Displays top Text
            text_for_image = tk.Label(text="Image File")

            text_for_image.place(x= 15, y=100)

        #Creates the RadioButtons for options
        
            PDF_for_conversion = tk.Radiobutton(text="PDF", variable=var, value=1, command=radiobuttons)

            JPEG_for_conversion = tk.Radiobutton(text="JPEG", variable=var, value=2, command=radiobuttons)

            ICO_for_conversion = tk.Radiobutton(text="ICO", variable=var, value=3, command=radiobuttons)

            PNG_for_conversion = tk.Radiobutton(text="PNG", variable=var, value=4, command=radiobuttons)

            PPM_for_conversion = tk.Radiobutton(text="PPM", variable=var, value=5, command=radiobuttons)

            PGM_for_conversion = tk.Radiobutton(text="PGM", variable=var, value=6, command=radiobuttons)

            PBM_for_conversion = tk.Radiobutton(text="PBM", variable=var, value=7, command=radiobuttons)

            BMP_for_conversion = tk.Radiobutton(text="BMP", variable=var, value=8, command=radiobuttons)

            TIFF_for_conversion = tk.Radiobutton(text="TIFF", variable=var, value=9, command=radiobuttons)

            Webp_for_conversion = tk.Radiobutton(text="Webp", variable=var, value=10, command=radiobuttons)

            PDF_for_conversion.place(x= 200, y=130)

            JPEG_for_conversion.place(x= 200, y=150)

            ICO_for_conversion.place(x= 200, y=170)

            PNG_for_conversion.place(x= 200, y=190)

            PPM_for_conversion.place(x= 200, y = 210)

            PGM_for_conversion.place(x=200, y=230)

            PBM_for_conversion.place(x=200, y=250)

            BMP_for_conversion.place(x=200, y=270)

            TIFF_for_conversion.place(x=200, y=290)

            Webp_for_conversion.place(x=200, y=310)


            Conversion_button = tk.Button(text="Convert!", command=Conversion1)

            Conversion_button.place(x=400, y=200)

            entry1 = tk.Entry(root, width=30)
        
            entry1.place(x=350, y =140)


            text4.place(x=200, y=100)

            text5.place(x=400, y=100)

    except:
        tk.messagebox.showerror(title= "Error", message= "Unable to open file. File May be Corrupted or File name is too large to read.")
def Conversions():

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the "output" folder inside the script directory
    output_path = os.path.join(script_dir, "Conversions")

    # Check if the path actually exists
    if not os.path.exists(output_path):

        tk.messagebox.showwarning(title="No Folder Found", message="The Conversions folder was not found. The Conversion folder will be Created")


        os.makedirs(output_path)
    
    # Open the folder in File Explorer
    subprocess.run(["explorer", output_path])








# -----------------------------------------------------------------------------------------------------------------------------

    #                           
    # 
    #                                       END OF THE FUNCTIONS 
    #
    #                                                               
    #                                                               #

#   -------------------------------------------------------------------------------------------------------
#                                           

#                                           START OF THE WINDOW

#
#   ____________________________________________________________________________________________________________________________
# Opens file for the icon



# Creat


try:
    directory_path = os.path.dirname(__file__)

    file_path = os.path.join(directory_path, 'Icon.ico')

    if os.path.exists(file_path):

        root = tk.Tk()

        root.title("Converter")

        directory_path = os.path.dirname(__file__)

        root.iconbitmap(file_path)

    elif not os.path.exists(file_path):

        tk.messagebox.showerror(title= "No icon file found", message = "Icon File not found. Using Default Icon File. Pleace Consider using my icon file ;)")

        root = tk.Tk()

        root.title("Converter")
except:
    tk.messagebox.showerror(title = "Corrupted", message = "Icon file is corrupted, Using Default Icon File")


root.geometry("580x480")

root.resizable(height=False, width=False)


#Ignore!
#Just a value -----------
var = IntVar()
# -----------------------------

# This starts the menu bar with the option menu. 

menubar = Menu(root)

# This is the selection for the File category

filemenu = Menu(menubar, tearoff=0)


# Use imagetest to open and display an image

filemenu.add_command(label="View Conversions", command=Conversions)  # Example placeholder

filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="Files", menu=filemenu)

# Help Option
# About me

About = Menu(menubar, tearoff=0)

# About.add_command(label="About Me", command=(Aboutme))  # Display an image in 'About Me'

About.add_command(label="Source Code", command=link_to_source)

About.add_command(label="More Tools Here!", command=link_to_github)

menubar.add_cascade(label="About", menu=About)


# Label and input stuff and font creation for some reason


font1 = font.Font(family="Arial", size=14, weight="normal")


font1a = font.Font(family="Arial", size=8, weight="normal")

text = tk.Label(text="Picture Conversions", font=font1)

text2 = tk.Label(text="Made by Ricardo", font=font1a)

text3 = tk.Label(text="Select Image!", font=font1)

text4 = tk.Label(text="Select Converstion", font=font1a)

text5 = tk.Label(text="Name Your file!", font=font1a)

# -----------------------------------------------   This Button opens up the file   --------------------------------------------

Button_for_FILE = tk.Button(text="Open FIle", command=imageopener_and_Conversion)

Button_for_FILE.place(x= 12, y = 400)

text3.place(x=12, y=350)

# These last two go last to run the menubar DONT CHANGE IT

root.config(menu=menubar)

# Packing text
text.pack()

text2.pack()

# Run the main loop
root.mainloop()



