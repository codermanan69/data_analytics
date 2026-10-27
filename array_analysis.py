import numpy as np

sales = np.array([
    [120, 150, 180],
    [100, 130, 160],
    [200, 190, 220],
    [90, 110, 140]
])

products = ['A', 'B', 'C', 'D']
 

total_sales = np.sum(sales, axis=1)
print("Total sales of each product:")

for i in range(len(products)):
    print("Product", products[i], ":", total_sales[i])


average_sales = np.mean(sales, axis=1)
print("\nAverage sales of each product:")

for i in range(len(products)):
    print("Product", products[i], ":", round(average_sales[i], 2))


index = np.argmax(average_sales)

print("\nProduct with highest average sales:", products[index])
print("Highest average sales:", round(average_sales[index], 2))
