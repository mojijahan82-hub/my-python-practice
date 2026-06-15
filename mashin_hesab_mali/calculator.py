def calculate(monthly_income,tax_rate,month_expences,currency):
    monthly_tax= monthly_income*(tax_rate/100)
    monthly_full_income=monthly_income - monthly_tax
    monthly_full_new = monthly_full_income - month_expences
    year_income = monthly_income * 12
    yearly_tax=monthly_tax * 12
    year_full_income= year_income - yearly_tax
    year_expences= month_expences * 12
    year_full_new= year_full_income - year_expences

    print("---------------------------------------")
    print(f"monthly income:{monthly_income:,.3f}{currency}")
    print(f"tax rate:{tax_rate:,.0f}")
    print(f"monthly tax:{monthly_tax:,.3f}{currency}")
    print(f"monthly full income:{monthly_full_income:,.3f}{currency}")
    print(f"monthly expences:{month_expences:,.3f}{currency}")
    print(f"monthly full new:{monthly_full_new:,.3f}{currency}")
    print(f"year income:{year_income:,.3f}{currency}")
    print(f"yearly tax:{yearly_tax:,.3f}{currency}")
    print(f"yearly full income:{year_full_income:,.3f}{currency}")
    print(f"yearly expences:{year_expences:,.3f}{currency}")
    print(f"yearly full new:{year_full_new:,.3f}{currency}")
    print("---------------------------------------")


def main():
    try:
      monthly_income_input = float(input("please enter yout monthly income:"))
      tax_rate_input= float(input("please enter your tax rate(%):"))
      monthly_expences_input=float(input("Please enter your monthly expences:"))
    
      calculate(monthly_income_input,tax_rate_input,monthly_expences_input,"Toman")
    except ValueError as e:
        print(f"error :{e}")
if __name__ == '__main__':
    main()