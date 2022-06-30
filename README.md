# ImageToPdf


<img src="media/logoImageToPdf.png" width="100" style="padding-left:0px"/>

## Features
<br>

### ▶ Organize pics
<br>
<p>By setting up a folder like it will be shown later in this document the script sort all photos following alphanumerical order and putting
all the files in the same folder( ImageToPdf ).</p>
<p>This is helpful when you want to put together large amounts of pictures stored in different folders and you want to preserv the order between all the items like a comic downloaded in separate chapters and images.</p>
<p><a href="#convert-to-pdf">Convert to pdf</a> uses this schema for generating the pdf.</p>

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
    * For converting to Pdf you must have a folder named ImageToPdf in your path folder or you should have executed <a href="#organize-pics">Organize pics</a> before.  

<br>

1. Donwload <a href="https://github.com/AntonioMrtz/ImageToPdf">the project </a>and unzip it.
<br>

2. Open the executable ImageToPdf.exe
<br>

3. Click on OrganizePics. <br><br>
![](/media/main_menu.png)

4. Now select the folder where the folders of imnages are stored
by clicking on "Browse" (1) and when you´re done just click on "Organize". (2)<br><br>
![](/media/organize_pics_menu.png)

5. Now you can generate the Pdf by going to the main menu pressing "Back" and then ImageToPdf.

![](/media/main_menu.png)

6. Its Done ! The Pdf will be stored in the folder you selected before.

<br>
<hr>

## Tech usage
<br>

- In this proyect i have made an extensive use of the OS library of python to iterate through the files and directories and creating/deleting files.


- With the use of regex i could solved one big issue like it is the order in which the files are stored and iterated. The script make use
of preordered folders and files but this doesn`t match the order that the OS has internally. By creating a modified sort method this problem was solved.

- The shutil library allow me to copy files from source to destination. I did not rename files from the source folders because it implies modifying user files and when using a file it gives you errors because is being used.

- I have set the logging level to Warning but if you want to see in which order the files and folders are being accesed you can set it up to DEBUG at the beginning of the script.

- To generate the Pdf i worked with the PIL library for python.

- The GUI was made using SimpleGUI Python and exents the user to modify code manually and opened the chance to just need the executable and don´t worry about dependencies.

<br>

## Upcoming features

1. Local compression of pdfs
<br><br>
<hr><br>

*If you have any sugestions or you find error or bugs contact with me trough my social medias or mail. You can find those in my github profile or [webpage](https://antoniomrtz.github.io/Antonio-Martinez-Portafolio/)*
