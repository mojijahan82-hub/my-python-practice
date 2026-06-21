def kabise(Year):
    return Year % 4 == 0 and (Year % 100 != 0 or Year %400 == 0)
def main():
    while True:
        Year_input=int(input("Please Enter Your Year:"))
        if Year_input == 0:
          break
        elif kabise(Year_input) == True:
            print("Year Is leap.")
        elif kabise(Year_input) == False:
            print("Year Is Not Leap")

if __name__ == "__main__":
    main()