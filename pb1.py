
number = int(input("Enter a number : "))

guess_5 = 0
guess_6 = 0
guess_7 = 0


guess = number /2
limit = 0


while limit < 5 :
    temp = number/ guess
    guess = (guess + temp) / 2
    limit += 1
    guess_5 = format(guess, ".3f")

guess = number /2
limit = 0
while limit < 6 :
    temp = number/ guess
    guess = (guess + temp) / 2
    limit += 1
    guess_6 = format(guess, ".3f")

guess = number /2
limit = 0

while limit < 7 :
    temp = number/ guess
    guess = (guess + temp) / 2
    limit += 1
    guess_7 = format(guess, ".3f")

    
print("Result of repeat the process five times :  ", guess_5)
print("Result of repeat the process six times :  ", guess_6)
print("Result of repeat the process seven times :  ", guess_7)

