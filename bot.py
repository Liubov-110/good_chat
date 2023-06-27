from chat import menu, greeting, regards


greeting()

while input('\nЄ кілька хвилин на розмову? [answer in English, please]').lower() != 'no':
    if menu() == 'quit':
        break

regards()
