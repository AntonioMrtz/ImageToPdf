import os
import logging
import shutil

# You can use RIPSMC hromium to download 

folder=os.fsencode("E:\RIP MSC tmo\Descargas\\")     #* Put here the folder path that contains all the folders with the pictures
foldername=folder.decode()

logging.basicConfig(level=logging.WARNING)

#? MEJORA poner interfaz grafica
#? MEJORA seleccion de carpeta graficamentw

#! The intermediate chapters like 7.5 are stored after the previous one 7 ( if this dont work in your OS , intermediate chapter would be stored
#! before the previuos)



def organizePics():

    # Create output folder

    if not os.path.isdir(foldername+"\\"+"ImageToPdf"):

        os.mkdir(foldername+"\\"+"ImageToPdf")

    else: # delete contents of folder if it exists

        for f in os.listdir(foldername+"\\"+"ImageToPdf"):
            os.remove(os.path.join(foldername+"\\"+"ImageToPdf", f))

    imageToPdf_folder_name=foldername+"\\"+"ImageToPdf"
    
    current_page=0 # stores the number of files for renaming

    # iterating trough the subfolders

    for file in os.listdir(folder):

        filename=file.decode()
        absolute_path_file=foldername+filename

        if os.path.isdir(absolute_path_file):   # only considering subfolders
            
            folder_nested=os.fsencode(absolute_path_file)

            logging.warning(absolute_path_file)

            for file_nested in os.listdir(folder_nested):

                file_nested_name="\\"+file_nested.decode()
                absolute_path_file_nest=absolute_path_file+file_nested_name

                '''
                if ".png" in absolute_path_file_nest:
                    
                    logging.debug(absolute_path_file_nest)

                    # for avoid permission errors files are copied then renamed

                    shutil.copyfile(absolute_path_file_nest,imageToPdf_folder_name+"\\"+str(current_page)+".png")
                    
                    
                    current_page+=1

                elif ".jpg" in absolute_path_file_nest:
                    
                    logging.debug(absolute_path_file_nest)

                    # for avoid permission errors files are copied then renamed

                    shutil.copyfile(absolute_path_file_nest,imageToPdf_folder_name+"\\"+str(current_page)+".jpg")
                   
                    current_page+=1
                '''




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
    
    print("Welcome to ImageToPdf!\nWhat would you want to do?\n\n0.Organize images of multiple folders\n1.Convert pics to pdf")
    entryCode=input()

    
    function=params.get(entryCode,-1)

    if(function==-1):
        print("mal numero pa")
        return -1
    else:
        function()


if __name__ == "__main__":

    main()