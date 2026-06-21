def triangle_type(x,y,z):
    if x <= 0 or y <= 0 or z <= 0:
        return False
    elif (x + y < z) or (y + z < x) or (x + z < y):
        return False
    else:
        return True
def main():
    x_input= float(input("Please Enter Side 1: "))
    y_input = float(input("Please Enter Side 2: "))
    z_input = float(input("Please Enter Side 3: "))
    result = triangle_type(x_input,y_input,z_input)
    if result == False:
        print("Not a Triangle")
    elif result == True:
        if x_input == y_input == z_input:
            print("equilateral")
        elif x_input == y_input or y_input == z_input or x_input == z_input:
            print("isosceles")
        else:
            print("scalene")

if __name__ == "__main__":
    main()