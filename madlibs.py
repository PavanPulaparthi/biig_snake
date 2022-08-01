#  # string concatenation (How to put strings together)
#  # supposee we want to create a string that says "Subscribe to ___________"
# youtuber = "plio" # some string variable

#  # a few ways to do this
# print("Subscribe to "+ youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj =input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Person: ")
madlib = f"Jessica Hagelscamp is so {adj}! It makes me so excited all the time because, \
I love to {verb1}. Stay hydrated nd {verb2} like you are {famous_person}!" 
print (madlib)