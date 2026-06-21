def respons(question):
    if question == "" :
        respon = "Fine. Be that way!"
    elif question.endswith("?") and question == question.upper() :
        respon = "Calm down, I know what I'm doing!"
    elif question == question.upper():
        respon = "Whoa, chill out!"
    elif question.endswith("?"):
        respon = "Sure."
    else:
        respon = "Whatever."
    return respon
def main():
    while True:
      try:
        question_input= input("Please Enter Question: ")
        if question_input.isdigit():
            raise ValueError("Please Enter Question.")
        result = respons(question_input)
        print(result)
      except ValueError as Error:
          print(f"Error:{Error}")
if __name__ == "__main__":
    main()

    