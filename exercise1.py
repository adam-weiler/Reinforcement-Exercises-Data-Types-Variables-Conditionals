documentary = 'Bowling for Columbine'
dramedy = 'The Breakfast Club'
drama = 'Gladiator'
comedy = 'Airplane!'
book = '1984'


def ask_theme(theme):
    print('Do you like {} movies?'.format(theme))
    return input()


def movie_recommendation():
    doc_input = ask_theme('Documentary')
    drama_input = ask_theme('Drama')
    comedy_input = ask_theme('Comedy')

    print(doc_input)
    print(drama_input)
    print(comedy_input)



movie_recommendation()