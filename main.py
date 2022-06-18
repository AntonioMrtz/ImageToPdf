import os

# You can use RIPSMC hromium to download 

folder=os.fsencode("E:\RIP MSC tmo\Descargas\\")
foldername=folder.decode()


#? MEJORA poner interfaz grafica
#? MEJORA seleccion de carpeta graficamentw

#! PROBLEMON , QUE PASA CON CAPITULOS 7.5 , SE METEN DELANTE? parece que no -> testear

def main():

    #TODO PONER VERSION FINAL
    '''
    print("Welcome to ImageToPdf!\nWhat would you want to do?\n\n1.Organize images of multiple folders\n2.Convert pics to pdf")
    entryCode=input()

    if entryCode==0:
        organizePics()
    elif entryCode==1:
        convertToPdf()
    '''
    organizePics()


def organizePics():

    #! crear carpeta final

    for file in os.listdir(folder):

        filename=file.decode()
        absolute_path_file=foldername+filename

        if os.path.isdir(absolute_path_file):
            
            #* entrar carpeta
            #* recorrer y tratar , no tratar subcarpetas

            folder_nested=os.fsencode(absolute_path_file)

            for file_nested in os.listdir(folder_nested):

                file_nested_name="\\"+file_nested.decode()
                absolute_path_file_nest=absolute_path_file+file_nested_name

                #if absolute_path_file_nest in [".png" or ".jpg"]:
                #! FALTA comprobar si png y añadir a la carpeta grande

                print(absolute_path_file_nest)

        else:
            os.remove(absolute_path_file)     

def convertToPdf():

    #TODO pedir carpetas , importar libreria to PDF
    pass



if __name__ == "__main__":

    main()