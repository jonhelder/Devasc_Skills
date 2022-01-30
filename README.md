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



