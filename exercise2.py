#Exercise 2

documentary = 'Bowling for Columbine'
dramedy = 'The Breakfast Club'
drama = 'Gladiator'
comedy = 'Airplane!'
book = '1984'


def ask_theme(theme): #Asks user which genre they prefer.
    while (True): #Will look until user gives valid number.
        print('On a scale of 1 to 5, how do you like {} movies?'.format(theme))

        answer = int(input())

        if (answer >= 0) and (answer <= 5):
            return answer
        else:
            print('That answer is not recognized.')


def give_recommendation(title, genre): #Gives the user a recommendation based on their choices.
    return 'You would enjoy \'{}\'. It is a {}.'.format(title, genre)


def title_recommendation(): #Asks user their preference on 3 genres. Based on their input, gives a recommendation.
    doc_input = ask_theme('Documentary')
    drama_input = ask_theme('Drama')
    comedy_input = ask_theme('Comedy')

    if (doc_input >= 4) or (doc_input > drama_input) and (doc_input > comedy_input): #Rated Documentary at least 4, or rated Documentary higher than the other options.
        print(give_recommendation(documentary, 'Documentary'))
    elif (doc_input <= 3) and (drama_input >= 4 and comedy_input >= 4): #Rated Documentary no more than 3, and rated the other options at least 4.
        print(give_recommendation(dramedy, 'Dramedy'))
    elif (drama_input >= 4) or (drama_input > doc_input) and (drama_input > comedy_input): #Rated Drama at least 4, or rated Drama higher than the other options.
        print(give_recommendation(drama, 'Drama'))
    elif (comedy_input >= 4) or (comedy_input > doc_input) and (comedy_input > drama_input): #Rated Comedy at least 4, or rated Comedy higher than the other options.
        print(give_recommendation(comedy, 'Comedy'))
    else: #Otherwise, recommend a book.
        print(give_recommendation(book, 'book'))

title_recommendation() #Calls the main function.