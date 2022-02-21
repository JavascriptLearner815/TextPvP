player = {
    "hp": 20,
    "maxhp": 20
}
punch_times = 0
goblin_tolerance = 2
# valid_hp_number = [1,2,3,4,5]

def game(punch_times):
    if player["hp"] <= 0:
        return print("You died!")

    move = input("You encounter a goblin. What will you do? (punch, kick, hide) ")
    if move.lower() == "punch":
        print("You punch the goblin!")
        punch_times += 1
        print(f"You have punched him {punch_times} times!")

    # decrease_hp = input(f"Your HP is {player['hp']}. Decrease HP? ")

    # if decrease_hp == "yes":
        # decrease_amount = int(input("How much? (1-5) "))
        # if decrease_amount in valid_hp_number:
            # player["hp"] -= decrease_amount
        # else:
            # print("You can only decrease your HP by 1-5!")

    return punch_times

while True:
    punch_times = game(punch_times)
    