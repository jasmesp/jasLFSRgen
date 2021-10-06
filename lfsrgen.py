def form(arg):
    print("{:04b}".format(arg))


def test():
    IV = 0b1101

    for i in range(16):
        new_bit = (IV ^ (IV >> 1))
        IV = (IV >> 1) | (new_bit << 3)
        print(IV & 1, end="")


def main():
    output_length = int(input("How many digits?\n"))
    iv = (1 << 127) | 1
    for i in range(output_length):
        s_bit = (iv ^ (iv >> 1) ^ (iv >> 2) ^ (iv >> 7))
        iv = (s_bit >> 1) | (iv << 3)
        print(iv & 1, end="")
    print("")
    quit = (input("Q to exit, N to continue:\n")).lower()

    if quit == ("q"):
        pass
    else:
        main()


main()
