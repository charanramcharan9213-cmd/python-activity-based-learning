import math

# Format: (route_name, demand, bus_capacity, available_buses)
routes = [
    ("Hostel Route", 135, 50, 3),
    ("City Route", 92, 40, 2),
    ("Railway Station", 48, 30, 2),
    ("Airport Route", 20, 25, 1)
]

total_demand = total_buses = total_unserved = 0

print("\n-- CAMPUS TRANSPORT ALLOCATION --")
for route, demand, capacity, available in routes:
    needed = math.ceil(demand / capacity)
    allocated = min(needed, available)
    unserved = max(0, demand - (allocated * capacity))
    
    total_demand += demand
    total_buses += allocated
    total_unserved += unserved
    
    print(f"{route:15} | Demand: {demand:3} | Needed: {needed} | Allocated: {allocated} | Unserved: {unserved}")

print("-" * 65)
print(f"TOTALS | Demand: {total_demand} | Allocated Buses: {total_buses} | Unserved: {total_unserved}")
