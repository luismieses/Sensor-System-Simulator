import json
import time


# Class that handles how the data given by the sensors
class Information:

	# Initializes the data 
	def __init__(self, data):
		self.data = data

	# Outputs the data in the terminal
	def run(self):

		print('Time: ', self.data['Time/Date'])
		print('Sensor number: ', self.data['Sensor number'])
		print('Alarm count: ', self.data['Alarm count'])
		print('Error count: ', self.data['Error count'])

		# Getting the sensor reading of the temperature
		reading = self.data['Temperature reading']

		# Statement that handles if theres not temperature to read
		if reading == "N/A":
			print('Temperature reading: N/A')
			print('-------------------------------------')

		# If the sensor did gave us a reading then print the data in Fahrenheit and Celsius
		else: 
			# Data is given in Fahrenheit
			fah = float(self.data['Temperature reading'])
			# Formula of Celsius
			cel = (fah-32)*(5/9)
			print('Temperature in F: ', fah)
			print('Temperature in C: ', cel)
			print('-------------------------------------')

		# Saves all of the data in a master file
		file = "master.txt"
		with open(file, 'a') as outfile:
		 	json.dump(self.data, outfile)

# Function that handles how the sensor files are opening
# Recieves a number which dictates the sensor file that will be open 	
def openingFiles(files):

	# Statement for Sensor 1
	if files == 1:
		# Handles if the program can't open the file
		try:
			with open('Sensor1.json') as file:
				data = json.loads(file.read())
				file.close()
				return data

		except IOError:
			print('Could not open Sensor 1 data')
			return -1

	# Statement for sensor 2
	elif files == 2:
		# Handles if the progtam can't open the file
		try:
			with open('Sensor2.json') as file:
				data = json.loads(file.read())
				file.close()
				return data

		except IOError:
			print('Could not open Sensor 2 data')
			return -1

	# Statement  for sensor 3
	else:
		# Handles if the program can't open the file
		try:	
			with open('Sensor3.json') as file:
				data = json.loads(file.read())
				file.close()
				return data

		except IOError:
			print('Could not open Sensor 3 data')
			return -1

	

def main():		

	# Master program runs forever
	while True:
		
		# Calling the opening file by giving it 1,2,3 as integers which are the ID's of the sensor
		# Note: The number of the ID's can't be different otherwise the master won't be able to open the 
		# Sensor files
		x = openingFiles(1)
		y = openingFiles(2)
		z = openingFiles(3)

		displayX = Information(x)
		displayY = Information(y)
		displayZ = Information(z)

		displayX.run()
		displayY.run()
		displayZ.run()

		# master programs activates every 30 seconds
		seconds = time.sleep((30))


main()
