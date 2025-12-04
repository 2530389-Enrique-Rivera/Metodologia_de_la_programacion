# Portada:

#Name: Enrique De Jesus Rios Rivera
#Matriculation: 2530389
#Group: IM 1-3

# -----------------------------------------------------------------------------
# Executive Summary:
# - A function in Python is a named block of code that groups statements to perform
#   a specific task and can be called from other parts of the program.
# - Parameters are named variables in a function definition; arguments are the
#   actual values passed to the function when it is called.
# - Separating logic into reusable functions improves readability, testability,
#   and reuse across the program.
# - A return value is the result a function provides back to the caller. Returning
#   results is preferred over printing because the caller can further process the
#   value (composition, testing) and decouples computation from presentation.
# - This document includes six problems: rectangle computations, grade
#   classification, list statistics, apply discount (pure function), greeting with
#   default parameters, and factorial. For each problem: description, inputs,
#   outputs, validations, and three test cases (normal, border, error).
# -----------------------------------------------------------------------------
# Principles and Good Practices (brief):
# - Prefer small functions with single responsibility.
# - Avoid duplicating logic; extract repeated code into helper functions.
# - Try to write pure functions when possible (same output for same input).
# - Document functions with short comments describing parameters and return values.
# - Use clear, descriptive names: calculate_area, summarize_numbers, apply_discount.
# -----------------------------------------------------------------------------
# (Optional) Diagrams / tables:
# - Flow for Problem 3: parse string -> validate non-empty -> convert to floats ->
#   call summarize_numbers -> present results.
# - Table of test cases for each problem is shown in comments before each problem.
# -----------------------------------------------------------------------------
# Template for each problem (comments before its code):
# Problem X: <short title>
# Description: ...
# Inputs: ...
# Outputs: ...
# Validations: ...
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...


# Problem 1: Rectangle area and perimeter
# Description:
# Calculate area and perimeter of a rectangle using two functions.
# Inputs:
# - width (float)
# - height (float)
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
# Validations:
# - width > 0 and height > 0
# Test cases:
# 1) Normal: width=5.0, height=3.2
# 2) Border: width=0.0001, height=0.0001
# 3) Error: width=-2, height=3

def calculate_area(width, height):
    """
    Return area of rectangle.
    Parameters:
      width (float): rectangle width (expected > 0)
      height (float): rectangle height (expected > 0)
    Returns:
      float: area
    """
    return width * height

def calculate_perimeter(width, height):
    """
    Return perimeter of rectangle.
    Parameters:
      width (float)
      height (float)
    Returns:
      float: perimeter
    """
    return 2 * (width + height)

def run_problem_1():
    print("\n--- Problem 1: Rectangle area and perimeter ---")
    test_cases = [
        ("Normal", 5.0, 3.2),
        ("Border", 0.0001, 0.0001),
        ("Error", -2, 3),
    ]
    for label, w, h in test_cases:
        print(f"\nTest case: {label}")
        try:
            width = float(w)
            height = float(h)
        except Exception:
            print("Error: invalid input")
            continue
        if width <= 0 or height <= 0:
            print("Error: invalid input")
            continue
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print("Area:", area)
        print("Perimeter:", perimeter)


# Problem 2: Grade classifier
# Description:
# Classify a numeric score (0-100) into letter grades A-F.
# Inputs:
# - score (float or int)
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
# Validations:
# - 0 <= score <= 100
# Test cases:
# 1) Normal: score=87
# 2) Border: score=90
# 3) Error: score=150

def classify_grade(score):
    """
    Return letter grade for a numeric score (0-100).
    Parameters:
      score (float): numeric score
    Returns:
      str: one of "A", "B", "C", "D", "F"
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def run_problem_2():
    print("\n--- Problem 2: Grade classifier ---")
    test_cases = [
        ("Normal", 87),
        ("Border", 90),
        ("Error", 150),
    ]
    for label, s in test_cases:
        print(f"\nTest case: {label}")
        try:
            score = float(s)
        except Exception:
            print("Error: invalid input")
            continue
        if not (0 <= score <= 100):
            print("Error: invalid input")
            continue
        category = classify_grade(score)
        # Display per conventions
        print("Score:", score)
        print("Category:", category)


# Problem 3: List statistics function (min, max, average)
# Description:
# Parse a comma-separated string of numbers and return min, max, average.
# Inputs:
# - numbers_text (string), e.g. "10,20,30"
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
# Validations:
# - numbers_text not empty after strip, all elements convertible to float, list non-empty
# Test cases:
# 1) Normal: "10, 20, 30"
# 2) Border: "5" (single element)
# 3) Error: "" (empty) or "10, abc, 30"

def summarize_numbers(numbers_list):
    """
    Return a dictionary with min, max, and average of numbers_list.
    Parameters:
      numbers_list (list of float)
    Returns:
      dict: {"min": float, "max": float, "average": float}
    """
    if not numbers_list:
        raise ValueError("numbers_list must not be empty")
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    average = sum(numbers_list) / len(numbers_list)
    return {"min": minimum, "max": maximum, "average": average}

def run_problem_3():
    print("\n--- Problem 3: List statistics ---")
    test_cases = [
        ("Normal", "10, 20, 30"),
        ("Border", "5"),
        ("ErrorEmpty", ""),
        ("ErrorBad", "10, abc, 30"),
    ]
    for label, text in test_cases:
        print(f"\nTest case: {label}")
        numbers_text = text
        if numbers_text.strip() == "":
            print("Error: invalid input")
            continue
        parts = [p.strip() for p in numbers_text.split(",") if p.strip() != ""]
        if not parts:
            print("Error: invalid input")
            continue
        numbers = []
        try:
            for p in parts:
                numbers.append(float(p))
        except Exception:
            print("Error: invalid input")
            continue
        try:
            summary = summarize_numbers(numbers)
        except Exception:
            print("Error: invalid input")
            continue
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", summary["average"])


# Problem 4: Apply discount list (pure function)
# Description:
# Given a list of prices and a discount rate (0-1), return a new list with discounted prices.
# Inputs:
# - prices_text (string), e.g. "100,200,300"
# - discount_rate (float between 0 and 1)
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
# Validations:
# - prices_text not empty, all prices > 0
# - 0 <= discount_rate <= 1
# Test cases:
# 1) Normal: "100,200", discount_rate=0.10
# 2) Border: "0.01, 0.02", discount_rate=0
# 3) Error: invalid price or discount_rate=1.5

def apply_discount(prices_list, discount_rate):
    """
    Return a new list of discounted prices. Does not modify original list.
    Parameters:
      prices_list (list of float): list of original prices (>0 expected)
      discount_rate (float): between 0 and 1
    Returns:
      list of float: discounted prices
    """
    discounted = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted.append(discounted_price)
    return discounted

def run_problem_4():
    print("\n--- Problem 4: Apply discount list ---")
    test_cases = [
        ("Normal", "100,200", 0.10),
        ("Border", "0.01, 0.02", 0.0),
        ("Error", "100, -50", 0.2),
        ("ErrorRate", "50, 60", 1.5),
    ]
    for label, prices_text, rate in test_cases:
        print(f"\nTest case: {label}")
        if prices_text.strip() == "":
            print("Error: invalid input")
            continue
        price_parts = [p.strip() for p in prices_text.split(",") if p.strip() != ""]
        if not price_parts:
            print("Error: invalid input")
            continue
        try:
            prices = [float(p) for p in price_parts]
        except Exception:
            print("Error: invalid input")
            continue
        if any(p <= 0 for p in prices):
            print("Error: invalid input")
            continue
        try:
            discount_rate = float(rate)
        except Exception:
            print("Error: invalid input")
            continue
        if not (0 <= discount_rate <= 1):
            print("Error: invalid input")
            continue
        discounted = apply_discount(prices, discount_rate)
        print("Original prices:", prices)
        print("Discounted prices:", discounted)


# Problem 5: Greeting function with default parameters
# Description:
# Create a greet(name, title="") function that returns "Hello, <full_name>!"
# Inputs:
# - name (string)
# - title (string, optional)
# Outputs:
# - "Greeting:" <greeting_message>
# Validations:
# - name not empty after strip
# Test cases:
# 1) Normal: name="Alice", title="Dr."
# 2) Border: name=" Bob " (title empty)
# 3) Error: name="" or "   "

def greet(name, title=""):
    """
    Return a greeting string. If title is not empty, it is placed before the name.
    Parameters:
      name (str): person's name (non-empty)
      title (str): optional title
    Returns:
      str: greeting message
    """
    name_clean = name.strip()
    title_clean = title.strip()
    if title_clean:
        full_name = f"{title_clean} {name_clean}"
    else:
        full_name = name_clean
    return f"Hello, {full_name}!"

def run_problem_5():
    print("\n--- Problem 5: Greeting with default parameters ---")
    test_cases = [
        ("Normal", {"name": "Alice", "title": "Dr."}),
        ("Border", {"name": " Bob ", "title": ""}),
        ("Error", {"name": "   ", "title": "Eng."}),
    ]
    for label, params in test_cases:
        print(f"\nTest case: {label}")
        name = params["name"]
        title = params.get("title", "")
        if name.strip() == "":
            print("Error: invalid input")
            continue
        greeting = greet(name, title=title)
        print("Greeting:", greeting)


# Problem 6: Factorial function (iterative)
# Description:
# Compute factorial n! for non-negative integers n. Implemented iteratively to avoid recursion limits.
# Inputs:
# - n (int)
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
# Validations:
# - n is integer
# - n >= 0
# - n <= 20 (to avoid extremely large results)
# Test cases:
# 1) Normal: n=5
# 2) Border: n=0
# 3) Error: n=-3 or n=21

def factorial(n):
    """
    Compute factorial iteratively. Chosen iterative implementation to avoid recursion depth and
    repeated function-call overhead for larger n.
    Parameters:
      n (int): non-negative integer
    Returns:
      int: n!
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def run_problem_6():
    print("\n--- Problem 6: Factorial ---")
    test_cases = [
        ("Normal", 5),
        ("Border", 0),
        ("ErrorNegative", -3),
        ("ErrorLarge", 21),
    ]
    for label, n_val in test_cases:
        print(f"\nTest case: {label}")
        try:
            n = int(n_val)
        except Exception:
            print("Error: invalid input")
            continue
        if n < 0 or n > 20:
            print("Error: invalid input")
            continue
        fact = factorial(n)
        print("n:", n)
        print("Factorial:", fact)


# Main runner: call each problem's runner so the file executes tests when run.

def main():
    run_problem_1()
    run_problem_2()
    run_problem_3()
    run_problem_4()
    run_problem_5()
    run_problem_6()

if __name__ == "_main_":
    main()

# Conclusions:
# - Functions help organize logic into reusable building blocks and make code easier
#   to read and test. Small functions with single responsibilities reduce complexity.
# - Returning values with 'return' allows callers to decide how to present or further
#   process results; it separates computation from I/O.
# - Default parameters and named arguments increase flexibility and readability.
# - Encapsulating repeated logic (e.g., parsing and validation) reduces duplication.
# - The main program coordinates calls to pure functions and handles user-visible I/O,
#   keeping computation separate from presentation.

# References (minimum 5):
# 1. Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. Python Software Foundation.
# 2. Lutz, M. (2013). Learning Python (5th Edition). O'Reilly Media.
# 3. Zelle, J. (2010). Python Programming: An Introduction to Computer Science. Franklin, Beedle & Associates.
# 4. PEP 8 -- Style Guide for Python Code. https://peps.python.org/pep-0008/
# 5. Python Standard Library Documentation. https://docs.python.org/3/library/
# 6. Freeman, E., & Robson, E. (2012). Head First Programming. O'Reilly Media.

#Repo
#https://github.com/2530389-Enrique-Rivera/Metodologia_de_la_programacion.git