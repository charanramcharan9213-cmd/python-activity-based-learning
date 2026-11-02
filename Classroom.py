classrooms = [
    ["RESERVED", None, None, "S101"],
    [None, "RESERVED", None, None],
    ["S105", None, None, None]
]

waiting_list = ["S102", "S103", "S101", "S104", "S106"]

def existing_students(grid):
    return [seat for room in grid for seat in room if seat and seat != "RESERVED"]

for student in waiting_list:
    if student in existing_students(classrooms):
        print(f"{student}: Duplicate assignment rejected")
        continue
    
    placed = False
    for r_idx, room in enumerate(classrooms):
        for s_idx in range(len(room)):
            if room[s_idx] is None:
                room[s_idx] = student
                print(f"{student} assigned to Room {r_idx + 1}, Seat {s_idx + 1}")
                placed = True
                break
        if placed:
            break

print("\n-- CLASSROOM SUMMARY --")
for i, room in enumerate(classrooms, 1):
    vacant = room.count(None)
    reserved = room.count("RESERVED")
    occupied = len(room) - vacant - reserved
    print(f"Classroom {i} | Occupied: {occupied} | Reserved: {reserved} | Vacant: {vacant}")