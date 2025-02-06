
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

def open_file():
	try:
		with open('model.csv', mode='r') as file:
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

def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def main():
	theta0, theta1 = open_file()
	while True:
		try:
			mileage = float(input("Please enter the mileage: "))
		except EOFError:
			print("BYE")
			return
		except:
			print("Invalid mileage")
			continue
		if mileage < 0:
			print("The mileage must be a positive number.")
			continue
		break
	price = estimatePrice(mileage, theta0, theta1)
	if price < 0:
		price = 0
		print("The line is in the negative side")
	print (price)

if __name__ == "__main__":
	main()