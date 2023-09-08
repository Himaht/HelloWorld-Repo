import math

TAX_RATE = 0.1  # 10% tax rate 
TAX_RATE1 = 0.12 # 12% tax rate 
TAX_RATE2 = 0.22  # 22% tax rate 
# get the user input
marital_status = input("Are you married? (yes/no): ").lower().strip(" ")
income = float(input("Enter your annual income: $"))

single_income_limit = 95376
married_income_limit = 190751


if marital_status == "no":
    if income <= 11000:
        tax_amount = income * TAX_RATE
        print(f"Your tax amount is: ${tax_amount:.2f}")
    elif 11001 <= income <= 44725:
        tax_amount = income * TAX_RATE1
        print(f"Your tax amount is: ${tax_amount:.2f}")
    elif 44726 <= income <= 95375:
        tax_amount = income * TAX_RATE2
        print(f"Your tax amount is: ${tax_amount:.2f}")
    else:
        print("Income is too big for this calculator")

elif marital_status == "yes":
    if income <= 22000:
        tax_amount = income * TAX_RATE
        print(f"Your tax amount is: ${tax_amount:.2f}")
    elif 22001 <= income <= 89450:
        tax_amount = income * TAX_RATE1
        print(f"Your tax amount is: ${tax_amount:.2f}")
    elif 89451 <= income <= 190750:
        tax_amount = income * TAX_RATE2
        print(f"Your tax amount is: ${tax_amount:.2f}")
    else:
        print("Income is too big for this calculator")
else:
    print("Please enter either yes or no for marital status")
