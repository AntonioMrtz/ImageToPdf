import os
import logging
import shutil
import re
import PySimpleGUI as sg
from PIL import Image


#? You can use RIPSM Chromium to download comics/manga from TMO or other sources


numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


#*-------  INTERFACE INITIALIZATION        -----------------------

sg.theme('DarkAmber')
font = ('Arial', 13)

layout_organizePics = [[sg.Text('Enter the folder that stores the image folders:', key="texto")],
                       [sg.Text('folder', size=(8, 1)),
                        sg.Input(), sg.FolderBrowse('Browse')],
                       [sg.Submit(button_text="Organize", key="seleccionar_ruta"), sg.Cancel(button_text="Back", key="main")]]


layout_convertToPdf = []


layout = [[sg.Button('OrganizePics', key="organize_pics")],
          [sg.Button('ImageToPdf', key="convert_to_pdf")],
          [sg.Button('Exit',key="exit")]]


window = sg.Window('ImageToPdf', layout,
                   icon="media\logoImageToPdf.ico", size=(800, 600), font=font)


#*------------ GLOBAL VARIABLES  -----------

folder = None

foldername = None

folder_convertToPdf = None  # * Put here the folder path converted
foldername_convertToPdf = None

folder_generated=0         #* stores if we have create the ImageToPdf folder before


#*------------ LOGGING  -----------


logging.basicConfig(level=logging.WARNING,
                    format='[%(asctime)s.%(msecs)03d] [%(levelname)-7s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

#*------


def organizePics():

    global folder_generated

    # Create output folder

    if not os.path.isdir(foldername+"/"+"ImageToPdf"):

        os.mkdir(foldername+"/"+"ImageToPdf")

    else:  # delete contents of folder if it exists

        for f in os.listdir(foldername+"/"+"ImageToPdf"):
            os.remove(os.path.join(foldername+"/"+"ImageToPdf", f))

    imageToPdf_folder_name = foldername+"/"+"ImageToPdf"

    current_page = 0  # stores the number of files for renaming pics in order

    # iterating trough the subfolders

    for filename in sorted(os.listdir(foldername), key=numericalSort):

        if filename != "ImageToPdf":

            absolute_path_file = foldername+filename

            if os.path.isdir(absolute_path_file):   # only considering subfolders

                folder_nested = os.fsencode(absolute_path_file)

                logging.debug(absolute_path_file)

                for file_nested in os.listdir(folder_nested):

                    file_nested_name = "\\"+file_nested.decode()
                    absolute_path_file_nest = absolute_path_file+file_nested_name

                    logging.debug(absolute_path_file_nest)

                    if ".png" in absolute_path_file_nest:

                        logging.debug(absolute_path_file_nest)

                        shutil.copyfile(
                            absolute_path_file_nest, imageToPdf_folder_name+"\\"+str(current_page)+".png")

                        current_page += 1

                    elif ".jpg" in absolute_path_file_nest:

                        logging.debug(absolute_path_file_nest)

                        shutil.copyfile(
                            absolute_path_file_nest, imageToPdf_folder_name+"\\"+str(current_page)+".jpg")

                        current_page += 1

    folder_generated=1
    return


def convertToPdf():

    first_flag = 0
    pics = []

    if not os.path.isdir(foldername_convertToPdf):

        logging.warning(
            "ImageToPdf folder not generated")
        return

    for filename in sorted(os.listdir(foldername_convertToPdf), key=numericalSort):

        absolute_path = foldername_convertToPdf+"\\"+filename
        logging.debug(filename)

        if first_flag == 0:

            first_flag += 1

            image_1 = Image.open(absolute_path)
            im_1 = image_1.convert('RGB')

        else:

            image = Image.open(absolute_path)
            im = image.convert('RGB')
            pics.append(im)

    im_1.save(foldername+"ImageToPdf.pdf", save_all=True, append_images=pics)


if __name__ == "__main__":

    while True:

        event, values = window.read()

        #* MENU SCREEN

        if event == "organize_pics":

            window2 = sg.Window('ImageToPdf',  [[sg.Text('Enter the folder that stores the image folders:', key="texto")],
                                                [sg.Text('folder', size=(8, 1)),
                                                 sg.Input(), sg.FolderBrowse('Browse')],
                                                [sg.Submit(button_text="Organize", key="seleccionar_ruta"), sg.Cancel(button_text="Back", key="main")]], icon="media\logoImageToPdf.ico", size=(800, 600), font=font)
            window.Close()
            window = window2

        elif event == "convert_to_pdf" and folder_generated==0:

            sg.Popup('First orgnize the folders with OrganizePics in order to generate the PDF',keep_on_top=True)

        elif event == "convert_to_pdf" and folder_generated==1:

            convertToPdf()
            sg.Popup(f"Pdf generated in folder {foldername_convertToPdf}", keep_on_top=True)
            break
            

        #* ORGANIZE PICS SCREEN

        elif event == "seleccionar_ruta":

            path = values['Browse']+"/"

            # * Put here the folder path that contains all the folders with the pictures
            folder = os.fsencode(path)

            foldername = folder.decode()

            folder_convertToPdf = os.fsencode(foldername+"ImageToPdf/")
            foldername_convertToPdf = folder_convertToPdf.decode()

            organizePics()
            sg.Popup('The files have been organized', keep_on_top=True)

        elif event == "main":

            window2 = sg.Window('ImageToPdf', [[sg.Button('OrganizePics', key="organize_pics")],
                                               [sg.Button(
                                                   'ImageToPdf', key="convert_to_pdf")],
                                               [sg.Button('Exit',key="exit")]], icon="media\logoImageToPdf.ico", size=(800, 600), font=font)
            window.Close()
            window = window2

        elif event == sg.WIN_CLOSED or event == 'exit':
            break

    window.close()
