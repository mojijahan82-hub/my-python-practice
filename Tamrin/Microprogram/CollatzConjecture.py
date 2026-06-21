def Collatz(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")  
    count = 0
    while number != 1 :
        if number % 2 == 0:
            number = number // 2
            count += 1
        else:
            number = (number * 3) + 1
            count += 1
    return count
def main():
    while True:
      try:
        number_input = int(input("Please Enter Number: "))
        print(f"Collatz Your Number({number_input}):" , Collatz(number_input))
      except ValueError as Error:
          print(f"Error: {Error}")
if __name__ == "__main__":
    main()