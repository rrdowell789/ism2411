#Self Assessment Questions
#1.) The first bug I noticed was the missing colon on the second for loop. I found it from the error message Python gave me. This tells me I'm okay at reading error messages, but I'd have a harder time finding bugs that don't crash the program.
#2.) Apply_discount takes a price and a tier (gold, silver, or bronze). And gives back the price after the discount. Gold takes off 15%, silver 10%, and bronze 5%, and no tier is none. Yes, a colleague could use it without reading the code.
#3.) I used AI on exercise 5 to explain the what error messages meant/ what they were talking about speicifally. I think AI helped because it was able to easily breakdown concepts that im still leanring to understand, and i ws abel to ask it unlimited questions.


# Exercise 1:
#Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# Exercsie 2:

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

    #Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3:

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final Price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4:

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 6:

x = 100 #apple

def double_it():
    x = 999 #another apple
    return x * 2
print(x)
print(double_it())
print(x)

# Exercise 5

# 1: the second loop header was missing a colon, which caused a SyntaxError.To fix, add ":" at the end of the "for sale in sales" line.
# 2: the first loop used "total = sale", so total was overwritten on every pass and only kept the last sale (90). To fix, use "total += sale" so each sale is added to the running total.
# 3: the while loop used "i <= len(sales)". The list has 5 items (indexes 0-4), so when i hit 5 it caused an IndexError. To fix, use "i < len(sales)" so the loop stops at the last valid part.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
