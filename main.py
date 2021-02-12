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



def sumBetweenOdd(x,y):
    bazinga = 1
    for i in range(x%2==0,y):
        bazinga = bazinga + i
    
    return bazinga

print(sumBetweenOdd(4,13))




def FirstLast(w):

    if w[0] == w[-1]:
        return True
    
    return False

print(FirstLast("roar"))
    