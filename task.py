# Create a dictionary of English to Spanish translations
english_to_spanish = {
    "hello": "hola",
    "goodbye": "adiós",
    "cat": "gato"

    # Add more words and translations here
}

word = input("Enter an English word to translate to Spanish: ")

if word in english_to_spanish:
    translation = english_to_spanish[word]
    print(f"{word} in Spanish is {translation}.")
else:
    print(f"Sorry, {word} is not in the dictionary.")