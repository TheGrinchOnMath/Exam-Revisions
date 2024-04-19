chosen_mode = int(
    input(
        "If you want to encrypt a message, type 1.\n"
        + "If you want to decrypt a message, type 2.\n"
        + "-> "
    )
)

key = str(
    input(
        "please input your key. only the alphabet characters and the space bar are allowed.\n"
        + "-> "
    )
)

message = str(
    input(
        "Please input your message here. Please only use alphabet characters and space.\n"
        + "-> "
    )
)

alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz "]

modulo = len(alphabet)


def encrypt(message, key):
    message_arr = [char for char in message]
    final_message = ""
    fullkey = []

    for char in key:
        fullkey.append(alphabet.index(char))

    key_length = len(fullkey)

    for i in range(0, len(message_arr)):
        fullkey.append(fullkey[i % key_length])

    for i in range(0, len(message_arr)):
        try:
            final_message += alphabet[
                (alphabet.index(message_arr[i % modulo]) + fullkey[i % modulo]) % modulo
            ]
        except IndexError():
            print(
                (alphabet.index(message_arr[i % modulo]) + fullkey[i % modulo]) % modulo
            )
            return

    print(
        "your final message is\n-->"
        + final_message
        + "<--\nwith key:"
        + "\n-> "
        + key
        + " <-"
        + ".\nHave a nice day!"
    )


def decrypt(message, key):
    message_arr = [char for char in message]
    final_message = ""
    fullkey = []

    for char in key:
        fullkey.append(alphabet.index(char))

    key_length = len(fullkey)

    for i in range(0, len(message_arr)):
        fullkey.append(fullkey[i % key_length])

    for i in range(0, len(message_arr)):
        try:
            final_message += alphabet[
                (alphabet.index(message_arr[i % modulo]) - fullkey[i % modulo]) % modulo
            ]
        except IndexError():
            print(
                (alphabet.index(message_arr[i % modulo]) - fullkey[i % modulo]) % modulo
            )
            return

    print(
        "your final message is\n-->"
        + final_message
        + "<--\nwith key:"
        + "\n-> "
        + key
        + " <-"
        + ".\nHave a nice day!"
    )


if chosen_mode == 1:
    encrypt(message, key)
elif chosen_mode == 2:
    decrypt(message, key)
else:
    print("please type 1 or 2.\nExiting...\n")
