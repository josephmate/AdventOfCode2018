
def solve1(val):
    #Only two recipes are on the board: the first recipe got a score of 3, the second, 7.
    scores = []
    scores.append(3)
    scores.append(7)

    #Each of the two Elves has a current recipe: the first Elf starts with the
    #first recipe, and the second Elf starts with the second recipe.
    elf1Pointer = 0
    elf2Pointer = 1
    
    for i in range(0, val + 10):

        # To create new recipes, the two Elves combine their current recipes.
        # This creates new recipes from the digits of the sum of the current
        # recipes' scores. With the current recipes' scores of 3 and 7, their
        # sum is 10, and so two new recipes would be created: the first with
        # score 1 and the second with score 0. If the current recipes' scores
        # were 2 and 3, the sum, 5, would only create one recipe (with a score
        # of 5) with its single digit.
        recipeSum = scores[elf1Pointer] + scores[elf2Pointer]
        if recipeSum >= 10:
            scores.append(recipeSum // 10)
        scores.append(recipeSum % 10)

        # each Elf picks a new current recipe. To do this, the Elf steps forward
        # through the scoreboard a number of recipes equal to 1 plus the score of
        # their current recipe. So, after the first round, the first Elf moves
        # forward 1 + 3 = 4 times, while the second Elf moves forward 1 + 7 = 8
        # times. If they run out of recipes, they loop back around to the
        # beginning.
        elf1Pointer = (elf1Pointer + scores[elf1Pointer] + 1) % len(scores)
        elf2Pointer = (elf2Pointer + scores[elf2Pointer] + 1) % len(scores)

    result = ""
    for i in range(val, val+10):
        result += str(scores[i])

    return result




print(f'solve1(9) = {solve1(9)} should be: 5158916779')
print(f'solve1(5) = {solve1(5)} should be: 0124515891')
print(f'solve1(18) = {solve1(18)} should be: 9251071085')
print(f'solve1(2018) = {solve1(2018)} should be: 5941429882')
print(f'solve1(540391) = {solve1(540391)}')


def solve2(val):
    #Only two recipes are on the board: the first recipe got a score of 3, the second, 7.
    scores = []
    scores.append(3)
    scores.append(7)

    #Each of the two Elves has a current recipe: the first Elf starts with the
    #first recipe, and the second Elf starts with the second recipe.
    elf1Pointer = 0
    elf2Pointer = 1
    
    while True:
        # To create new recipes, the two Elves combine their current recipes.
        # This creates new recipes from the digits of the sum of the current
        # recipes' scores. With the current recipes' scores of 3 and 7, their
        # sum is 10, and so two new recipes would be created: the first with
        # score 1 and the second with score 0. If the current recipes' scores
        # were 2 and 3, the sum, 5, would only create one recipe (with a score
        # of 5) with its single digit.
        recipeSum = scores[elf1Pointer] + scores[elf2Pointer]
        if recipeSum >= 10:
            scores.append(recipeSum // 10)
        scores.append(recipeSum % 10)

        # each Elf picks a new current recipe. To do this, the Elf steps forward
        # through the scoreboard a number of recipes equal to 1 plus the score of
        # their current recipe. So, after the first round, the first Elf moves
        # forward 1 + 3 = 4 times, while the second Elf moves forward 1 + 7 = 8
        # times. If they run out of recipes, they loop back around to the
        # beginning.
        elf1Pointer = (elf1Pointer + scores[elf1Pointer] + 1) % len(scores)
        elf2Pointer = (elf2Pointer + scores[elf2Pointer] + 1) % len(scores)

        if len(scores)-len(val) >= 0:
            condition = ""
            for i in range(len(scores)-len(val), len(scores)):
                condition += str(scores[i])

            if condition == val:
                return len(scores) - len(val)



print(f'solve2("0124515891") = {solve2("0124515891")} should be: 5')

if False:
    print(f'solve2("51589") = {solve2("51589")} should be: 9')
    print(f'solve2("515891") = {solve2("515891")} should be: 9')
    print(f'solve2("5158916") = {solve2("5158916")} should be: 9')
    print(f'solve2("51589167") = {solve2("51589167")} should be: 9')
    print(f'solve2("515891677") = {solve2("515891677")} should be: 9')
    print(f'solve2("5158916779") = {solve2("5158916779")} should be: 9')
    print(f'solve2("01245") = {solve2("01245")} should be: 5')
    print(f'solve2("012451") = {solve2("012451")} should be: 5')
    print(f'solve2("0124515") = {solve2("0124515")} should be: 5')
    print(f'solve2("01245158") = {solve2("01245158")} should be: 5')
    print(f'solve2("012451589") = {solve2("012451589")} should be: 5')
    print(f'solve2("92510") = {solve2("92510")} should be: 18')
    print(f'sovle2("925107") = {solve2("925107")} should be: 18')
    print(f'sovle2("9251071") = {solve2("9251071")} should be: 18')
    print(f'sovle2("92510710") = {solve2("92510710")} should be: 18')
    print(f'sovle2("925107108") = {solve2("925107108")} should be: 18')
    print(f'sovle2("9251071085") = {solve2("9251071085")} should be: 18')
    print(f'solve2("59414") = {solve2("59414")} should be: 2018')
    print(f'solve2("594142") = {solve2("594142")} should be: 2018')
    print(f'solve2("5941429") = {solve2("5941429")} should be: 2018')
    print(f'solve2("59414298") = {solve2("59414298")} should be: 2018')
    print(f'solve2("594142988") = {solve2("594142988")} should be: 2018')
    print(f'solve2("5941429882") = {solve2("5941429882")} should be: 2018')
    print(f'solve2("540391") = {solve2("540391")}')

