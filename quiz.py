import random 
number_to_guess =random.randint(1,100)
while True:
    try: 
        user_input=int(input('Enter a Nmber to guess : '))
        if user_input<number_to_guess:
            print('Tow low')
        elif user_input>number_to_guess:
            print('to high ')
        else:
            print(' congratulations u guessed the correct answer ')
            break
    except ValueError:
        print('enter a valid number ')
        
    


    

