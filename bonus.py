


def calculate_bonus(time,salary):
    if time> 5:
        total_salary = salary+(salary*.05)
    if time<= 5:
        total_salary=salary
    return total_salary

def main():
    time = float(input("How many years have you worked here? "))
    salary = float(input("What is your current salary? "))
    print("Your total salary is",calculate_bonus(time, salary))

main()
