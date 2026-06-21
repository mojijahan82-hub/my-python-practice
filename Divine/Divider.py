def Divider(total,people,percent,status,currency):
    if status == "N":
        while True:
          try:
            percent_arr= percent.split(" ")
            arr_count= len(percent_arr)

            if arr_count != people:
                raise ValueError("Percent count not equal To people count.")
        
        
            if abs(sum(float(x)for x in percent_arr) - 100) > 0.001:
                raise ValueError("Total percent most be 100")
            
            break
          
          except ValueError as b:
            print(f"Error:{b}")
            percent = input("Please Enter Each Peron Percent With Space:")

        
        result =[total * (float(p) / 100) for p in percent_arr]

        print(f"Total expences:{total:,.3f}{currency}")
        print(f"Number of people:{people}")

        for id,share in enumerate(result,1):
            print(f"percent:{id} must pay {share:,.3f}{currency}")

    elif status == "E":

        share_money=total / people

        print(f"Total expences:{total:,.3f}{currency}")
        print(f"Number of people:{people}")
        print(f"Each percent must be pay:{share_money:,.3f}{currency}")

    else:
        raise ValueError("Invalid Status")

def main():
    while True:
        try:
            total_input=float(input("Please Enter Total Price:"))
            break

        except ValueError as b:
            print(f"Error:{b}")

    while True:
        try:
            people_input=int(input("Please Enter People:"))
            if people_input < 1:
                raise ValueError("Number Of People Must Be Greater Than 1.")
            break

        except ValueError as b:
            print(f"Error:{b}")

    while True:
        status_input=input("[E] For Equal Expences | [N] For Not Equal Expences .").upper()
        if status_input in ["E","N"]:
            break
        else:
            print("Error: Invalid Status")
    percent_input=""
    if status_input == "N":
          percent_input = input("Please Enter Each Peron Percent With Space:")

    Divider(total_input,people_input,percent_input,status_input,"Toman")

if __name__ == "__main__":
    main()