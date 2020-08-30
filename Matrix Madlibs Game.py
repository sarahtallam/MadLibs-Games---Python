# Initialize variables
TheMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["", "", "", ""]
adj = ["", ""]


# Get input from user
print ("Welcome, user!")
print ("Let's play a game of madlibs!")
neo = input("What's your name? \n")

# Getting theMatrix variable from user
print(f"Hello {neo}! Are you ready?")
theMatrix = input("What is something you want to know more about? \n")

# Getting system variable from user
print (f"OoOoOoh! You want to know more about {theMatrix}, huh?")
print (f"Okay, well, first tell me what you already know about {theMatrix}.")
system = input(f"What noun would you categorize {theMatrix} as: \n ")

# Getting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}: \n")

# Getting inside variable from user
inside = input(f"Now give me any relaxing noun that's in the present tense:\n")

# Getting all profession variable from user
print(f"Okay, now I need four professions relating to {system}:\n")

for i in range(len(profession)):
        profession[i] = input(f"Profession (plural) {i+1} / {len(profession)}: \n")

# Getting the save variable from user
save = input(f"Please write a hero-related verb (present tense): \n")

# Getting the unplugged variable from user
unplugged = input(f"Now, please write a verb that makes you think about relief (past tense): \n")

# Getting the adjectives variable from user
print(f"Lastly, I need you to write me two dystopian adjectives: \n")

for i in range(len(adj)):
        adj[i] = input(f"Adjective {i+1} / {len(adj)}: \n")
        
# Getting the fight variable from user
fight = input(f"and a verb: \n")


# Initialize story
madlibsStory = (f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
        f"But when you're {inside}, you look around, what do you see? " +
        f"{profession[0]}, {profession[1]}, {profession [2]}, {profession [3]}. The very minds " +
        f"of the people we are trying to {save}. But until we do, these " +
        f"people are still a part of that {system} and that makes them " +
        f"our {enemy}. You have to understand, most of these people are " +
        f"not ready to be {unplugged}. And many of them are so {adj[0]}, " +
        f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")
# Print story
print (madlibsStory)
input()

