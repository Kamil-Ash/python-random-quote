import random
def primary(num):
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    for _ in range(num):
        rnd = random.randint(0, last)
        print(quotes[rnd],end='')

if __name__== "__main__":
    primary(2)
