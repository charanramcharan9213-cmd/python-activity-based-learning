participants = [
    ("REG101", "Asha"),
    ("REG102", "Bharat"),
    ("REG103", "Charan"),
    ("REG102", "Bharat Duplicate"),
    ("REG104", "Divya")
]

fee = 250
sponsorships = [10000, 7500, 5000]
expenses = [12000, 8000, 4500, 3000]

seen_ids = []
valid_count = 0

for reg_id, name in participants:
    if reg_id in seen_ids:
        print(f"DUPLICATE REGISTRATION REJECTED: {reg_id} ({name})")
    else:
        seen_ids.append(reg_id)
        valid_count += 1

revenue = valid_count * fee
sponsorship_total = sum(sponsorships)
expense_total = sum(expenses)
total_funds = revenue + sponsorship_total
balance = total_funds - expense_total

print("\n-- FESTIVAL FINANCIAL AUDIT --")
print(f"Valid Participants: {valid_count} | Revenue: ₹{revenue}")
print(f"Sponsorships: ₹{sponsorship_total} | Total Funds: ₹{total_funds}")
print(f"Total Expenses: ₹{expense_total} | Final Balance: ₹{balance}")
print("Result Status:", "SURPLUS" if balance >= 0 else "DEFICIT")
