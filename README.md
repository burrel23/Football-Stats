# CI/CD Project Burrel PUEGUO - Youssef HASSANI

This is a little Website on Football , which give you :
-  Informations and Stats about any Football team 
- Informations and Stats about football players playing in the top 5 Leagues (England, France, Spain, Italy and Portugal) per season. 
All these informations
are being taken from a Football API : v3.football.api-sports.io.


# Requirements
To execute this project, you will need: 

- A computer running a Linux distribution
- Install Python3 : sudo apt install Python3
- Install the Python package manager pip : sudo apt install pip

# Installation

- Clone de git project : git clone https://github.com/burrel23/Football-Stats.git
- Change working directory : cd Football-Stats
- install dependancies : pip install -r requirements.txt

# Run the app

To launch the application, use the following command from the project directory: python3 app.py

Website Access : http://localhost:3000

# How to run the app with Docker

- Install Docker dependancies
- Build the Image in the app directory : docker build -t <image name> .
- Launch the Docker : docker run -d -p 5000:3000 <image name>
- Website access : http://localhost:5000

# How to test the app 

Type this command to test app : pytest test_app.py
3 tests are being define for this app : 
  - Welcome Page's return is 200 OK
  - Player Page's return is 200 OK
  - Team Page's return is 200 OK
