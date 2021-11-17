def encode(msg):  # we compute the following function by counting the equal consecutive
    #  letters that the message has and grouping them into its number and then its letter
    count = 0
    previous_char = msg[0]
    result = ''
    length = len(msg)

    i = 0
    while i != length:
        character = msg[i]

        if previous_char == character:
            count = count + 1
        else:
            result = result + str(count) + previous_char
            count = 1
        previous_char = character
        i = i + 1

    return msg, result + str(count) + str(previous_char)
