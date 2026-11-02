applicants = [
    ("Asha", 88, [82, 91, 86, 92], 92, 180000),
    ("Bharat", 88, [79, 85, 90, 95], 95, 160000),
    ("Charan", 72, [65, 70, 68, 78], 78, 240000),
    ("Divya", 91, [92, 88, 94, 90], 70, 150000),
    ("Esha", 84, [80, 48, 90, 85], 90, 120000)
]

eligible = []

for name, aggregate, subjects, attendance, income in applicants:
    valid = (
        0 <= aggregate <= 100 
        and all(0 <= mark <= 100 for mark in subjects) 
        and 0 <= attendance <= 100 
        and income >= 0
    )
    if not valid:
        print(f"{name} - Invalid Record")
    elif aggregate >= 60 and min(subjects) >= 50 and attendance >= 75 and income <= 250000:
        eligible.append((name, aggregate, attendance, income))
    else:
        print(f"{name} not eligible")

# Deterministic tie-breaking sort key: (-aggregate, -attendance, income)
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\nSCHOLARSHIP MERIT LIST")
for rank, (name, marks, attendance, income) in enumerate(eligible, 1):
    print(f"{rank}. {name} | Aggregate: {marks} | Attendance: {attendance}% | Income: {income}")