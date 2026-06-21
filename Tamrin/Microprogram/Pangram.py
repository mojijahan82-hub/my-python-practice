def isogram(string):
    seen_lettrs=[]
    for i in string:
        if i ==  "-" or i == " " or i == "_":
            continue
        if i in seen_lettrs:
            return False
        seen_lettrs.append(i)
    return True
def main():
    while True:
      try:
        string_input = input("Please Enter Your Word: ").lower()
        if isogram(string_input):
            print("It's an isogram!")
        else:
            print("It's NOT an isogram!")
      except ValueError as Error:
          print(f"Error: {Error}")
if __name__ == "__main__":
    main()