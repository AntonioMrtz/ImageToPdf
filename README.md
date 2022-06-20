# ImageToPdf


<img src="media/logoImageToPdf.png" width="100" style="padding-left:0px"/>

## Features
<br>

### ▶ Organize pics
<br>
<p>By setting up a folder like it will be shown later in this document the script sort all photos following alphanumerical order and putting
all the files in the same folder( ImageToPdf ).</p>
<p>This is helpful when you want to put together large amounts of pictures stored in different folders and you want to preserv the order between all the items like a comic downloaded in separate chapters and images.</p>
<p><a href="#convert-to-pdf">Convert to pdf</a> uses this schema for generating the pdf. Meanwhile its not active you can just upload the sorted photos to
<a href="https://tools.pdf24.org/es/png-a-pdf">an unlimited length online pdf converter</a>.</p>

<br>

### ▶ Convert to Pdf
<br>
<p>Gets all the pictures from the created folder in <a href="#organize-pics">Organize pics</a> and put it together on a PDF keeping the order of those.</p>
</br>
</br>


<hr>

## Intructions of use
<br>

* PRECONDITIONS
    * The main folder you will put in the path should have at least one folder with the images. ( The hierarchy must be : folder->folder/s->images)
    * For converting to Pdf you must have a folder named ImageToPdf in your path folder.   

<br>
1. Place the full path of the folder that stores all the photos:
<br><br>

![folder](/media/folder_change.png)

<br>
2. Save the changes in the file.

<br>
3. Run the script by typing python main.py in the command prompt (only one of those):

>python main.py

>python3 main.py

<br>
4. Enter the number of the option you want to execute in the command prompt :
<br><br>

![functions](/media/current_functions.png)
<hr>

## Tech usage
<br>

- In this proyect i have made an extensive use of the OS library of python to iterate through the files and directories and creating/deleting files.


- With the use of regex i could solved one big issue like it is the order in which the files are stored and iterated. The script make use
of preordered folders and files but this doesn`t match the order that the OS has internally. By creating a modified sort method this problem was solved.

- The shutil library allow me to copy files from source to destination. I did not rename files from the source folders because it implies modifying user files and when using a file it gives you errors because is being used.

- I have set the logging level to Warning but if you want to see in which order the files and folders are being accesed you can set it up to DEBUG at the beginning of the script.

- To generate the Pdf i worked with the PIL library for python.

<br>

## Upcoming features

1. Graphic interface for selecting folder and options with SIMPLEGUI
2. Local compression of pdfs
<br><br>
<hr><br>

*If you have any sugestions or you find error or bugs contact with me trough my social medias or mail. You can find those in my github profile or [webpage](https://antoniomrtz.github.io/Antonio-Martinez-Portafolio/)*
