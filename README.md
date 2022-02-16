Devasc_Skills
Task1: GitHub
Openen the DEVASC_LABVM, opened terminal 
Opened Github and created new repository
Task implementation:
created a new folde Devasc_Skilss is the ~/labs/devnet-src directort
- git init
- git pull https://github.co/jonhelder/Devasc_Skills.git
- git branch -m master main
Task trouble: suffering with the master/main on gitbub
task verification: see Task1.png

Task2: Ansible
Task Preparation: Had to run both VM's on one PC. Copy the hosts ans ansible config file to the Devasc_Skills directory
Task Implemetation: created the file ios_status.yaml
Task trouble: on both my PC's (Desktop-4GB ans LAPtop-GB) I was not able to run both VM's at the same time. 
Only when I reduce the required RAM of te DEVASC-VM to 2GB and the CRS1000 to 3GB I was able to run both.
I has some troubel in the ansible scrip to react on a response, but was able to fix that
Task verification: see Task2.png

Task3: Docker
Taskpreparation: Run only the DEVASC-LABVM, create the Task3 directory.
Task implemenation: created  Create_Apache_Docker.sh                    
Task trouble: At start I didnt unsderstoot I had the creat the dockerfile instead od creating it on the run . Staring apachr form Docker is not just start
names of docker images cann't be any capital letter.
TaskVerivcation: se Task3/pgn. before the paybook, there is no Sampleimage image and afthe the playbook there is.


Task4: Jenkins
Taskpreparation: 
	Do a final git push
	Start the Jenkings container
	Web brows to localhost:8080 and login to Jenkins
	Create a Job: item name build apache container
        GIt: Rpository URL: https://github.com/jonhelder/Devasc_Skills.git
	Credentials: jonhelder/github-token
	Branch Specifier: */main
	Execure shell command: bash ./Task3/Create-Apache-Container.sh 
Task implementation:
BuildApacheContainer
Before installing the apache container the script first deletes the 
apache-container and the apache-image. It then creates them again.
Second the script creates the Dockerfile which will be used to create 
the apache-images file. then  the contaier will be created.
TestApacheContainer
If the container is working a succesfull HTPP request can be made.
Task trouble shooting: It took a long time it worked. After deleting all the 
files an recreating it worked.

Task5: RestAPI
TaskPreperation: Start  the DEVASC-VM and the CSR1000v-VM
Task implementation:
Opened a terminal and tried the curl examples which worked. (with another 
IP-address). I googled to find some exaples using Python.
I used OPTIONS POST AND get
Task troubleshooting
The  desired response to be found in the header. 
Also the JSON resonse come with a single quote wheras true JSON requires double qoutes!
Task verification: see screenshot in Webex Teams space the netconfPOST.py gives an HTTP reponse of 409. This is because the "severity":"alerts" was already created.

Task6: Webex Teams API
TaskPreperation: For this task only the DEVASC-VM must be started. check Internet connectivity to ping 8.8.8.8
Login in Webex for Developers at https://developer.webex.com to obtain the access token to be used in the script.
Task Implementation: create the scripts using the "Lab - Construct a Python Script to Manage Webex TEams"
- createWebexRoom.py  creates the space in Webex
- addMemberToRoom.py adds Yvan to the Webex-Space
- sendMessageToRoom.py send a message to the WebexSpace
Opened Webex to see if completed 
Task Trouble shooting: The Webex Token is only 12 hours valid, 
Task verification: see schreenshop in Webex TeamsSpace.
