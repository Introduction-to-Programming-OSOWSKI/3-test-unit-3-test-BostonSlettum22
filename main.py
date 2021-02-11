def countB(w):

    total = 1

    for i in range(1,len(w)):
        total = total + i

    if w[i] == "b":
        return len(w)

print(countB("boston"))



def removeLast(w):
    bazinga = w[len(w)-1]

    for i in range(2,len(w)+1):
        bazinga = w[len(w)-i] + bazinga 

    return bazinga

print(removeLast("winter"))

