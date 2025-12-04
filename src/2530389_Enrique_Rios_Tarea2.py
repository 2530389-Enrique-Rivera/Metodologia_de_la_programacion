#Name: Enrique De Jesus Rios Rivera
#Matriculation: 2530389
#Group: IM 1-3

# ==================================================
# 7.2 Problem 2: Work hours and overtime payment
# ==================================================
# Description:
# Calculates weekly payment including overtime.
# Inputs: hours_worked (float), hourly_rate (float)
# Outputs: Regular pay, Overtime pay, Total pay, Overtime flag
# Validations: hours_worked >= 0, hourly_rate > 0
# Test cases:
#  Normal: hours_worked=38, rate=100 -> no overtime
#  Border: hours_worked=40 -> exact limit
#  Error: hours_worked=-5 -> Error

try:
    hours_worked = float(input("Hours worked: "))
    hourly_rate = float(input("Hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        overtime_hours = max(0.0, hours_worked - 40.0)
        regular_hours = min(hours_worked, 40.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40.0)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)
except:
    print("Error: invalid input")

# ==================================================
# 7.3 Problem 3: Discount eligibility
# ==================================================
# Description:
# Determines if the customer gets discount based on student/senior flag
# or purchase total.
# Inputs: purchase_total (float), texts YES/NO
# Outputs: Discount flag, final total
# Test cases:
#  Normal: total=1200, NO, NO -> discount
#  Border: total=1000, NO, NO -> discount
#  Error: text="MAYBE" -> Error

try:
    purchase_total = float(input("Purchase total: "))
    is_student_text = input("Student (YES/NO): ").strip().upper()
    is_senior_text = input("Senior (YES/NO): ").strip().upper()

    if purchase_total < 0.0:
        print("Error: invalid input")
    elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)
except:
    print("Error: invalid input")

# ==================================================
# 7.4 Problem 4: Basic statistics of three integers
# ==================================================
# Description:
# Reads 3 integers and outputs sum, average, max, min, and even flag.
# Test cases:
#  Normal: 2,4,6 -> all even
#  Border: 1,2,3 -> not all even
#  Error: "a",2,3 -> Error

try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)
except:
    print("Error: invalid input")

# ==================================================
# 7.5 Problem 5: Loan eligibility
# ==================================================
# Description:
# Determines loan eligibility based on income, debt ratio, and credit score.
# Test cases:
#  Normal: income 10000, debt 2000, score 700 -> eligible
#  Border: income 8000, debt 3200, score 650 -> eligible
#  Error: income 0 -> Error

try:
    monthly_income = float(input("Monthly income: "))
    monthly_debt = float(input("Monthly debt: "))
    credit_score = int(input("Credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)
except:
    print("Error: invalid input")

# ==================================================
# 7.6 Problem 6: BMI and category flag
# ==================================================
# Description:
# Calculates BMI and determines category flags.
# Test cases:
#  Normal: 70kg, 1.75m -> normal
#  Border: BMI=18.5 -> normal
#  Error: height=0 -> Error

try:
    weight_kg = float(input("Weight (kg): "))
    height_m = float(input("Height (m): "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_r = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print("BMI:", bmi_r)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
except:
    print("Error: invalid input")

# --------------------------------------------------
# Conclusions
# --------------------------------------------------
# Each problem demonstrates input validation, conditionals, arithmetic
# processing, and boolean logic. The solutions follow clean variable
# naming and separation of concerns.

# --------------------------------------------------
# References
# --------------------------------------------------
# - Python Official Docs: https://docs.python.org/3/
# - Class Notes
 
 #Repo
#https://github.com/2530389-Enrique-Rivera/Metodologia_de_la_programacion.git