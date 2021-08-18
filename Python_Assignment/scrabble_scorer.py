OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Score for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints


def initial_prompt():
   print("Let's play some Scrabble!\n")
   word = input("Enter a word to be scored: ")
   return word


def simple_scorer(word):
    word = word.lower()
    letter_points = ""

    letter_points += '\nScore for {word}: {point_value} \n'.format(word = word, point_value = (len(word)))
    return letter_points

def vowel_bonus_scorer(word):
    word = word.lower()
    letter_points = ""
    num_vowels = 0
    num_consonants = 0

    for char in word:
        if char in 'aeiou':
            num_vowels += 3
        else:
            num_consonants += 1
    
    total_points = num_vowels + num_consonants
    letter_points = "\nScore for {word}: {total_points}\n".format(word = word, total_points = total_points)
    return letter_points


def scrabble_scorer(word):
    score = 0
    total_score =""

    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]
    total_score = "\nScore for {word}: {score}\n".format(word = word, score = score)
    return total_score

def scorer_prompt():
    print("\nwhich scoring algorithm would you like to use?\n")
    
    print("0- Simple: One point per character\n1- Vowel Bonus: Vowels are worth 3 points\n2- Scrabble: Uses Scrabble points system")
    choice = input('\nEnter 0, 1, or 2: ')
    algorithm_choice = int(choice)
    return algorithm_choice

def transform(old_dict):
    new_dict = {}

    for (key, value) in old_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(OLD_POINT_STRUCTURE)

scrabble_scorer_old = {
    'name': 'Scrabble', 
    'description': 'The traditional scoring algorithm', 
    'scoring_function': scrabble_scorer}

scrabble_scorer_simple = {
    'name': 'Simple Score', 
    'description': 'Each letter is worth 1 point.', 
    'scoring_function': simple_scorer}

scrabble_scorer_vowels = {'name': 'Bonus Vowels', 
'description': 'Vowels are 3 pts, consonants are 1 pt', 
'scoring_function': vowel_bonus_scorer}

scoring_algorithms = (
    scrabble_scorer_simple, 
    scrabble_scorer_vowels, 
    scrabble_scorer_old)


def run_program():
    word = initial_prompt()
    selected_dict = scorer_prompt() 
    score = scoring_algorithms[selected_dict]['scoring_function']

    result = score(word)
    print(result)


