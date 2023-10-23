# Eva D
# 10/23/2023
# Details if a set of 3 random numbers can make a triangle


import random

def is_triangle(side1, side2, side3):
    if (side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1:
        return True
    #elif (side1+side2)<side3 or (side1+side3)<side2 or (side2+side3)<side1:
    else:
        return False


def main():
    side1= random.randint(1,10)
    side2 = random.randint(1,10)
    side3 = random.randint(1,10)
    print(side1,side2,side3)
    if is_triangle(side1,side2,side3) == True:
        print("These lengths can make a triangle!")
    elif is_triangle(side1,side2,side3) == False:
        print("These lengths cannot form a triangle.")

if __name__ == '__main__':
    main()

