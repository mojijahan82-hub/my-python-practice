def convert_bills(amount):
    bills = [100,50,10,5,2,1]
    result={}
    for bill in bills:
        count , amount = divmod(amount, bill)
        if count > 0:
            result[bill] = count
    return result
def main():
    while True:
        try:
            amount_input= int(input("Please Enter Amount: "))
            print(f"Your Convert: {convert_bills(amount_input)}")
        except ValueError as Error:
            print(f"Error: {Error}")
if __name__ == "__main__":
    main()