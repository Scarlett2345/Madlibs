# string concantenation - putting strings together
country1 = "Kenya"

#a few wys to do it
print("I live in " + country1)
print("I live in {}".format(country1))
print(f"I live in {country1}")

#I prefer the f string so I´m gonna use that to create our madlib
#a madlib is a paragraphin which you fill in the blanks
noun = input("please enter a noun that is a compliment: ")
adj = input("Please enter an adjective: ")
noun1 = input("please enter a noun: ")
noun2 = input("please enter a noun: ")
verb = input("please enter a verb: ")

print(f"At last, My {noun} has come along. My {adj} are over and life is like a {noun1}.\
I found a {noun2} that i could {verb} to. ")


