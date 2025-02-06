
import numpy as np
import csv
import matplotlib.pyplot as plt

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

def predict(km, price, learning_rate=0.01, iterations=1000):
	theta0, theta1 = 0.0, 0.0
	max_km = max(km)
	norm_km = [k / max_km for k in km]
	max_price = max(price)
	norm_price = [p / max_price for p in price]
	m = len(km)
	for _ in range(iterations):
		acum0 = 0
		acum1 = 0
		i = 0
		for i in range(m):
			error = estimatePrice(norm_km[i], theta0, theta1) - norm_price[i]
			acum0 += error
			acum1 += error * norm_km[i]

		theta0 -= (acum0 * learning_rate) / m
		theta1 -= (acum1 * learning_rate) / m
	theta0 = theta0 * max_price
	theta1 = theta1 * (max_price / max_km)
	return theta0, theta1

def plot_model(km, price, regression_line):
	plt.scatter(km, price, color='blue', label='Original Data')

	plt.plot(km, regression_line, color='red', label='Lineal Regresion Model')

	plt.title('Lineal Regresion')
	plt.xlabel('km')
	plt.ylabel('Price')
	plt.legend()
	plt.show()

def calculate_metrics(km, price, theta0, theta1):
	predictions = [estimatePrice(x, theta0, theta1) for x in km]

	errors = [pred - actual for pred, actual in zip(predictions, price)]

	mse = sum([error ** 2 for error in errors]) / len(errors)
	rmse = np.sqrt(mse)
	mae = sum([abs(error) for error in errors]) / len(errors)

	return mse, rmse, mae

def main():
	km, price = open_file()
	theta0, theta1 = predict(km, price, 0.001, 100000)

	try:
		with open("model.csv", "w") as file:
			file.write(f"{theta0},{theta1}")
	except:
		print("Something's wrong saving data in model.csv")
	print(f"Training complete! Model saved with theta0 = {theta0}, theta1 = {theta1}")

	plt.scatter(km, price, color='blue', label='Original Data')

	regression_line = [estimatePrice(x, theta0, theta1) for x in km]
	mse, rmse, mae = calculate_metrics(km, price, theta0, theta1)

	print(f"Model Precision Metrics:")
	print(f"Mean Squared Error (MSE): {mse:.2f}")
	print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
	print(f"Mean Absolute Error (MAE): {mae:.2f}")
	plot_model(km, price, regression_line)

if __name__ == "__main__":
	main()