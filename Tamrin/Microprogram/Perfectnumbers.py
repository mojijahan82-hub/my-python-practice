def perfectnumber(number):
    count = 0
    for i in range(1 , number):
        if number % i == 0 : count+=i
    if  number == count: result = "Perfect"
    elif number < count: result = "Abundant"
    elif number > count: result = "Deficient"
    return result
def main():
    while True:
        try:
            number_input=int(input("Please Enter Number :"))
            if number_input < 1 :
                raise ValueError("Classification is only possible for positive integers.")
            print(f"Result: {perfectnumber(number_input)}")
        except ValueError as Error:
            print(f"Error: {Error}")
if __name__ == "__main__":
    main()