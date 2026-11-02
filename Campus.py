import math

participants = int(input("Number of participants: "))
fee = float(input("Registration fee per participant: "))
sponsorship = float(input("Confirmed sponsorship: "))

venue, equipment, transport = 12000, 5000, 3000
catering_per_person, certificate_per_person = 150, 20

fixed_cost = venue + equipment + transport
variable_per_person = catering_per_person + certificate_per_person

if participants < 0 or fee < 0 or sponsorship < 0:
    print("Inputs cannot be negative")
else:
    total_cost = fixed_cost + (participants * variable_per_person)
    revenue = participants * fee
    funds = revenue + sponsorship
    balance = funds - total_cost
    net_per_person = fee - variable_per_person

    print("\n-- EVENT FINANCIAL SUMMARY --")
    print("Fixed cost: ₹", fixed_cost)
    print("Variable cost: ₹", participants * variable_per_person)
    print("Total expenditure: ₹", total_cost)
    print("Registration revenue: ₹", revenue)
    print("Total funds: ₹", funds)
    print("Final balance: ₹", balance)

    if net_per_person > 0:
        minimum = max(0, math.ceil((fixed_cost - sponsorship) / net_per_person))
        print("Minimum registrations to break even:", minimum)
    else:
        print("Break-even impossible: per-person fee does not cover variable costs")