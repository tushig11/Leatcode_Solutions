# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

# Please note that both secret number and friend's guess may contain duplicate digits.

def getHint(self, secret: str, guess: str) -> str:
    bull = sum([secret[i] == guess[i] for i in range(len(secret))])
    both = sum(min(secret.count(x),guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bull,both-bull)

    
def BruteForce(self, secret: str, guess: str) -> str:
    b, c = 0, 0
    if secret == guess:
        return str(len(secret)) + "A0B"
    
    s = list(secret)
    g = list(guess)   
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            i = i - b
            del s[i]
            del g[i]
            b += 1

    for i in g:
        if i in s:
            k = s.index(i)
            if k != -1:
                c += 1
                del s[k]
    
    return "%d%s%d%s" % (b,"A",c,"B")

