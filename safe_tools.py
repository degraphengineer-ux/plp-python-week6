def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"

def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"

# Test cases to match the required output
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))