#! python3
# sandwichMaker.py ATBS Chp 8, 2nd last challenge

import pyinputplus as pyip
import time
#dictionarys of ingredients and costing
sandwiches={'bread': {'wheat': 2, 'white': 1.5, 'sourdough': 3},
            'protein': {'chicken': 1.5, 'turkey': 2.5, 'ham': 2, 'tofu': 0.5},
            'cheese': {'cheddar': 0.4, 'Swiss': 1.2, 'mozzarella': 0.8},
            'extras': {'mayo': 0.2, 'mustard': 0.2, 'lettuce': 0.1, 'tomato': 0.1},
            }
#welcomes
print('Welcome to Deli Duck!')
time.sleep(3)
#choice of ingredients (tally cost)
print('What type of bread would you like?')
bread = pyip.inputMenu(list(sandwiches['bread'].keys()), numbered=True, caseSensitive=False)
print('What\'s your preference for protein?')
protein = pyip.inputMenu(list(sandwiches['chicken'].keys()), numbered=True, caseSensitive=False)
wantCheese = pyip.inputYesNo(prompt ="Do you want cheese?\n")
if wantCheese = 'yes':
    print("What kind of cheese?")
    cheese = pyip.inputMenu(list(sandwiches['cheese'].keys()), numbered=True, caseSensitive=False)
for extra in list(sandwiches[extras].keys()):
    print("Would you like" + extra + "?")
    str(extra) = pyip.inputYesNo #this doesn't seem to be possible

#Function to sum the cost
def price:
    





#display of chosen ingredients and total cost
