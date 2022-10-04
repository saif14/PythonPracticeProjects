import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '_', '+']

def random_pass_gen():
    print('Welcome to the Password Generator')

    number_of_letters = int(input("How many letters would like in your password?\n"))
    number_of_symbols = int(input("How many symbols would like in your password?\n"))
    number_of_numbers = int(input("How many numbers would like in your password?\n"))

    generated_pass = []

    for i in range(1, number_of_letters - number_of_numbers - number_of_symbols + 1):
        idx = random.randint(0, len(letters) - 1)
        generated_pass += letters[idx]
    for i in range(1, number_of_symbols + 1):
        idx = random.randint(0, len(symbols) - 1)
        generated_pass += symbols[idx]
    for i in range(1, number_of_numbers + 1):
        idx = random.randint(0, len(numbers) - 1)
        generated_pass += numbers[idx]

    random.shuffle(generated_pass)
    final_pass = "".join(generated_pass)

    print("Generated Password:\n " + final_pass)


