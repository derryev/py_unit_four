# Eva D
# 10/18/2023
# Calculates total salary of someone at a company, accounting for if they get a bonus


def calculate_bonus(time,salary):
    """
    calculates total salary accounting for if they recieve bonus
    :param time: number of years person has worked for company
    :param salary: the person's salary
    :return: the total salary accounting for if the person recieves a bonus
    """
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
