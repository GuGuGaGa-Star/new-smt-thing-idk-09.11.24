with open("quotes.txt", "r", encoding="utf-8") as skibidy_sigma:
    data = skibidy_sigma.read()

print(data)

answer = input("Напиши свое прізвище -")

with open("quotes.txt", "a", encoding="utf-8") as skibidy_sigma:
    skibidy_sigma.write("\n" + answer)

with open("quotes.txt", "r", encoding="utf-8") as skibidy_sigma:
    data = skibidy_sigma.read()

print(data)
