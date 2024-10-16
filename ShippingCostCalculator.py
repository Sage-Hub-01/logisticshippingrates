# Shipping Cost Calculator

## Input package waight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Caculate shipping cost
shipping_cost = weight * rate

##Display the result
print(f"Shipping Cost: {shiping_cost} USD")
