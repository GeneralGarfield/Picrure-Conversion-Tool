# Program Converter GUI
# Description: 
#   Converts images to pdf or pdf to images
#
# Author: GeneralGarfield
# Date: 4/1/2025
# Revised: 
#   4/15/2025




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

import sys





# Functions for the Menu



# ----------------- FiX THIS IN A LATER UPDATE
#def Tutorial():
    #directory_path = os.path.dirname(__file__)

    # subprocess.run(["notepad", file_path2])
# --------------------------------------

def file_opener():
    # Open the file dialog and return the selected file path

    file = filedialog.askopenfile(mode="r", filetypes=[("All Files", "*.jpg *.png *.ico")])
    
    if file:

        return file.name
    
    return None


def link():
    
    webbrowser.open_new_tab("https://github.com/GeneralGarfield")




def radiobuttons():
   selection = int(var.get())

   return selection





def imageopener_and_Conversion():

    def Conversion1():
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

        

        

        

        user_input = str(entry1.get())

        if not user_input.strip():
            tk.messagebox.showerror(title="No name", message="Please name your file")

        
        
        value = radiobuttons()

        output1 = "Conversions/PDF"
        output2 = "Conversions/JPEG"
        output3 = "Conversions/ICO"
        output4 = "Conversions/PNG"

        
        if value == 1:
            
            image.save(f"{output1}/{user_input}.pdf")
            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
        elif value == 2:
            
            im = image.convert("RGB")
            im.save(f"{output2}/{user_input}.jpeg")
            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
        elif value == 3:
            
            image.save(f"{output3}/{user_input}.ico")
            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")
        elif value == 4:
            
            image.save(f"{output4}/{user_input}.png")
            tk.messagebox.showinfo(title= "Sucsess", message= "File Converted successfully!")

            Exception
            
   
    file_path = file_opener()  # Get the file path from file_opener
    
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




        PDF_for_conversion.place(x= 200, y=130)

        JPEG_for_conversion.place(x= 200, y=150)

        ICO_for_conversion.place(x= 200, y=170)

        PNG_for_conversion.place(x= 200, y=190)

        Conversion_button = tk.Button(text="Convert!", command=Conversion1)

        Conversion_button.place(x=400, y=200)

        entry1 = tk.Entry(root, width=30)
        

        

         

        entry1.place(x=350, y =140)


        text4.place(x=200, y=100)

        text5.place(x=400, y=100)


        
    

# -------------------------------- FIX THIS IN A LATER UPPDATE ----------
#def Aboutme():
    
  #  directory_path = os.path.dirname(__file__)
    
   # file_path3 = os.path.join(directory_path, 'about.txt')
    
   # subprocess.run(["notepad", file_path3])
# -------------------------------

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

directory_path = os.path.dirname(__file__)

file_path = os.path.join(directory_path, 'test.ico')

# Creates the main Window and Icon

root = tk.Tk()

root.title("Converter")

root.iconbitmap(file_path)

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

Help = Menu(menubar, tearoff=0)

# Help.add_command(label="Tutorial", command=Tutorial)  # Example placeholder

menubar.add_cascade(label="Help", menu=Help)

# About me

About = Menu(menubar, tearoff=0)

# About.add_command(label="About Me", command=(Aboutme))  # Display an image in 'About Me'

About.add_command(label="Github", command=link)

menubar.add_cascade(label="About", menu=About)\


# Label and input stuff and font creation for some reason


font1 = font.Font(family="Arial", size=14, weight="normal")


font1a = font.Font(family="Arial", size=8, weight="normal")




text = tk.Label(text="Welcome to the PDF convertion tool!", font=font1)

text2 = tk.Label(text="Made by Ricardo", font=font1a)

text3 = tk.Label(text="Select Image To start Conversion!", font=font1)

text4 = tk.Label(text="Select Converstion", font=font1a)

text5 = tk.Label(text="Name Your file!", font=font1a)



# -----------------------------------------------   This Button opens up the file   --------------------------------------------


Button_for_FILE = tk.Button(text="Click Here!", command=imageopener_and_Conversion)



Button_for_FILE.place(x= 12, y = 400)

text3.place(x=12, y=350)





# These last two go last to run the menubar DONT CHANGE IT

root.config(menu=menubar)






# Packing text
text.pack()

text2.pack()



# Run the main loop
root.mainloop()
