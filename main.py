player = {
    "hp": 20,
    "maxhp": 20
}
# valid_hp_number = [1,2,3,4,5]

def game():
    if player["hp"] <= 0:
        return print("You died!")

    

    # decrease_hp = input(f"Your HP is {player['hp']}. Decrease HP? ")

    # if decrease_hp == "yes":
        # decrease_amount = int(input("How much? (1-5) "))
        # if decrease_amount in valid_hp_number:
            # player["hp"] -= decrease_amount
        # else:
            # print("You can only decrease your HP by 1-5!")
    game() # Keep running the game

game()