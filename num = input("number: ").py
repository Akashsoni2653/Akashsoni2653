num = input("number: ")
dictionary = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" :"seven",
    "8" :"eight",
    "9" : "nine",
    "0" : "zero"
}
for number in num:
    result = ""
    result += dictionary.get(number,number) + " "
    print(result)