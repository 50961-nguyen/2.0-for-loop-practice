## Setup
1. Git Clone this repository in your Unti 2 Folder
2. Make a file called for_loop_practice.py in this folder. 

## Instructions
Write a program that asks a user to enter whether they won (W) or lost (L) each of their last ten games using a for loop. 
Assume there were no ties. 

If there are any invalid inputs (ex. WINS, blah, w, etc.), print "Invalid input". Track the number of invalid inputs.

Output to the user the total number of wins and the total number of losses.

Don't forget header and IPO comments

## Sample Output

    Please enter your win or loss from the last ten games.
    Enter result of game (W) or (L): W
    Enter result of game (W) or (L): L
    Enter result of game (W) or (L): WINSS
    Invalid input
    Enter result of game (W) or (L): W
    Enter result of game (W) or (L): W
    Enter result of game (W) or (L): W
    Enter result of game (W) or (L): L
    Enter result of game (W) or (L): L
    Enter result of game (W) or (L): W
    Enter result of game (W) or (L): W

    You won 6 game(s).
    You lost 3 game(s).
    You had 1 invalid input(s).

## Starter Code
```python
"""
Header comments here
"""

# TODO: create variables to track the number of wins, losses, and invalid inputs

# TODO: set up for loop for 10 rounds 

    result = input("Enter result of game (W) or (L): ")

    # TODO: check user input, if they typed "W", then increase win count, if they typed "L", then increase loss count
    # Anything else will print "Invalid Input" and increase the invalid count
    
    
# TODO: Print the results
```
