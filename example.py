from Rank import Rank

from random import randrange
if __name__ == "__main__":
    
    players = {}
    # create 10 players with rank
    for i in range(0, 10):
        players[i] = Rank(i)

    # some text to beautify output
    verbose = {}
    verbose[0] = "lost vs"
    verbose[1] = "won vs"
    verbose[2] = "played a draw vs"
    
    # let players play random games versus each other
    for i in range(1, 10000):
        p1 = randrange(10)
        p2 = randrange(10)
        while(p2 == p1):
            p2 = randrange(10)
        gameResult = randrange(3)
        players[p1].vs(players[p2], gameResult)
        print (p1, verbose[gameResult], p2)
    
    print ("\nResults\n##############\n")

    # print sorted results
    for key, value in sorted(players.items(), key=lambda item: item[1].points, reverse = True):
        print("%s: %s" % (value.id, value.points))
        
        
    