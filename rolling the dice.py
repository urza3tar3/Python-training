import random
#dice_outcome1 = random.randint(1,6)
#dice_outcome2 = random.randint(1,6)
#print(f"({dice_outcome1},{dice_outcome2})")


class Dice:
    def roll_the_dice(self):
        dice_outcome1 = random.randint(1, 6)
        dice_outcome2 = random.randint(1, 6)
        #print(f"({dice_outcome1},{dice_outcome2})")
        return (dice_outcome1, dice_outcome2) #returning them as tuples, bdal the line above


dice = Dice()
print(dice.roll_the_dice()) #pep8 is responsible for a perfect formate in pycharm you learn as you go

