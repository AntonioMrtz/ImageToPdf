import os
import logging
import shutil
import re


numbers = re.compile(r'(\d+)')

def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts



#* You can use RIPSM Chromium to download comics/manga from TMO or other sources
#* Meanwhile ImageToPdf is not available you can just upload the sorted pics in order to generate a pdf https://tools.pdf24.org/es/png-a-pdf

folder=os.fsencode("E:\RIP MSC tmo\Descargas\\")     #* Put here the folder path that contains all the folders with the pictures
foldername=folder.decode()

logging.basicConfig(level=logging.WARNING)



def organizePics():

    # Create output folder

    if not os.path.isdir(foldername+"\\"+"ImageToPdf"):

        os.mkdir(foldername+"\\"+"ImageToPdf")

    else: # delete contents of folder if it exists

        for f in os.listdir(foldername+"\\"+"ImageToPdf"):
            os.remove(os.path.join(foldername+"\\"+"ImageToPdf", f))

    imageToPdf_folder_name=foldername+"\\"+"ImageToPdf"
    
    current_page=0 # stores the number of files for renaming pics in order



    # iterating trough the subfolders

    for filename in sorted(os.listdir(foldername),key=numericalSort):

        
        absolute_path_file=foldername+filename

        if os.path.isdir(absolute_path_file):   # only considering subfolders
            
            folder_nested=os.fsencode(absolute_path_file)

            logging.debug(absolute_path_file)

            for file_nested in os.listdir(folder_nested):

                file_nested_name="\\"+file_nested.decode()
                absolute_path_file_nest=absolute_path_file+file_nested_name

                logging.debug(absolute_path_file_nest)

               
                if ".png" in absolute_path_file_nest:
                    
                    logging.debug(absolute_path_file_nest)

                    shutil.copyfile(absolute_path_file_nest,imageToPdf_folder_name+"\\"+str(current_page)+".png")
                                       
                    current_page+=1

                elif ".jpg" in absolute_path_file_nest:
                    
                    logging.debug(absolute_path_file_nest)

                    shutil.copyfile(absolute_path_file_nest,imageToPdf_folder_name+"\\"+str(current_page)+".jpg")
                   
                    current_page+=1
        




def convertToPdf():

    #TODO after getting folder name , generate pdf 
    #TODO imageToPdf will be needed
    #TODO search module generate pdf python
    pass

params = {

    '0' : organizePics,
    '1' : convertToPdf

}

def main():
    
    print("Welcome to ImageToPdf!\nWhat would you want to do?\n\n0.Organize images of multiple folders in one \n1.Convert pics to pdf")
    entryCode=input()

    
    function=params.get(entryCode,-1)

    if(function==-1):
        print("Número inválido")
        return -1
    else:
        function()


if __name__ == "__main__":

    main()