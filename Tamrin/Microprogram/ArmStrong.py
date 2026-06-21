def Armstrong(number):
    str_number=str(number)
    if sum(int(i) ** len(str_number) for i in str_number) == number:
        return True
    else:
        return False
def main():
        while True:
          try:
            number_input= input("Please Enter number (or 'exit' to quit) : ")
            if number_input.lower() == "exit":
              break
            num=int(number_input)
            result= Armstrong(num)
            if result == True:
                print(f"Your Number ({number_input}) Is Armstrong.")
            elif result == False:
                print(f"Your Number ({number_input}) Is Not Armstrong")
          except ValueError as Error:
                print(f"Error: {Error}")
if __name__ == "__main__":
    main()
