import zombiedice
import random 

class MyZombie:

    def __init__(self,name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dic with info about the current state of the game.
        # You can choose o ignore it in your code. 

        diceRollResults = zombiedice.roll() # first roll 
        # roll() returns a dictionary with keys 'brain', 'shotgun', and 'footsteps' with  how 
        # many rolls of each type there were. 
        # The 'rolls' key is a list of (color, icon) tuples with the exact roll result information.
        # Example of a roll() return value:
        # {'brains' : 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls' :[('yellow', 'brains'), ('red', 'footsteps'), ('green', 'shotgun')]}

        # Replace this zomibe code with your own:

        brains = 0 
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2 :
                diceRollResults = zombiedice.roll()
            else:
                break 


class MoveOrStay(MyZombie):

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        while diceRollResults and random.randint(0,1) == 0 :
            diceRollResults = zombiedice.roll()

class StopAtTwoBrain(MyZombie):
    
    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2 :
                diceRollResults = zombiedice.roll()
            else:
                break

class StopAtTwoShotgun(MyZombie):

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2 :
                diceRollResults = zombiedice.roll()
            else:
                break


class StopAtTwoShotgun(MyZombie):

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2 :
                diceRollResults = zombiedice.roll()
            else:
                break


class MoveOneOrFour(MyZombie):

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        roll_times = random.randint(1,4)
        shotgun = 0 
        turn = 1 

        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if turn != roll_times or shotgun < 2 :
                diceRollResults = zombiedice.roll()
                turn += 1
            else:
                break

class GunVsBrain(MyZombie):

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        shotgun = 0 
        brains = 0 

        while diceRollResults is not None:

            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            
            if shotgun > brains:
                break 
            else:
                diceRollResults = zombiedice.roll() 


zombies = (
    MyZombie(name='Normal Zombie'),
    StopAtTwoBrain(name='StopAtTwoBrain'),
    MoveOrStay(name='MoveOrStay'),
    StopAtTwoShotgun(name='StopAtTwoShotgun'),
    MoveOneOrFour(name='MoveOneOrFour'),
    GunVsBrain(name='GunVsBrain')
)


# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
