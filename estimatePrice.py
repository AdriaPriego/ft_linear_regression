
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

def open_file():
	try:
		with open('predictions.csv', mode='r') as file:
			csv_reader = csv.reader(file)
			theta0, theta1 = next(csv_reader)
	except FileNotFoundError:
		print("File not found.")
		theta0, theta1 = 0.0, 0.0
	except StopIteration:
		print("Empty file.")
		theta0, theta1 = 0.0, 0.0
	except:
		print("Something's wrong...")
		theta0, theta1 = 0.0, 0.0
	return float(theta0), float(theta1)

def estimatePrice(milage, theta0, theta1):
	return theta0 + (theta1 * milage)

def main():
	theta0, theta1 = open_file()
	while True:
		try:
			milage = float(input("Please enter the milage: "))
		except EOFError:
			print("BYE")
			return
		except:
			print("Invalid Milage")
			continue
		break
	print (estimatePrice(milage, theta0, theta1))

if __name__ == "__main__":
	main()