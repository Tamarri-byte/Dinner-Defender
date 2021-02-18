

class BasicRecipe:
    def __init__(self,name,ingridients):
        self.name = name
        self.ingridients = ingridients

class Ingridients:
    def __init__(self,ingriName,ingriAmount,ingriUnit):
        self.ingriName = ingriName
        self.ingriAmount = ingriAmount
        self.ingriUnit = ingriUnit

class Directions:
    def __init__(self,direction):
        self.direction



def createNewRecipe():

    

    recipeName = input("Name your new recipe: ")
    ingridientList = []
    directions = []

    print("Let's start with the ingridients...")

    ingridientsDone = False

    while not ingridientsDone:
        ingridientName = input('What is the name of this ingridient? (e.g. "Cheddar")')
        ingridientUnit = input('What will be the unit of measure? (e.g. "oz")' )
        ingridientAmount = input(f'How many {ingridientUnit}(s) is needed?')
        
        currentIngriDone = -1
        while currentIngriDone == -1:
            print(f"Name: {ingridientName} \n Amount: {ingridientAmount} {ingridientUnit}(s)" )
            correct = input("Does this look correct? (y/n): " )

            if correct == "y":
                currentIngriDone = 1
                newIngri = Ingridients(ingridientName,ingridientAmount,ingridientUnit)
                ingridientList.append(newIngri)
                #add ingridient
                
            elif correct == "n":
                currentIngriDone = 0
            else:
                print("You didn't confirm if this was fine, lets try again.")
                continue
        
        if currentIngriDone == 1:
            finishedInput = input("Great, Are you all done with this recipe? (y/n)")
            if finishedInput == "y":
                break
            elif finishedInput == "n":
                continue #go to the next ingridient
        else:
            continue #ignore this ingri and create a new one

        


createNewRecipe()
    

