import random

map = [["","",""], ["","",""], ["","",""]]
unsearched_map = [[" "," "," "], [" "," "," "], [" "," "," "]]
treasure = "treasure"
trap = "trap"
found_treasure= False
alive = True

def create_map(empty_map):
    
    treasure_row = random.randint(0,2)
    treasure_column = random.randint(0,2)
    empty_map[treasure_row][treasure_column] = "treasure"
    traps = int(input("How many traps do you want: "))

    set_traps(empty_map,traps)
    

    return empty_map

def set_traps(empty_map,trap_amount = 3):
    i=0
    while(i<trap_amount):
        trap_row = random.randint(0,2)
        trap_column = random.randint(0,2)
        if(empty_map[trap_row][trap_column] == ""):
            empty_map[trap_row][trap_column] = "trap"
        else:   
            continue
        i +=1

def search(living):
    guess_row = int(input("Which row you want to visit: "))
    guess_column = int(input("Which column you want to visit: "))
    
    check_index(guess_row,guess_column,living)

def check_index(guessRow,guessCol,living):
    if(unsearched_map[guessRow][guessCol] == " "):
        pass
    else:
        print("already guessed")
        return
    #print(map[guessRow][guessCol])
    if(map[guessRow][guessCol] == "trap"):
        print("BOOM! You hit a trap and died.")
        print(alive)
        ali = False
        unsearched_map[guessRow][guessCol] == "🏴‍☠️"
    elif(map[guessRow][guessCol] == "treasure"):
        print("You found the treasure! Good Job!")
        found_treasure = True
        unsearched_map[guessRow][guessCol]
        unsearched_map[guessRow][guessCol] == "👑"
    else:
        unsearched_map[guessRow][guessCol] = "x"
    
    
    

    return 

create_map(map)
#print(map)
while(alive == True and found_treasure ==False):
    search(alive)
    print(unsearched_map[0])
    print(unsearched_map[1])
    print(unsearched_map[2])
    print("Alive: ",alive)
    print("Treasure found: ",found_treasure)
print("reached the end")