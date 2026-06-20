from collections import Counter
import re
import pypdf

def Count(text):
    lower_text = text.lower()
    words = re.findall(r"\b\w+\b",lower_text)
    word_count = Counter(words)
    return word_count.most_common(n=10)

def main():
    status = input("Please Enter Your Status | [c] for copy paste | [R] Read For Text File | [P] Read From Pdf File | [A] All Page Of PDf:").upper()
    if status == "C":
        text = input("Please Enter Your Text:").strip()
    elif status == "R":
        address = input("Please Enter Your File Address:")
        f = open(address)
        text = f.read()
    elif status == "P":
        address = input("Please Enter Your File Address:")
        page_number = int(input("Please Enter Your Number Of Page You Want To Count:"))
        reader = pypdf.PdfReader(address)
        page_reader = reader.pages[page_number]
        text = page_reader.extract_text()
    elif status == "A":
        address = input("Please Enter Your File Address:")
        reader = pypdf.PdfReader(address)
        number_of_pages = len(reader.pages)
        
        open("main.txt","w",encoding="utf-8").close()

        for i in range(number_of_pages):
            page = reader.pages[i]
            add = page.extract_text()
            if add:
                with open("main.txt","a",encoding="utf-8") as f:
                  f.write(add)
        with open("main.txt","r", encoding="utf-8") as f:
              text=f.read()
    else:
        text = ""

    word_counter=Count(text)

    for word,count in word_counter:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()