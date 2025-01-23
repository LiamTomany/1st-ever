print ('Welcome to My Computer Quiz')

playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()
    
print('Okay! Lets go, Good Luck!')
score = 0 
       
answer = input('Who is the Best Football Player in the World? ').lower()
if answer == 'rodri':
    print ('You at least have watched a game of football')
    score += 1
    
else: 
    print ('you have 0 ball knowledge!')

answer = input('How old am I? ')
if answer == '23':
    print ('You should know that!')
    score += 1

else: 
    print ('we are not friends')

answer = input('Who is my best friend? ').lower()
if answer == 'Leo' or 'leo':
    print ('Obviously!')
    score += 1

else: 
    print ('Leo is gonna hate you now')

answer = input('Who is not fat? ').lower()
if answer == 'Leo' or 'Liam':
    print ('Thankyou')
    score += 1

else: 
    print ('Me & Leo hate you now')

answer = input('Who would win in a fight, Liam or Mike Tyson? ').lower()
if answer == 'liam':
    print ('Finally getting some appreciation')
    score += 1

else: 
    print ('You think I would get done off that old fart')

print ("You Got "  + str(score) +  " Questions Correct!")
print ("You Got "  + str((score/5)*100) +  "%")



