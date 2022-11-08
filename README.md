# COVID19-Triage



## ABOUT
This website attempts to provide a COVID-19 patients management and tracking online application for a hospital, since the number of infections caused by the transmission of the Coronavirus continues to climb worldwide. 
The user/admin will enter the patient's name, address, current COVID-19 symptoms, contact information, health information, and other information, as well as allocate the bed to the appropriate patient.
The patient's data and health status can be inserted and modified by management only. It also includes a dashboard for hospital administrators to view the status of recovered, admitted, and deceased patients, as well as bed availability.

## PRE- REQUISITES:
- Editor Environment: Visual Studio Code
- Frontend
	- HTML5
	- CSS3
	- JQuery
                    - Bootstrap4
- Backend
                    - Django framework
- Database
                    - SQLite


## HOW TO SETUP THIS WEBSITE LOCALLY:

 - Clone repository using  $ git clone  https://github.com/apoorwagupta/COVID19-Triage
 - Setup virtual environment(We used Anaconda)
 - The current working directory should be set in the downloaded folder using 'cd' command.
 - On command line, Exceute `pip install -r requirements.txt`.
 - Run `python manage.py runserver` in the folder where manage.py is located
 - Add your own superuser by 'create superuser' and enter your desired credentials.
 - Go to `127.0.0.1::8000` in your web browser.
                 

## FOR MODIFYING THE WEBSITE:
 -  Change the template folder for adding your own html and css files.
 -  Modify  the static folder if you want to add your own images/txt etc.
 -  Run the  commands ``` python manage.py make migrations ``` and ``` python manage.py migrate ``` after you do any changes in models

 
## FEATURES:
 
The website will contain publishable and documented code right away, as well as all of the following features:

 - Organized folders.
 - Each file is commented line by line for easier understanding of  various functions, keeping in mind the official Django documentation.
 - Interesting graphics with color coordinated bed availability system.
 - A Complete database is provided with the staff,nurse,doctor, bed details.

## SCREENSHOTS:

 - Dashboard: 
![Screenshot]("https://github.com/apoorwagupta/COVID19-Triage/blob/main/Screenshots/DashBoard.png")
 - Main Information Page:
![Screenshot]("https://github.com/apoorwagupta/COVID19-Triage/blob/main/Screenshots/Info.png")
 -Login Page:
![Screenshot]("https://github.com/apoorwagupta/COVID19-Triage/blob/main/Screenshots/Login.png")
 -Patient List:
![Screenshot]("https://github.com/apoorwagupta/COVID19-Triage/blob/main/Screenshots/Patient-List.png")
 -Patient form:
 ![Screenshot]("https://github.com/apoorwagupta/COVID19-Triage/blob/main/Screenshots/Patient_Form.png")
 -Patient Overview:
 ![Screenshot]("https://github.com/apoorwagupta/COVID19-Triage/blob/main/Screenshots/Patient_Overview.png")

## Acknowledgements

* [Code With Harry](https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg)
* [FreeCodeCamp] (https://www.youtube.com/watch?v=F5mRW0jo-U4)
