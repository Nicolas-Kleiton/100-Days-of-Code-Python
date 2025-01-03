from project_logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            is_upper = letter.isupper()
            shifted_position = (alphabet.index(letter.lower()) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position].upper() if is_upper else alphabet[shifted_position]

    print(f"Here is the {encode_or_decode} result: {output_text}")

print(logo)

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    if direction == "encode" or direction == "decode":
        cipher(text, shift, direction)
    else:
        print("Invalid input. You need to choose 'encode' or 'decode' ")

    while True:
        restart = input("Would you like to continue? Type 'Y' or 'N': ").upper()
        if restart == 'N':
            should_continue = False
            print("Goodbye! :)")
            break
        elif restart == 'Y':
            break
        else:
            print("Invalid input. You need to choose 'Y' or 'N'.")