def reverse(string):
    string.reverse()
    result = "".join(string)
    return result
def main():
    while True:
      try:
        string_input=input("Please Enter Your string:").strip()
        if string_input.isdigit():
           raise ValueError("Please Enter String.")
        string_list = list(string_input)
        print(f"result: {reverse(string_list)}")
      except ValueError as Error:
         print(f"Error: {Error}")
if __name__ == "__main__":
    main()


