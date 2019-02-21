import json
from difflib import get_close_matches


dictionary = json.load(open("dictionary.json"))


def get_definition(target_word):
    # Convert target to lower case to eliminate case sensitivity
    target_word = target_word.lower()
    # If the target is contained within the dict
    if target_word in dictionary:
        # Retrieve the definition from the dict
        definition = dictionary[target_word]
        # Return a formatted string of the word (key) and definition (value)
        return f"{target_word}: {definition}"
    else:
        # Using the sequence comparison module difflib to find close matches
        close_matches = get_close_matches(target_word, dictionary.keys())
        # If any close matches are found, present the to the user and ask them to select one
        if len(close_matches) > 1:
            print(
                f"Your word was not found. Here are up to 3 close matches for your original input: {close_matches}. ", end='')
            user_selection_index = int(
                input("Type 1-3 to select a word. \n")) - 1
            # Change the target to the newly selected word from close matches
            corrected_target_word = close_matches[user_selection_index]
            # Retrieve the definition of the new target
            definition = dictionary[corrected_target_word]
            # Return a formatted string of the new word (key) and definition (value)
            return f"{corrected_target_word}: {definition}"
        # If no close matches are found, tell the user the word nor any close matches were found
        else:
            return f"{target_word} not found. No similar words found either. Please try another word!"


user_word = input("Please enter a word to search the dictionary for: \n")
print(get_definition(user_word))
