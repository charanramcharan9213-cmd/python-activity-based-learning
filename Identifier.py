def validate_email(email):
    errors = []
    if " " in email:
        errors.append("Email must not contain spaces")
    if email.count("@") != 1:
        errors.append("Email must contain exactly one '@'")
    else:
        username, domain = email.split("@")
        if not username:
            errors.append("Username is missing")
        if not domain or "." not in domain or domain.startswith(".") or domain.endswith("."):
            errors.append("Domain must contain a valid inner dot")
    return errors

def validate_id(reg_id):
    if len(reg_id) != 13:
        return False
    return (
        reg_id[:3] == "SRM" 
        and reg_id[3:5].isdigit() 
        and reg_id[5] == "-" 
        and reg_id[6:8].isalpha() 
        and reg_id[6:8].isupper() 
        and reg_id[8] == "-" 
        and reg_id[9:13].isdigit()
    )

email = input("Student Email: ").strip()
reg_id = input("Registration ID: ").strip()

email_errs = validate_email(email)
print("\n-- VALIDATION RESULTS --")
print("Email:", "VALID" if not email_errs else f"INVALID ({', '.join(email_errs)})")
print("Reg ID:", "VALID" if validate_id(reg_id) else "INVALID (Expected format: SRM26-CS-1042)")