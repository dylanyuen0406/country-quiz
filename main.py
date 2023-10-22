isgameover = False
score = 0
lvl1qns = ["Which continent is USA located?", "Which is the biggest country in the world?",
           "Which country borders Portugal?", "which country won the recent Qatar World Cup?",
           "How many states does USA have?", "which country does the state of Michigan belong to?",
           "Which country borders Alaska?", "Which country is the biggest country in Africa?",
           "Which continent does Lebanon belong to?", "Which country would appear last in the dictionary?"]
lvl1ans = ["NorthAmerica", "Russia", "Spain", "Argentina", "Fifty", "USA", "Canada", "Algeria", "Asia", "Zimbabwe"]
lvl2qns = ["Which is the only country to date to gain independence unwillingly?",
           "Which country has more than one capital?", "Which is the most populous country in Africa?",
           "Which country is the safest in the world?", "Which country in the UN has the smallest land area?",
           "Which country invented french fries?", "Which country had the former name of Siam?",
           "Which country's flag contains a cactus?", "Which country's flag is neither rectangular nor square?",
           "Which country's flag was once a triangle?"]
lvl2ans = ["Singapore", "South Africa", "Nigeria", "Iceland", "Monaco", "Belgium", "Thailand", "Mexico", "Nepal",
           "China"]

for e in range(1):
    for i in lvl1qns:
        k = input(i)
        for j in lvl1ans:
            if k == j:
                print("ok")
                score += 1
            else:
                if e == 1:
                    print("You lose")
if score == 10:
    print("Congrats!Let's move on to Level 2!")
    score -= 10
    for e in range(1):
        for a in lvl2qns:
            b = input(a)
            for c in lvl2ans:
                if b == c:
                    print("ok")
                    score += 1
                else:
                    if e == 1:
                        print("you lose")
if score == 10:
    print('YAAAAAAy')
    print(";3")
