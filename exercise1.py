#Exercise 1

documentary = 'Bowling for Columbine'
dramedy = 'The Breakfast Club'
drama = 'Gladiator'
comedy = 'Airplane!'
book = '1984'


def ask_theme(theme): #Asks user which genre they prefer.
    print('Do you like {} movies?'.format(theme))
    return input().lower()

def give_recommendation(title, media="movie"): #Gives the user a recommendation based on their choices. Media is movie by default.
    return 'You would enjoy the {} \'{}\'.'.format(media, title)


def title_recommendation(): #Asks user their preference on 3 genres. Based on their input, gives a recommendation.
    doc_input = ask_theme('Documentary')
    drama_input = ask_theme('Drama')
    comedy_input = ask_theme('Comedy')

    if (doc_input == "yes"):
        print(give_recommendation(documentary))
    elif (doc_input == "no") and (drama_input == "yes" and comedy_input == "yes"):
        print(give_recommendation(dramedy))
    elif (drama_input == "yes"):
        print(give_recommendation(drama))
    elif (comedy_input == "yes"):
        print(give_recommendation(comedy))
    else:
        print(give_recommendation(book, 'book'))

title_recommendation() #Calls the main function.