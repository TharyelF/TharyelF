
#  string concatenation (aka how to ptu strings together)
# suppouse we want to create a string that says "subscribe to ___________"
#youtuber = "Tharyel Faria" # some string variable

# a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")


from os import link


adj = input("adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")


madlib = f"Programar é muito {adj}! Me deixa muito animado em descobrir novas coisas \
Eu vivo para {verb1}. Fique bem e {verb2} bastante coca igual {famous_person}!"

print(madlib) 

link = input("link: ")


madlib = f"{link}"

print(madlib)

