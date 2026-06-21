def Raindrops(number):
    result = ""
    if number % 3 == 0:
      result += "pling "
    if number % 5 == 0:
      result += "plang "
    if number % 7 == 0:
      result += "Plong "
    if result == "":
      return str(number)
    else:
      return result
def main():
    while True:
      try:
        number_input = int(input("Please Enter Number Raindrops: "))
        print(f"Riandrop: {Raindrops(number_input)}")
      except ValueError as Error:
          print(f"Error:{Error}")
if __name__ == "__main__":
    main()