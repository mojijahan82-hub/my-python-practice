def chessboard(squares):
    grains=[]
    for i in range(squares):
        result = 2 ** i
        grains.append(result)
    return grains
def main():
    try:
      squares_input=int(input("Please Enter Number Chessboard: "))
      while squares_input < 0 or squares_input > 64:
          print("Error! Please Enter Number Between 1 And 64.")
          squares_input=int(input("Please Enter Agian Number Chessboard: "))
      grains=chessboard(squares_input)
      print("\n" + "-"*40)
      print(f"{"square":<10} {"Grains":>20}")
      print("-" * 40)
      for i in range(squares_input):
          print(f"{i+1:<10} {grains[i]:>20,}")
      print("-" * 40)
      print(f"{"Total:":<10} {sum(grains):>20,}")
      print("-" * 40)
    except ValueError as Error:
        print(f"Error:{Error}")
if __name__ == "__main__":
    main()

