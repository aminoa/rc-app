# requires Python 3.10 or greater
for i in range(1, 101):
    match (i % 3, i % 5):
        case (0, 0):
            print("CracklePop")
        case (0, _):
            print("Crackle")
        case (_, 0):
            print("Pop")
        case (_, _):
            print(i)