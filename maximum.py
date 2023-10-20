

def max(number_1, number_2):
    if number_1 > number_2:
        larger = number_1
        return larger
    elif number_1<number_2:
        larger = number_2
        return larger
    else:
       larger = "There cannot be a maximum when both numbers are the same!"
       return larger

def main():
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))
    print(max(number_1,number_2))



main()
