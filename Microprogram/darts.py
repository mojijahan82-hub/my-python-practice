import math
class point:
    def __init__ (self , x = 0 , y = 0):
        self.x = x
        self.y = y
    def darts (self):
        score = 0
        result  = (self.x ** 2 + self.y ** 2) ** 0.5
        if result > 10 : score = 0
        elif result > 5 : score = 1
        elif result > 1 : score = 5
        else : score = 10
        return score
def main():
    while True:
        try:
            x_input=float(input("Please Enter X Point: "))
            y_input = float(input("Please Enter Y Point: "))
            result = point(x_input , y_input)
            score = result.darts()
            print(f"Your Score: {score}")
        except ValueError as Error:
            print(f"Error: {Error}")
if __name__ == "__main__":
    main() 