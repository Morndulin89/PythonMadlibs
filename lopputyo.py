 #A small program that lets you create madlibs-stories (two options)

#Introduces the program 
def opening():
    print("Hello and welcome to this small madlibs-program. ")
    print("We will create a story together and you can save the final product into the file.")
    print("I will prompt You to give me words to fill out the story.")

#Gives the necessary prompts for the 1st story
def story1Words():
    #Creates an empty list for the words
    wordList = []
    adj1 = input("Could you give me an adjective?   ")
    #Adds the word to the list
    wordList.append(adj1)
    adj2 = input("How about another adjective?  ")
    wordList.append(adj2)
    bird = input("Now I'd require a type of a bird.     ")
    wordList.append(bird)
    room = input("Could you think of a room in a house? ")
    wordList.append(room)
    verbPast = input("How about a verb in past tense?   ")
    wordList.append(verbPast)
    verb = input("Now just a regular verb, please?  ")
    wordList.append(verb)
    relative = input("I'd require a type of relative, please?   ")
    wordList.append(relative)
    noun1 = input("How about any kind of noun?  ")
    wordList.append(noun1)
    liquid  = input("Could you give me a type of liquid?    ")
    wordList.append(liquid)
    verbIng = input("Now I'd need another verb, this time ending with -ing? ")
    wordList.append(verbIng)
    bodyPart = input("Now I'd need a bodypart (in plural form)? ")
    wordList.append(bodyPart)
    nounPlur  = input("Could you give me a plural version of a noun?    ")
    wordList.append(nounPlur)
    verbIng2 = input("I'd need another verb ending -ing?    ")
    wordList.append(verbIng2)
    noun2 = input("And finally, one more noun, please?  ")
    wordList.append(noun2)
    #returns the created list
    return wordList

#Creates the 1st story
def createStory1(words):
    #adds a marker between stories
    filler = "\n##########################\n"
    a = "It was a " + words[0] + " November day. I woke up to the " + words[1] + " smell of " + words[2] + " roasting in the " + words[3] + " downstairs.\n" 
    b = "I " + words[4] + " down the stairs to see if I could help " + words[5] + " the dinner. My mom said, \"See if " + words[6] + " needs a fresh "+ words[7] + ".\"\n"
    c = "So I carried a tray of glasses full of " + words[8] + " into the " + words[9] + " room. When I got there, I couldn't believe my " + words[10] + "!\n"
    d = "There were " + words[11] + " " + words[12] + " on the " + words[13] + "!" 
    #creates a one longer string of the shorter ones
    concat = filler + a + b + c + d
    #makes the story in uppercase
    story = concat.upper()
    #returns the story
    return story

#Gives the necessary prompts for the 2nd story
def story2Words():
    wordList = []
    adj1 = input("Could you give me an adjective?   ")
    wordList.append(adj1)
    noun1 = input("How about any kind of noun?  ")
    wordList.append(noun1)
    adj2 = input("How about another adjective?  ")
    wordList.append(adj2)
    place = input("Now I'd require a place.     ")
    wordList.append(place)
    adj3 = input("How about another adjective?  ")
    wordList.append(adj3)
    adj4 = input("And another adjective?  ")
    wordList.append(adj4)
    vehicle = input("Could you think of a vehicle, in plural form? ")
    wordList.append(vehicle)
    adj5 = input("And yet another adjective?  ")
    wordList.append(adj5)    
    plurNoun = input("How about another noun, in plural?   ")
    wordList.append(plurNoun)
    adj6 = input("And once again an adjective?  ")
    wordList.append(adj6)
    plurNoun2 = input("Another plural noun, please?   ")
    wordList.append(plurNoun2)
    adj7  = input("How about another adjective?    ")
    wordList.append(adj7)
    plurNoun3 = input("Another plural noun, please?   ")
    wordList.append(plurNoun3)
    adj8 = input("Once again an adjective? ")
    wordList.append(adj8)
    noun2 = input("Now I'd need a regular noun? ")
    wordList.append(noun2)
    verb  = input("Could you give me a verb?    ")
    wordList.append(verb)
    plurNoun4 = input("Another plural noun, please?   ")
    wordList.append(plurNoun4)
    verb2 = input("Another verb, please?   ")
    wordList.append(verb2)
    job = input("Could you think of a job, in plural form? ")
    wordList.append(job)
    adj9  = input("How about another adjective?    ")
    wordList.append(adj9)
    verb3 = input("One more verb, please?   ")
    wordList.append(verb3)
    adj10 = input("And finally, one more adjective, please?  ")
    wordList.append(adj10)
    return wordList

def createStory2(words):
    filler = "\n##########################\n"
    a = "Star Wars is a " + words[0] + " " + words[1] + " of " + words[2] + " versus evil in a " + words[3] + " far far away.\n"
    b = "There are " + words[4] + " battles between " + words[5] + " " + words[6] + " in space and " + words[7] + " duels with " + words[8] + " called " + words[9] + " sabers.\n"
    c = words[10] + " called \"droids\" are helpers and " + words[11] + " to the heroes.\n"
    d = "A " + words[12] +" power called \"The " + words[13] +"\" " + words[14] + "s people to do " + words[15] + " things, like " + words[16] + " " + words[17] + ".\n"
    e = "The Jedi " + words[18] + " use The Force for the " + words[19] + " side and the Sith " + words[20] + " it for the " + words[21] + " side."
    concat = filler + a + b + c + d + e
    story = concat.upper()
    return story

#creates a new file if necessary or adds the created story to the existing file
def writeStory(story):
    f = open("storytime.txt", "a")
    f.write(story)
    f.close()

#prints out all the stories saved in the file
def printStories():
    f = open("storytime.txt", "r")
    for line in f:
        print(line)
#declaring a variable for starting the game (default is "y")
cont = "y"
#as long as the player gives Y, the game continues
while cont == "y" or cont == "Y":
    #creating empty list and string variables 
    wordList = []
    story = ""
    #choosing the story or skipping creating a new
    choice  = input("Would you like story 1, story 2 or skip creating new?(Press 1, 2 or something else)")
    #if the player chooses 1 or 2, game enters another if/else
    #game enters first function prompting the words and then creates a story from them
    if choice == "1" or choice == "2":
        if choice == "1":
            wordList = story1Words()
            story = createStory1(wordList)
        else:
            wordList = story2Words()
            story = createStory2(wordList)
        print("Your words were: ", wordList)
        print("And here's your story: ")
        print(story)
    #if player presses something else, creating a new story is skipped altogether
    else:
        break
    #player is asked if they want to save the story or note
    save = input("Would you like to save your story? y/n    ")
    if save == "y" or save =="Y":
        writeStory(story)
    #player is asked if he wants to create another story
    cont = input("If you want to try again, press \"Y\".    ")
#game ends
print("Thank you for playing!")
#all the stories are printed, if the player so wants
printTexts = input("Would you like to print the stories you have saved so far? y/n   ")
if printTexts == "y" or printTexts == "Y":
    printStories()
print("You can still find your created stories from the same folder as this file.")