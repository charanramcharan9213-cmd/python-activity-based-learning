registered_tickets = ["T101", "T102", "T103", "T104", "T105"]
entry_attempts = ["T101", "T102", "T102", "T999", "T103", "T104"]

seats = [
    [None, None, None],
    [None, None, None]
]

used_tickets = []
accepted = rejected = 0

for ticket in entry_attempts:
    if ticket not in registered_tickets:
        print(f"{ticket} REJECTED: Not registered")
        rejected += 1
        continue
    if ticket in used_tickets:
        print(f"{ticket} REJECTED: Duplicate entry attempt")
        rejected += 1
        continue
    
    assigned = False
    for row in seats:
        for i in range(len(row)):
            if row[i] is None:
                row[i] = ticket
                used_tickets.append(ticket)
                accepted += 1
                print(f"{ticket} ACCEPTED: Assigned seat")
                assigned = True
                break
        if assigned:
            break

print("\n-- EVENT ENTRY SUMMARY --")
available_seats = sum(row.count(None) for row in seats)
print(f"Accepted: {accepted} | Rejected: {rejected} | Available Seats: {available_seats}")
