
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import statistics

def open_file():
	try:
		with open('data.csv', mode='r') as file:
			km = np.array([])
			price = np.array([])
			csv_reader = csv.reader(file)
			csv_reader = csv.reader(file)
			header = next(csv_reader)
			for row in csv_reader:
				km = np.append(km, float(row[0]))
				price = np.append(price, float(row[1]))
	except FileNotFoundError:
		print("File not found.")
		exit(1)
	except StopIteration:
		print("Empty file.")
		exit(1)
	except:
		print("Something's wrong...")
		exit(1)
	return km, price

def estimatePrice(milage, theta0, theta1):
	return theta0 + (theta1 * milage)

def main():
	km, price = open_file()
	theta0, theta1 = 0.0, 0.0
	learningRate = 0.01
	m = km.size
	iterations = 0
	max_iterations = 10000
	km = (km - km.mean()) / km.std()
	price = (price - price.mean()) / price.std()
	while iterations < max_iterations:
		acum0 = 0
		acum1 = 0
		i = 0
		for i in range(m):
			acum0 += estimatePrice(km[i], theta0, theta1) - price[i]
			acum1 += (estimatePrice(km[i], theta0, theta1) - price[i]) * km[i]
		tmp0 = (acum0 / m) * learningRate
		tmp1 = (acum1 / m) * learningRate
		anttheta0 = theta0
		anttheta1 = theta1
		theta0 = theta0 - tmp0
		theta1 = theta1 - tmp1
		if abs(theta0 - anttheta0) < 0.001 and abs(theta1 - anttheta1) < 0.001:
			print(theta0, theta1)
			break
		iterations += 1
	print(theta0, theta1)
if __name__ == "__main__":
	main()