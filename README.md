# Sensor-System-Simulator

This program simulates an IoT system. It consist of a sensor program that calculates the readings of the sensors and sends the data to a master program. The sensor first receives input from the user. It comes in the form of [ID:Reading]. ID means the sensor that its giving the input, the Reading is the target sensor read that the other readings will be based on. Once you give the input the sensor.py starts running. Inside the sensor.py are the following calculations: since there needs to be a simulation for an alarm counter, this was done by getting the absolute difference of the previous reading and the current reading. If that result is larger than 5, the alarm counter increases. For the error counter I decided that if the reading was less than 2 or more than 18, then the error counter increases. After that the data is pass to the Sensor class which in turn display the data to the terminal and send it to the each sensor file in the form of json. The master program activates activates and looks for each sensor file to read the data. #Note: this program can only take the reading of 3 sensors at the same time. Thats why there is a function called "openingFiles". The information class handles the data given by each sensor and displays the output in the terminal. #Note: this program doesn't can't output the last 10 reading by the sensor. Instead what it does is outputs what is currently read in each sensor file. Since each file is being appended every time it reads the information will change. A fallback of this method is that there will be reading that will be miss. After the display of each reading the master program thens saved the acquired record in a master log file. Both program terminate when a keyboard interruption occurs. 

Libraries : 
	
	-json
	- time
	- random
	- sys
	- datetime

Running the program :

	- Running the sensor
		
		- python3 sensor.py "ID - integer" "reading - integer"
	
	- Running the master

		- python3 master.py

Reference : 

	- https://www.w3schools.com/python/default.asp
	- https://linuxconfig.org/how-to-parse-data-from-json-into-python
	- https://www.tutorialspoint.com/python/time_sleep.htm
	- https://www.programiz.com/python-programming/json
	- https://stackoverflow.com/questions/8380006/file-open-function-with-try-except-python-2-7-1

Programming Language : 

	- Python 3

- Contributors : 

	- Luis Mieses

Developer : Luis F Mieses Gómez
