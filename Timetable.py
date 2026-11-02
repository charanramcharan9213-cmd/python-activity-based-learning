# Course format: (course_name, day, start_minute, end_minute, room)
classes = [
    ("C Programming", "Mon", 540, 600, "R101"),  # 09:00 - 10:00
    ("Mathematics", "Mon", 570, 630, "R102"),    # 09:30 - 10:30 (Overlap!)
    ("Physics Lab", "Mon", 630, 690, "LAB1"),    # 10:30 - 11:30
    ("Web Tech", "Tue", 540, 600, "R101")
]

unavailable = [
    ("Mon", 630, 660, "LAB1")
]

def overlaps(s1, e1, s2, e2):
    return s1 < e2 and s2 < e1

conflicts = 0

for i in range(len(classes)):
    c1, d1, s1, e1, r1 = classes[i]
    for j in range(i + 1, len(classes)):
        c2, d2, s2, e2, r2 = classes[j]
        if d1 == d2 and overlaps(s1, e1, s2, e2):
            print(f"TIMETABLE CLASH: {c1} and {c2} on {d1}")
            conflicts += 1
        if r1 == r2 and d1 == d2 and overlaps(s1, e1, s2, e2):
            print(f"ROOM CLASH: Room {r1} overbooked!")
            conflicts += 1

for course, day, start, end, room in classes:
    for uday, us, ue, uroom in unavailable:
        if day == uday and room == uroom and overlaps(start, end, us, ue):
            print(f"ROOM UNAVAILABLE: {course} in {room}")
            conflicts += 1

if conflicts == 0:
    print("Timetable is perfectly valid.")
else:
    print(f"Total issues found: {conflicts}")