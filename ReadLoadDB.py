import os

def ReadWordList():
	file_name = os.path.join("lib","WordList.txt")
	WordList = []
	with open(file_name, "r") as f:
		for line in f:
			WordList.append(line.split()[0])
	return WordList
	
def ReadCharacteristic():
	file_name = os.path.join("lib","Characteristic.csv")
	Data = []
	with open(file_name, "r") as f:
		for line in f:
			Data.append(line.split())
	return Data
	
	
def WriteWordList():
	file_name = os.path.join("lib","WordList.txt")
	WordList = []
	with open(file_name, "r") as f:
		for line in f:
			WordList.append(line.split()[0])
	return WordList
	
def WriteCharacteristic():
	file_name = os.path.join("lib","Characteristic.csv")
	Data = []
	with open(file_name, "r") as f:
		for line in f:
			Data.append(line.split())
	return Data