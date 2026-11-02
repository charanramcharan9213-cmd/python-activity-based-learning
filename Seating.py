seating = [
    ["S101", "S102", None, "RESERVED"],
    ["S103", "S102", "S105", None],
    ["S106", "BAD7", "RESERVED", "S108"]
]

seen = []
issues = empty_seats = reserved_seats = valid_students = 0

for r_idx, row in enumerate(seating, 1):
    for s_idx, val in enumerate(row, 1):
        loc = f"Row {r_idx}, Seat {s_idx}"
        if val is None:
            empty_seats += 1
        elif val == "RESERVED":
            reserved_seats += 1
        else:
            valid_id = (len(val) >= 2 and val[0] == 'S' and val[1:].isdigit())
            if not valid_id:
                print(f"INVALID ROLL ID: '{val}' at {loc}")
                issues += 1
            elif val in seen:
                print(f"DUPLICATE ROLL ID: '{val}' at {loc}")
                issues += 1
            else:
                seen.append(val)
                valid_students += 1

print("\n-- SEATING AUDIT SUMMARY --")
print(f"Valid Students: {valid_students} | Empty: {empty_seats} | Reserved: {reserved_seats} | Issues: {issues}")
