tryagain = True
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
def make_code():
    mess = input("enter the message which you wanna encode: ")
    num = int(input("enter the number how much position encode: "))
    mess1 = mess.lower()
    mess2 = len(mess1)
    count = 0
    itog = ""
    for i in range(0, mess2):
        w1 = mess1[count]
        if w1 in alfabet:
           index = alfabet.index(w1)
        w3 = index + num
        w4 = alfabet[w3]
        count = count + 1
        itog = itog+w4
    print(itog)

def decode():
    word = input("enter a decoded message: ")
    num = int(input("enter the number from decode: "))
    mess1 = word.lower()
    mess2 = len(mess1)
    count = 0
    itog = ""
    for i in range(0, mess2):
        w1 = mess1[count]
        if w1 in alfabet:
            index = alfabet.index(w1)
        w3 = index - num
        w4 = alfabet[w3]
        count = count + 1
        itog = itog+w4
    print(itog)

while tryagain == True:
    print("1) make a code")
    print("2) decode a message")
    print("3) quit")
    print()
    sel = int(input("Enter your selection: "))
    if sel == 1:
        make_code()
    elif sel == 2:
        decode()
    elif sel == 3:
        tryagain = False




