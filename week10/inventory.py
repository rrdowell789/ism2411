# Reflection Questions
# 1.) Going in, I didn't expect it to be possible to use indexes to retrieve things from your list order. It surprised me was that Python lets you use negative indexes like inventory[-1] to count from the end of a list. This is useful because you don't know how many items are in a list.
# 2.) In one of my classes, I had to track inventory for an assignment. Doing it in Excel meant manually updating rows, re-sorting, and rechecking totals every time an item was added or removed. With a Python list, I could store the items once, use .append() and .remove() to update them, and get counts and totals instantly with len() and sum(), as in my inventory exercises.


print("--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2
print(inventory[middle]) # middle item

print("--- Exercise 3: Slicing practice ---")
print(inventory[:3]) # first 3 items
print(inventory[-2:]) # last 2 items
print(inventory[::2]) # every 2nd item

print("--- Exercise 4: Modifying lists ---")
inventory.append("envelope")
print(inventory) 
inventory.remove("tape")
print(inventory)

print("--- Exercise 5: Tuple comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count= len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discount)


print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")