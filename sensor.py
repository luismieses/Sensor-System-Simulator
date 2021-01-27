import json
import time
import random
import sys 		
import datetime

# Class that handles the Sensor data
class Sensors:

	def __init__(self, targetTmp, senNumber, senReading, alarm_count, error_count):
		self.targetTmp = targetTmp
		self.senNumber = senNumber
		self.senReading = senReading
		self.alarm_count = alarm_count
		self.error_count = error_count


	def run(self):

		# Variable that gives the current time
		date_time = datetime.datetime.now()

		# Organizing the sensor data in JSON format
		
		data = {
			'Target temperature' : str(self.targetTmp),
			'Sensor number' : str(self.senNumber),
			'Time/Date' : str(date_time),
			'Temperature reading' : str(self.senReading),
			'Alarm count' : str(self.alarm_count),
			'Error count' : str(self.error_count)

			}

		# Sending the data to the corresponding sensor file
		file = "Sensor" + str(self.senNumber) + ".json"
		with open(file, 'w') as outfile:
		 		json.dump(data, outfile)
		 		print(data)
		



def main():

	# Alarm counter
	alarm_count = 0

	# Error counter
	error_count = 0

	# Argument of the sensor ID 
	senNumber = (sys.argv[1])

	# Argument of the first reading by the sensor ("Target reading")
	targetReading = int((sys.argv[2]))


	while True:

		# random sensor reading 
		senReading = round(random.uniform(2.00,20.00),2)

		# Getting the previous reading for comparison
		previous_reading = abs(targetReading - senReading)

		# Statement that determines if theres a low or high change
		if previous_reading > 5:

			# Increasing the counter
			alarm_count = alarm_count + 1

		# Statement that decides if there will be no data to read
		if senReading <= 2 or senReading >= 18:

			# Substitutes the current reading with N/A
			senReading = str('N/A')
			# increasing the counter
			error_count = error_count + 1


		sensors = Sensors(targetReading, senNumber, senReading, alarm_count, error_count)

		sensors.run()

		# Program runs every 10 seconds 
		seconds = time.sleep((10))



main()