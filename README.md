# leaky-mos
**mos model to find leakage current in digital circuits made on 45nm mgk tech node**
***
Topic: Finding Gate, Drain and Body leakage currents of 45nm_MGK tech node based 2 by 2 multiplier using Modelling and Simulation

Students: Arush Gupta (2019102042) 

Course Instructor: Prof. Zia Abbas

Year: Spring Semester 2022
***
#### How to run
- Pre-requisites:
	- Ng-Spice 
		- for ubuntu: sudo apt install ngspice
	- tree
		- for ubuntu: sudo apt install tree
	- browser (default firefox, edit bash script or install firefox)
	- bash script execution permissions
		- sudo chmod 744 run.sh
		- sudo chmod 744 clear.sh
	- python3
- steps
	- unzip all files in new folder
	- check pre-requisites 
	- run bash script: ./run.sh
	- to remove all temporary files: ./clear.sh
***
#### Approach
- For modelling, we created packages for NMOS, PMOS for both ON/OFF conditions. Then we found intermediate node voltages at different stacks. Using these we find leakage currents for following packages
	- and gate
	- xor gate 
	- final multiplier
- For simulation, we create one ngspice netlist whch contains all the transistors required for multiplier. Each transistor contains 4 voltage source of 0 magnitude for measuring current at each terminal. We measure gate and body leakage using these. 
***
#### Key Features
- everything is automated. Using a single command, we can run complete simulation
- Results are deomonstrated in good, easy to read html page instead of displaying in terminal in between multiple ngspice messages
- Comparision between both simulation and modelling methods
***
#### Future Improvements
- As this simulation method is unable to find drain leakage current as that requires knowledge of current state of transistor. This can be implemented with the help of a boolean flag and some more conditional statements
- This simulation method is not very accurate, example: $I_{bg}$ is contributing to both gate leakage and body leakage but in modelling, $I_{bg}$ is not considered for gate leakage. 
- Difference between both methods is large (3-8%) but this is due to not optimal simulations results. 
***
