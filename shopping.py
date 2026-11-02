budget = 2000
discount_rate = 0.10  # Corrected from OCR error to 10%
discount_threshold = 1500

products = ["Notebook", "Headphones", "Bottle", "Backpack"]
prices = [80, 650, 250, 900]
quantities = [4, 1, 2, 1]
original_quantities = quantities.copy()

def bill(qty):
    subtotal = sum(prices[i] * qty[i] for i in range(len(prices)))
    discount = subtotal * discount_rate if subtotal >= discount_threshold else 0
    return subtotal, discount, subtotal - discount

subtotal, discount, payable = bill(quantities)
print("Original Payable Amount: ₹", round(payable, 2))

idx = len(quantities) - 1
while payable > budget and idx >= 0:
    if quantities[idx] > 0:
        quantities[idx] -= 1
        subtotal, discount, payable = bill(quantities)
    else:
        idx -= 1

print("\n-- PURCHASE ADJUSTMENT SUMMARY --")
for i in range(len(products)):
    reduced = original_quantities[i] - quantities[i]
    if reduced > 0:
        print(f"{products[i]}: Reduced by {reduced} unit(s)")

print("Final Subtotal: ₹", round(subtotal, 2))
print("Discount Applied: ₹", round(discount, 2))
print("Final Payable Amount: ₹", round(payable, 2))
print("Remaining Budget: ₹", round(budget - payable, 2))
