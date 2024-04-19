import sys

chosen_mode = int(
    input(
        "\nIf you want to encrypt a message, please type 1.\nIf you want to decrypt a message, please type 2:\n\n"
    )
)

key = int(input("\nPlease input your key:\n"))

message = str(input("\nPlease type your message here:\n"))


alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz "]
modulo = len(alphabet)

def encrypt(message, key):
    global modulo
    final_message = ""

    for char in message:
        final_message += alphabet[(alphabet.index(char) + key) % modulo]

    print("This is your final message:\n" + final_message)
    sys.exit()
    
def decrypt(message, key):
    global modulo
    final_message = ""

    for char in message:
        final_message += alphabet[(alphabet.index(char) - key) % modulo]

    print("This is your final message:\n" + final_message)
    sys.exit()
    

if chosen_mode == 1:
    encrypt(message, key)
elif chosen_mode == 2:
    decrypt(message, key)
else:
    print("please type 1 or 2.\nExiting...\n")
    sys.exit()
