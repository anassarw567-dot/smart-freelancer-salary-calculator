# ==========================================
# SMART FREELANCER SALARY CALCULATOR - PRO
# ==========================================

print("==========================================")
print(" SMART FREELANCER SALARY CALCULATOR - PRO ")
print("==========================================")

while True:

    # -------- Name --------
    name = input("\nEnter your name: ")

    # -------- Projects --------
    while True:
        try:
            projects = int(input("Enter completed projects: "))
            if projects < 0:
                print("Projects cannot be negative.")
                continue
            break
        except:
            print("Invalid input. Enter a whole number.")

    # -------- Price Per Project --------
    while True:
        try:
            price = float(input("Enter price per project: "))
            if price < 0:
                print("Price cannot be negative.")
                continue
            break
        except:
            print("Invalid input. Enter numbers only.")

    # -------- Overtime Hours --------
    while True:
        try:
            overtime_hours = float(input("Enter overtime hours: "))
            if overtime_hours < 0:
                print("Hours cannot be negative.")
                continue
            break
        except:
            print("Invalid input.")

    # -------- Overtime Rate --------
    while True:
        try:
            overtime_rate = float(input("Enter overtime hourly rate: "))
            if overtime_rate < 0:
                print("Rate cannot be negative.")
                continue
            break
        except:
            print("Invalid input.")

    # -------- Tax --------
    while True:
        try:
            tax = float(input("Enter tax percentage: "))
            if tax < 0 or tax > 100:
                print("Tax must be between 0 and 100.")
                continue
            break
        except:
            print("Invalid input.")

    # -------- Expenses --------
    while True:
        try:
            expenses = float(input("Enter monthly expenses: "))
            if expenses < 0:
                print("Expenses cannot be negative.")
                continue
            break
        except:
            print("Invalid input.")

    # =================================
    # Calculations
    # =================================

    project_income = projects * price
    overtime_income = overtime_hours * overtime_rate

    total_income = project_income + overtime_income

    tax_amount = total_income * (tax / 100)

    net_profit = total_income - tax_amount - expenses

    # =================================
    # Performance Level
    # =================================

    if net_profit >= 3000:
        level = "Excellent Month 🔥"
    elif net_profit >= 1500:
        level = "Good Progress 📈"
    elif net_profit >= 500:
        level = "Average Month 👍"
    else:
        level = "Need More Clients 💼"

    # =================================
    # Report
    # =================================

    print("\n==================================")
    print("         MONTHLY REPORT")
    print("==================================")
    print("Freelancer Name :", name)
    print("Projects Income : $", project_income)
    print("Overtime Income : $", overtime_income)
    print("Total Income    : $", total_income)
    print("Tax Amount      : $", round(tax_amount, 2))
    print("Expenses        : $", expenses)
    print("Net Profit      : $", round(net_profit, 2))
    print("Performance     :", level)
    print("==================================")

    # =================================
    # Restart Program
    # =================================

    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the system.")
        break