square_input=int(input("Please Enter Number Chessboard: "))
gains=[]
for i in range(square_input):
  result = 2 ** i
  gains.append(result)
  print(f"{gains}")