def mood_response(mood):
    if mood.lower() == 'happy':
        return("I'm glad you are having a good day!")
    elif mood.lower() == 'sad':
        return("I'm sorry, I'm sure things will turn around for you soon!")
    elif mood.lower() == 'excited':
        return("It's good to have things to look forward to!")
    else:
        return("Isn't human emotion wonderful?")