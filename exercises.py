# Exercise 0: Example
def print_greeting(): # 'def' for function definition
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()



# Exercise 1: Vowel or Consonant
def check_letter():
    letter=input("Enter a letter (a-z or A-Z)").lower()
    if letter in 'aeiou':
        print(f'The letter {letter} is a vowel.')
    
    else:
        print(f'The letter {letter} is a consonant.')

check_letter()



# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    try:  # for converting the input to integer
        age = int(input("Please enter your age: "))

        if age < 0:
            print("Invalid age, negative number!")
            return

        voting_age = 21

        if age >= voting_age:
            print(f'You are {age}, You can vote.')
        else:
            print(f'You are {age}, You can`t vote, minimum age for voting is {voting_age}.')
        
    except ValueError:
        print("Invalid input. Please enter a number for the age.")

check_voting_eligibility()



# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age < 0:
            print("Invalid age, negative number!")
            return
        
        if dog_age <= 2:
            age_dogs_year= dog_age * 10
        
        else:
            age_dogs_year = 20 +(dog_age-2) * 7

        print(f'The dog`s age in dog years is {age_dogs_year}.')

    except ValueError:
        print("Invalid input. Please enter a number for the dog age.")

calculate_dog_years()



# Exercise 4: Weather Advice
def weather_advice():
    its_cold = input("It's cold (yes/no): ").lower()
    its_raining = input("It's raining (yes/no): ").lower()

    # you minsioned to use AND, OR, NOT operators
    # because I used NOT, I did not used <=='no'> 
    if its_cold=='yes' and its_raining=='yes':
        print("Wear a waterproof coat.")
    
    elif its_cold =='yes' and not(its_raining=='yes'): # can be => elif its_cold=='yes' and its_raining=='no':
        print("Wear a warm coat.")

    elif not(its_cold=='yes') and its_raining=='yes': # can be => elif its_cold=='no' and its_raining=='yes':
        print("Carry an umbrella.")
    
    elif not(its_cold=='yes') and not(its_raining=='yes'): # can be => elif its_cold=='no' and its_raining=='no':
        print("Wear light clothing.")

weather_advice()



# Exercise 5: What's the Season?
def determine_season():
    try:
        month=input("Enter the month of the year (Jan - Dec):").lower()
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        if month not in months:
            print("Invalid month input.")
            return
        
        day=int (input("Enter the day of the month:"))
        if day < 1 or day >31:
            print("Invalid day input.")
            return

        if month == 'dec' and day >=21 or month in ['jan','feb'] or month == 'mar' and day <=19:
            season = 'Winter'
        
        elif month == 'mar' and day >=20 or month in ['apr','may'] or month == 'jun' and day <=20:
            season = 'Spring'

        elif month == 'jun' and day >=21 or month in ['jul','aug'] or month == 'sep' and day <=21:
            season = 'Summer'
        
        elif month == 'sep' and day >=22 or month in ['oct','nov'] or month == 'dec' and day <=20:
            season = 'Fall'

        print(f'{month} {day} is in {season}')

    except ValueError:
        print("Invalid input. Please enter a valid number for the day.")

determine_season()



# Exercise 6: Number Guessing Game
def guess_number():
    target_num =42
    tryes = 5

    print("Guess a number between 1 and 100. You have 5 tries.")
    for attempt in range(1, tryes + 1):

        try:
            guess = int(input(f'Attempt {attempt}: Enter your guess: '))
            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess == target_num:
                print("Congratulations, you guessed correctly!")
                break
            
            elif guess < target_num:
                if attempt == tryes:
                    print("Last chance! Your guess is too low.")
                else:
                    print("Your guess is too low.")
            
            elif guess > target_num:
                if attempt == tryes:
                    print("Last chance! Your guess is too high.")
                else:
                    print("Your guess is too high.")

            if attempt == tryes:
                print("Sorry, you failed to guess the number in five attempts.")

        except ValueError:
            print("Invalid input. Please enter a number.")

guess_number()
