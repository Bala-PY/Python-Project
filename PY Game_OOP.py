import random 

class Game():
    user_name =''
    category =''
    animals = ''

    def __init__(self,user_name):
        print ("Welcome ", user_name, "! Lets begin the game.")
        self.user_name = user_name
        self.initialize_dict()
        self.play()
        
    def initialize_dict(self):
        self.animals = {'parrot': "I am a bird; I am green in color and have reddish beak",
                        'peacock': "I am a bird. I am colorful and known as the national bird of India",
                        'hen': "I am a domestic bird and give you eggs for omelette",
                        'crocodile': "I am a reptile; I am brownish green in colour, big in size and live in water.",
                        'snake': "I am a reptile. I make a hiss sound and can move without any legs",
                        'lizard': "I am a reptile; I live in most houses and I can easily crawl on the walls",
                        'bee': "I am an insect and I help with pollination and collect honey",
                        'mosquito': "I am an insect and I drink blood and spread disease",
                        'butterfly': "I am an insect and I have beautiful wings and I love nectar"}

    def play(self):
        print("Guess who I am from the below hints")
        randomanimal = random.choice(list(self.animals.keys())) #converting keys into list
        hints = self.animals.get(randomanimal)
        print(hints)
        print ( "your guess : ")
        guess = input().lower().strip() #get input from user here #convert guess to all lowercase and remove any whitespaces from the beginning or end. 
        if guess == randomanimal:
            print("You are right!")
        else:
            print("Wrong guess!")
            print("Would you like to continue the game(Y/N)?") 
            if(input().upper() == 'Y'): # get user input and if "Y"
                self.play()

class Game_attempt(Game):
    attempt = 2
    
    def play(self):
        print("Function Overriding Active :)") #Function overriding test line
        print("Guess who I am from the below hints")
        randomanimal = random.choice(list(self.animals.keys())) #converting keys into list
        hints = self.animals.get(randomanimal)
        print(hints)
        print ( "your guess : ")
        guess = input().lower().strip() #get input from user here #convert guess to all lowercase and remove any whitespaces from the beginning or end. 
        while(True):
            if guess == randomanimal:
                print("You are right!")
                print("Would you like to play the game again(Y/N)?") 
                if(input().upper() == 'Y'): # get user input and if "Y"
                    self.attempt = 2
                    self.play()
                break           
                            
            else:
                if self.attempt == 0:
                    print("Wrong guess! Game over!! Would you like to play again (Y/N)?") 
                    if(input().upper() == 'Y'): # get user input and if "Y"
                        self.attempt = 2
                        self.play()
                    break
                print("Wrong guess! You have " +str(self.attempt) +" more attempt.\nPlease retry.")
                self.attempt -= 1
                guess = input().lower().strip()
                        
if __name__ == "__main__":
    print(" Welcome to animal guessing game. Please enter your name: ")
    user_name = input() #get user name and store it in the variable user_name. IT will be passed to the constructor of Game class
    #Gameobj = Game(user_name)
    Gameobj = Game_attempt(user_name)
