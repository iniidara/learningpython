import random
def prob_dice_atleast(Nrolls, n_at_least):
    dice = ['.', ':', ':.', '::', '::.', ':::']
    Nsims = 10000
    how_many_matched = []
    for i in range(Nsims):
        matched = 0
        for i in range(Nrolls):
            roll = random.choice(dice)
            if roll == '::':
                matched += 1
        how_many_matched.append(matched)

    count = 0
    for i in how_many_matched:
        if i >= n_at_least:
            count += 1
    print(count/len(how_many_matched))

prob_dice_atleast(7, 3)
prob_dice_atleast(1, 1)